from universal_serial_bus.orm import ModelBuilder, OrmClassBase



def map_db_objects(db_url):
    engine, meta, tables, session = ModelBuilder.get_db_objects(db_url)
    script = ModelBuilder._gen_mapping_strings(db_url, print_out = False)
    exec(script)
    return engine, meta, tables, session



class Ac3FormatSpecificDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('wFormatTag', 2), ('bmBSID', 4),
                    ('bmAC3Features', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, wFormatTag, bmBSID, bmAC3Features,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.wFormatTag = wFormatTag
        self.bmBSID = bmBSID
        self.bmAC3Features = bmAC3Features



class ContinuousSamplingFrequency(OrmClassBase):
    fields_sizes = [('tLowerSamFreq', 3), ('tUpperSamFreq', 3), ]


    def __init__(self, tLowerSamFreq, tUpperSamFreq, parent_id = None):
        self.parent_id = parent_id
        self.tLowerSamFreq = tLowerSamFreq
        self.tUpperSamFreq = tUpperSamFreq



class DiscreteNumberOfSamplingFrequencie(OrmClassBase):
    fields_sizes = [('tSamFreq__1_', 3), ('tSamFreq__ns_', 3), ]


    def __init__(self, tSamFreq__1_, tSamFreq__ns_, parent_id = None):
        self.parent_id = parent_id
        self.tSamFreq__1_ = tSamFreq__1_
        self.tSamFreq__ns_ = tSamFreq__ns_



class DualChannelControlParameterBlock(OrmClassBase):
    fields_sizes = [('BChannel2Enable', 1), ]


    def __init__(self, BChannel2Enable, parent_id = None):
        self.parent_id = parent_id
        self.BChannel2Enable = BChannel2Enable



class DynamicRangeControlParameterBlock(OrmClassBase):
    fields_sizes = [('bEnable', 1), ]


    def __init__(self, bEnable, parent_id = None):
        self.parent_id = parent_id
        self.bEnable = bEnable



class HighLowScalingControlParameterBlock(OrmClassBase):
    fields_sizes = [('bLowScale', 1), ('bHighScale', 1), ]


    def __init__(self, bLowScale, bHighScale, parent_id = None):
        self.parent_id = parent_id
        self.bLowScale = bLowScale
        self.bHighScale = bHighScale



class ModeControlParameterBlock(OrmClassBase):
    fields_sizes = [('bMode', 1), ]


    def __init__(self, bMode, parent_id = None):
        self.parent_id = parent_id
        self.bMode = bMode



class MpegFormatSpecificDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('wFormatTag', 2),
                    ('bmMPEGCapabilities', 2), ('bmMPEGFeatures', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, wFormatTag, bmMPEGCapabilities, bmMPEGFeatures,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.wFormatTag = wFormatTag
        self.bmMPEGCapabilities = bmMPEGCapabilities
        self.bmMPEGFeatures = bmMPEGFeatures



class MultilingualControlParameterBlock(OrmClassBase):
    fields_sizes = [('bMultiLingual', 1), ]


    def __init__(self, bMultiLingual, parent_id = None):
        self.parent_id = parent_id
        self.bMultiLingual = bMultiLingual



class ScalingControlParameterBlock(OrmClassBase):
    fields_sizes = [('bScale', 1), ]


    def __init__(self, bScale, parent_id = None):
        self.parent_id = parent_id
        self.bScale = bScale



class SecondStereoControlParameterBlock(OrmClassBase):
    fields_sizes = [('B2ndStereoEnable', 1), ]


    def __init__(self, B2ndStereoEnable, parent_id = None):
        self.parent_id = parent_id
        self.B2ndStereoEnable = B2ndStereoEnable



class TypeIFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('bNrChannels', 1), ('bSubframeSize', 1), ('bBitResolution', 1), ('bSamFreqType', 1),
                    ('tSamFreq', 3), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, bNrChannels, bSubframeSize,
                 bBitResolution, bSamFreqType, tSamFreq, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.bNrChannels = bNrChannels
        self.bSubframeSize = bSubframeSize
        self.bBitResolution = bBitResolution
        self.bSamFreqType = bSamFreqType
        self.tSamFreq = tSamFreq



class TypeIiFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('wMaxBitRate', 2), ('wSamplesPerFrame', 2), ('bSamFreqType', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, wMaxBitRate, wSamplesPerFrame,
                 bSamFreqType, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.wMaxBitRate = wMaxBitRate
        self.wSamplesPerFrame = wSamplesPerFrame
        self.bSamFreqType = bSamFreqType



class TypeIiiFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('bNrChannels', 1), ('bSubframeSize', 1), ('bBitResolution', 1), ('bSamFreqType', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, bNrChannels, bSubframeSize,
                 bBitResolution, bSamFreqType, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.bNrChannels = bNrChannels
        self.bSubframeSize = bSubframeSize
        self.bBitResolution = bBitResolution
        self.bSamFreqType = bSamFreqType
