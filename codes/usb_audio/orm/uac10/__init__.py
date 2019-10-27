import usb.core

from universal_serial_bus.orm.usb20.descriptors import *
from .descriptors import *
from .formats.descriptors import *
from .. import UACdevice, byte_array_to_int, AttrDict, array, MUTE_CONTROL_ID, VOLUME_CONTROL_ID, \
    LEN_MUTE_VALUE, LEN_VOLUME_VALUE


int_eq_hex = OrmClassBase.int_eq_hex
int_to_hex = OrmClassBase.int_to_hex

LEN_FREQ_BYTES = 3
AUDIO_CLASS_SPECIFIC_REQUEST_CODE = AttrDict({'SET_CUR': 0x01,
                                              'GET_CUR': 0x81,
                                              'GET_MIN': 0x82,
                                              'GET_MAX': 0x83,
                                              'GET_RES': 0x84,
                                              'SET_RES': 0x05,
                                              'GET_MEM': 0x85})



class UACdevice(UACdevice):
    __version__ = '1.0'


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
            _class = AssociatedInterfacesDescriptor

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
                            '09': ExtensionUnitDescriptor}

                _class = _classes[int_to_hex(descriptor[2]).upper()]

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsInterfaceDescriptor,
                            '02': TypeIFormatTypeDescriptor}

                _class = _classes[int_to_hex(descriptor[2]).upper()]

        if int_eq_hex(descriptor[1], '25'):  # 如果是 CS_ENDPOINT
            if intf_type == "AC":
                pass  # There is no class-specific AudioControl interrupt endpoint descriptor

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsIsochronousAudioDataEndpointDescriptor}

                _class = _classes[int_to_hex(descriptor[2]).upper()]

        return _class, intf_type


    def get_sampling_freq(self, endpoint_id, bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['GET_CUR']):
        return byte_array_to_int(
            self.get_control_attributes(interface_or_endpoint_id = endpoint_id, is_interface = False,
                                        bRequest = bRequest, data_or_wLength = LEN_FREQ_BYTES))


    def set_sampling_freq(self, endpoint_id, freq = 44100):
        return self.set_control_attributes(interface_or_endpoint_id = endpoint_id, is_interface = False,
                                           bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['SET_CUR'],
                                           data_or_wLength = self._gen_sampling_freq_bytes(freq, LEN_FREQ_BYTES))


    def get_sampling_freqs(self, endpoint_id):

        def _validate_freq(freq):
            self.set_sampling_freq(endpoint_id, freq)
            return self.get_sampling_freq(endpoint_id) == freq


        try:
            freq_min = self.get_sampling_freq(endpoint_id, bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['GET_MIN'])
            freq_max = self.get_sampling_freq(endpoint_id, bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['GET_MAX'])
            freq_res = self.get_sampling_freq(endpoint_id, bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['GET_RES'])
        except usb.core.USBError  as e:
            raise usb.core.USBError('Check bSamFreqType & tSamFreq in TypeFormatTypeDescriptor.')

        return [freq for freq in range(freq_min - freq_res, freq_max + freq_res, freq_res) if _validate_freq(freq)]


    def get_mute(self, entity_id):
        mute = self.get_control_attributes(entity_id = entity_id, control_id = MUTE_CONTROL_ID,
                                           data_or_wLength = LEN_MUTE_VALUE,
                                           bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['GET_CUR'])
        return mute[0] == 1


    def set_mute(self, entity_id, mute = False):
        return self.set_control_attributes(entity_id = entity_id, control_id = MUTE_CONTROL_ID,
                                           data_or_wLength = array('B', [int(mute)]),
                                           bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['SET_CUR'])


    def get_volume(self, entity_id):
        volume_bytes = self.get_control_attributes(entity_id = entity_id, control_id = VOLUME_CONTROL_ID,
                                                   data_or_wLength = LEN_VOLUME_VALUE,
                                                   bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['GET_CUR'])
        return self._volume_bytes_to_db(volume_bytes)


    def set_volume(self, entity_id, volume_db = -60):
        return self.set_control_attributes(entity_id = entity_id, control_id = VOLUME_CONTROL_ID,
                                           data_or_wLength = self._db_to_volume_bytes(volume_db),
                                           bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['SET_CUR'])
