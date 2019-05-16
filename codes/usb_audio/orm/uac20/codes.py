from universal_serial_bus.orm import ModelBuilder, OrmClassBase



def map_db_objects(db_url):
    engine, meta, tables, session = ModelBuilder.get_db_objects(db_url)
    script = ModelBuilder._gen_mapping_strings(db_url, print_out = False)
    exec(script)
    return engine, meta, tables, session



class Ac3DecoderControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class AudioClassSpecificAcInterfaceDescriptorSubtype(OrmClassBase):
    fields_sizes = []


    def __init__(self, descriptor_subtype, value):
        self.descriptor_subtype = descriptor_subtype
        self.value = value



class AudioClassSpecificAsInterfaceDescriptorSubtype(OrmClassBase):
    fields_sizes = []


    def __init__(self, descriptor_subtype, value):
        self.descriptor_subtype = descriptor_subtype
        self.value = value



class AudioClassSpecificDescriptorType(OrmClassBase):
    fields_sizes = []


    def __init__(self, descriptor_type, value):
        self.descriptor_type = descriptor_type
        self.value = value



class AudioClassSpecificEndpointDescriptorSubtype(OrmClassBase):
    fields_sizes = []


    def __init__(self, descriptor_subtype, value):
        self.descriptor_subtype = descriptor_subtype
        self.value = value



class AudioClassSpecificRequestCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, class_specific_request_code, value):
        self.class_specific_request_code = class_specific_request_code
        self.value = value



class AudioFunctionCategoryCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_function_subclass_code, value):
        self.audio_function_subclass_code = audio_function_subclass_code
        self.value = value



class AudioFunctionClassCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_function_class_code, value):
        self.audio_function_class_code = audio_function_class_code
        self.value = value



class AudioFunctionProtocolCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_function_protocol_code, value):
        self.audio_function_protocol_code = audio_function_protocol_code
        self.value = value



class AudioFunctionSubclassCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_function_subclass_code, value):
        self.audio_function_subclass_code = audio_function_subclass_code
        self.value = value



class AudioInterfaceClassCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_interface_class_code, value):
        self.audio_interface_class_code = audio_interface_class_code
        self.value = value



class AudioInterfaceProtocolCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_interface_protocol_code, value):
        self.audio_interface_protocol_code = audio_interface_protocol_code
        self.value = value



class AudioInterfaceSubclassCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, audio_interface_subclass_code, value):
        self.audio_interface_subclass_code = audio_interface_subclass_code
        self.value = value



class AudiostreamingInterfaceControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class ClockMultiplierControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class ClockSelectorControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class ClockSourceControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class DecoderTypeCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, decoder_type_code, value):
        self.decoder_type_code = decoder_type_code
        self.value = value



class DolbyPrologicProcessingUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class DtsDecoderControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class DynamicRangeCompressorEffectUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class EffectUnitEffectType(OrmClassBase):
    fields_sizes = []


    def __init__(self, weffecttype, value):
        self.weffecttype = weffecttype
        self.value = value



class EncoderControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class EncoderTypeCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, encoder_type_code, value):
        self.encoder_type_code = encoder_type_code
        self.value = value



class EndpointControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class ExtensionUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class FeatureUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class MixerControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class ModulationDelayEffectUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class MpegDecoderControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class ProcessingUnitProcessType(OrmClassBase):
    fields_sizes = []


    def __init__(self, wprocesstype, value):
        self.wprocesstype = wprocesstype
        self.value = value



class ReverberationEffectUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class SelectorControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class StereoExtenderProcessingUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class TerminalControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class UpDownMixProcessingUnitControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class WmaDecoderControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value
