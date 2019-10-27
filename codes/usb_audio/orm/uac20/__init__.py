from array import array

from orm.tools import AttrDict
from universal_serial_bus import Endpoint
from universal_serial_bus.legacy import ENDPOINT
from universal_serial_bus.orm.usb20.descriptors import *
from .descriptors import *
from .formats.descriptors import *
from .. import UACdevice, AUDIO_CLASS_SPECIFIC_REQUEST_CODE


int_eq_hex = OrmClassBase.int_eq_hex
int_to_hex = OrmClassBase.int_to_hex
byte_array_to_hex = OrmClassBase.byte_array_to_hex
byte_array_to_int = OrmClassBase.byte_array_to_int

INTERRUPT_DATA_MESSAGE_LENGTH = 6



class InterruptDataMessage:

    def __init__(self, entity_id, control_id = 1, channel_no = 0, interface_or_endpoint_id = 0,
                 is_class_specific = True, from_interface = True,
                 bAttribute = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['CUR']):
        self.entity_id = entity_id
        self.control_id = control_id
        self.channel_no = channel_no
        self.interface_or_endpoint_id = interface_or_endpoint_id
        self.is_class_specific = is_class_specific
        self.from_interface = from_interface
        self.bAttribute = bAttribute


    @classmethod
    def from_byte_array(cls, message_byte_array):
        assert len(message_byte_array) == INTERRUPT_DATA_MESSAGE_LENGTH, 'Message should be 6 bytes long.'

        return InterruptDataMessage(entity_id = message_byte_array[5],
                                    control_id = message_byte_array[3],
                                    channel_no = message_byte_array[2],
                                    interface_or_endpoint_id = message_byte_array[4],
                                    bAttribute = message_byte_array[1],
                                    is_class_specific = (message_byte_array[0] & 0x01) == 0,
                                    from_interface = (message_byte_array[0] & 0x02) == 0)


    @property
    def bInfo(self):
        return (not self.from_interface) << 1 | (not self.is_class_specific)


    @property
    def wValue(self):
        return array('B', [self.channel_no, self.control_id])


    @property
    def wIndex(self):
        return array('B', [self.interface_or_endpoint_id, self.entity_id])


    @property
    def byte_array(self):
        return array('B', [self.bInfo, self.bAttribute]) + self.wValue + self.wIndex


    @property
    def is_vendor_specific(self):
        return not self.is_class_specific


    @property
    def from_endpoint(self):
        return not self.from_interface



class Endpoint(Endpoint):

    def get_interrupt_message(self):
        assert self.transfer_type == ENDPOINT.TRANSFER_TYPE.INTERRUPT, 'Must be an interrupt endpoint.'
        byte_array = self.read(INTERRUPT_DATA_MESSAGE_LENGTH)
        return InterruptDataMessage(byte_array)



class UACdevice(UACdevice):
    __version__ = '2.0'


    @classmethod
    def _categorize(cls, descriptor, intf_type = None):

        _class = None

        if int_eq_hex(descriptor[1], '01'):  # 如果是 device
            _class = StandardDeviceDescriptor

        if int_eq_hex(descriptor[1], '02'):  # 如果是 config
            _class = StandardConfigurationDescriptor

        if int_eq_hex(descriptor[1], '04'):  # 如果是 interface
            _class = StandardInterfaceDescriptor

            if int_eq_hex(descriptor[5], '03'):  # 如果是 HID
                intf_type = "HID"

            if int_eq_hex(descriptor[5], '01'):  # 如果是 audio

                if int_eq_hex(descriptor[6], '01'):  # 如果是 AC interface
                    intf_type = "AC"
                    _class = StandardAcInterfaceDescriptor

                if int_eq_hex(descriptor[6], '02'):  # 如果是 AS interface
                    intf_type = "AS"
                    _class = StandardAsInterfaceDescriptor

        if int_eq_hex(descriptor[1], '05'):  # 如果是 endpoint
            _class = StandardEndpointDescriptor

            if intf_type == "HID":
                pass

            if intf_type == "AC":
                _class = StandardAcInterruptEndpointDescriptor

            if intf_type == "AS":
                _class = StandardAsIsochronousAudioDataEndpointDescriptor

        if int_eq_hex(descriptor[1], '0B'):  # 如果是 interface association
            _class = StandardInterfaceAssociationDescriptor

        if int_eq_hex(descriptor[1], '24'):  # 如果是 CS_INTERFACE
            if intf_type == "AC":
                _classes = {'00': None,
                            '01': ClassSpecificAcInterfaceHeaderDescriptor,
                            '02': InputTerminalDescriptor,
                            '03': OutputTerminalDescriptor,
                            '04': MixerUnitDescriptor,
                            '05': SelectorUnitDescriptor,
                            '06': FeatureUnitDescriptor,
                            '07': 'EFFECT_UNIT',
                            '08': 'PROCESSING_UNIT',
                            '09': ExtensionUnitDescriptor,
                            '0A': ClockSourceDescriptor,
                            '0B': ClockSelectorDescriptor,
                            '0C': ClockMultiplierDescriptor,
                            '0D': SamplingRateConverterUnitDescriptor}

                _class = _classes[int_to_hex(descriptor[2]).upper()]

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsInterfaceDescriptor,
                            '02': TypeIFormatTypeDescriptor,
                            '03': EncoderDescriptor,
                            '04': 'DECODER'}

                _class = _classes[int_to_hex(descriptor[2]).upper()]

        if int_eq_hex(descriptor[1], '25'):  # 如果是 CS_ENDPOINT
            if intf_type == "AC":
                pass  # There is no class-specific AudioControl interrupt endpoint descriptor

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsIsochronousAudioDataEndpointDescriptor}

                _class = _classes[int_to_hex(descriptor[2]).upper()]

        return _class, intf_type



class MicrophoneArrayGeometry(MicrophoneArrayGeometryDescriptor):
    MIC_ARRAY_TYPE = AttrDict({'Linear': 0x00, 'Planar': 0x01, 'Dimensional': 0x02, 'Reserved': 0x03})
    MICROPHONE_TYPE = AttrDict({'OmniDirectional': 0x00,
                                'SubCardioid'    : 0x01,
                                'Cardioid'       : 0x02,
                                'SuperCardioid'  : 0x03,
                                'HyperCardioid'  : 0x04,
                                'Shaped'         : 0x05,
                                'VendorDefined'  : 0x00F})


    @classmethod
    def from_byte_array(cls, byte_array, parent_id = None):
        geo = super().from_byte_array(byte_array, parent_id)
        n_mics = geo.number_of_mics
        geo.number_of_mics = 0
        
        for i in range(n_mics):
            idx_base = 36 + i * 2 * 6
            params = dict(wMicrophoneType = byte_array_to_int(byte_array[idx_base + 0:idx_base + 2], signed = True),
                          wXCoordinate = byte_array_to_int(byte_array[idx_base + 2:idx_base + 4], signed = True),
                          wYCoordinate = byte_array_to_int(byte_array[idx_base + 4:idx_base + 6], signed = True),
                          wZCoordinate = byte_array_to_int(byte_array[idx_base + 6:idx_base + 8], signed = True),
                          wMicVertAngle = byte_array_to_int(byte_array[idx_base + 8:idx_base + 10], signed = True),
                          wMicHorAngle = byte_array_to_int(byte_array[idx_base + 10:idx_base + 12], signed = True))
            geo.add_mic(params)

        return geo


    @classmethod
    def degree_to_angle(cls, degree):
        return int(degree / 180 * 31416)


    def _refresh_length(self):
        self.set_attr_hex_value_from_int('wDescriptorLength', self.length)


    def set_guid(self, guid):
        self.set_attr_hex_value_from_int('guidMicArrayID', guid)


    def add_mic(self, params = dict(wMicrophoneType = MICROPHONE_TYPE['OmniDirectional'],
                                    wXCoordinate = 0,
                                    wYCoordinate = 0,
                                    wZCoordinate = 0,
                                    wMicVertAngle = 0,
                                    wMicHorAngle = 0)):
        for attr_name in ['wMicrophoneType', 'wXCoordinate', 'wYCoordinate',
                          'wZCoordinate', 'wMicVertAngle', 'wMicHorAngle']:
            length = self.get_size_of_field('{}_0_'.format(attr_name))
            self.setattr(attr_name = '{}_{}_'.format(attr_name, self.number_of_mics),
                         attr_value = self.int_to_hex(params[attr_name], length = length, signed = True),
                         size = length,
                         idx = None)

        self.number_of_mics += 1
        self._refresh_length()


    @property
    def bLength(self):
        return self.wDescriptorLength


    @property
    def number_of_mics(self):
        return self.hex_to_int(self.wNumberOfMics)


    @number_of_mics.setter
    def number_of_mics(self, number_of_mics):
        self.set_attr_hex_value_from_int('wNumberOfMics', number_of_mics)
