from universal_serial_bus.orm.usb20.descriptors import *
from .descriptors import *
from .formats.descriptors import *
from .. import UACdevice



class UACdevice(UACdevice):

    def _categorize(self, descriptor, intf_type = None):

        def is_a(descpt, i, code):
            return OrmClassBase.int_eq_hex(descpt[i], code)

        def get_code(descpt, i):
            return  OrmClassBase.int_to_hex(descpt[i])

        _class = None

        if is_a(descriptor, 1, '02'):  # 如果是 config
            _class = StandardConfigurationDescriptor

        if is_a(descriptor, 1, '05'):  # 如果是 endpoint
            if intf_type == "HID":
                _class = StandardEndpointDescriptor

            if intf_type == "AS":
                _class = StandardAsIsochronousAudioDataEndpointDescriptor

        if is_a(descriptor, 1, '04'):  # 如果是 interface

            _class = StandardInterfaceDescriptor

            if is_a(descriptor, 5, '03'):  # 如果是 HID
                intf_type = "HID"

            if is_a(descriptor, 5, '01'):  # 如果是 audio
                if is_a(descriptor, 6, '01'):  # 如果是 AC interface
                    intf_type = "AC"
                if is_a(descriptor, 6, '02'):  # 如果是 AC interface
                    intf_type = "AS"

        if is_a(descriptor, 1, '24'):  # 如果是 CS_INTERFACE
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

                _class = _classes[get_code(descriptor,2)]

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsInterfaceDescriptor,
                            '02': TypeIFormatTypeDescriptor,
                            '03': EncoderDescriptor,
                            '04': 'DECODER'}

                _class = _classes[get_code(descriptor,2)]

        if is_a(descriptor, 1, '25'):  # 如果是 CS_ENDPOINT
            if intf_type == "AC":
                pass

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsIsochronousAudioDataEndpointDescriptor}

                _class = _classes[get_code(descriptor,2)]

        return _class, intf_type
