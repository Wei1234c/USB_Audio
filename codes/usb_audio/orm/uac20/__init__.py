from universal_serial_bus.orm.usb20.descriptors import *
from .descriptors import *
from .formats.descriptors import *
from .. import UACdevice



class UACdevice(UACdevice):

    def _categorize(self, descriptor, intf_type = None):

        def is_a(descpt, i, code):
            return OrmClassBase.int_eq_hex(descpt[i], code)


        _class = None

        if is_a(descriptor, 1, '02'):  # 如果是 config
            _class = StandardConfigurationDescriptor

        if is_a(descriptor, 1, '05'):  # 如果是 endpoint
            if intf_type == "AS":
                _class = StandardAsIsochronousAudioDataEndpointDescriptor
            if intf_type == "HID":
                pass

        if is_a(descriptor, 1, '04'):  # 如果是 interface

            _class = StandardInterfaceDescriptor

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

                code = OrmClassBase.int_to_hex(descriptor[2])
                _class = _classes[code]

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsInterfaceDescriptor,
                            '02': TypeIFormatTypeDescriptor,
                            '03': EncoderDescriptor,
                            '04': 'DECODER'}

                code = OrmClassBase.int_to_hex(descriptor[2])
                _class = _classes[code]

        if is_a(descriptor, 1, '25'):  # 如果是 CS_ENDPOINT
            if intf_type == "AC":
                pass

            if intf_type == "AS":
                _classes = {'00': None,
                            '01': ClassSpecificAsIsochronousAudioDataEndpointDescriptor}

                code = OrmClassBase.int_to_hex(descriptor[2])
                _class = _classes[code]

        return _class, intf_type
