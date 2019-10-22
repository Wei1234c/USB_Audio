from array import array

from universal_serial_bus import Endpoint
from universal_serial_bus.orm.usb20.descriptors import *
from .descriptors import *
from .formats.descriptors import *
from .. import UACdevice, AUDIO_CLASS_SPECIFIC_REQUEST_CODE


int_eq_hex = OrmClassBase.int_eq_hex
int_to_hex = OrmClassBase.int_to_hex
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
