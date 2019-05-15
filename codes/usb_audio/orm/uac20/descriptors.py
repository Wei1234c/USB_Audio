from universal_serial_bus.orm import OrmClassBase



class Ac3DecoderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bDecoderID', 1),
                    ('bDecoder', 1), ('bmBSID', 4), ('bmAC3Features', 1), ('bmControls', 1), ('iDecoder', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bDecoderID, bDecoder, bmBSID, bmAC3Features,
                 bmControls, iDecoder, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bDecoderID = bDecoderID
        self.bDecoder = bDecoder
        self.bmBSID = bmBSID
        self.bmAC3Features = bmAC3Features
        self.bmControls = bmControls
        self.iDecoder = iDecoder



class AudioChannelClusterDescriptor(OrmClassBase):
    fields_sizes = [('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ]


    def __init__(self, bNrChannels, bmChannelConfig, iChannelNames, parent_id = None):
        self.parent_id = parent_id
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames



class ClassSpecificAcInterfaceHeaderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bcdADC', 2), ('bCategory', 1),
                    ('wTotalLength', 2), ('bmControls', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bcdADC, bCategory, wTotalLength, bmControls,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bcdADC = bcdADC
        self.bCategory = bCategory
        self.wTotalLength = wTotalLength
        self.bmControls = bmControls



class ClassSpecificAsInterfaceDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bTerminalLink', 1),
                    ('bmControls', 1), ('bFormatType', 1), ('bmFormats', 4), ('bNrChannels', 1), ('bmChannelConfig', 4),
                    ('iChannelNames', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bTerminalLink, bmControls, bFormatType, bmFormats,
                 bNrChannels, bmChannelConfig, iChannelNames, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bTerminalLink = bTerminalLink
        self.bmControls = bmControls
        self.bFormatType = bFormatType
        self.bmFormats = bmFormats
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames



class ClassSpecificAsIsochronousAudioDataEndpointDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bmAttributes', 1),
                    ('bmControls', 1), ('bLockDelayUnits', 1), ('wLockDelay', 2), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bmAttributes, bmControls, bLockDelayUnits,
                 wLockDelay, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bmAttributes = bmAttributes
        self.bmControls = bmControls
        self.bLockDelayUnits = bLockDelayUnits
        self.wLockDelay = wLockDelay



class ClockMultiplierDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bClockID', 1),
                    ('bCSourceID', 1), ('bmControls', 1), ('iClockMultiplier', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bClockID, bCSourceID, bmControls, iClockMultiplier,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bClockID = bClockID
        self.bCSourceID = bCSourceID
        self.bmControls = bmControls
        self.iClockMultiplier = iClockMultiplier



class ClockSelectorDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bClockID', 1),
                    ('bNrInPins', 1), ('baCSourceID_1_', 1), ('baCSourceID__p_', 1), ('bmControls', 1),
                    ('iClockSelector', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bClockID, bNrInPins, baCSourceID_1_,
                 baCSourceID__p_, bmControls, iClockSelector, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bClockID = bClockID
        self.bNrInPins = bNrInPins
        self.baCSourceID_1_ = baCSourceID_1_
        self.baCSourceID__p_ = baCSourceID__p_
        self.bmControls = bmControls
        self.iClockSelector = iClockSelector



class ClockSourceDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bClockID', 1),
                    ('bmAttributes', 1), ('bmControls', 1), ('bAssocTerminal', 1), ('iClockSource', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bClockID, bmAttributes, bmControls, bAssocTerminal,
                 iClockSource, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bClockID = bClockID
        self.bmAttributes = bmAttributes
        self.bmControls = bmControls
        self.bAssocTerminal = bAssocTerminal
        self.iClockSource = iClockSource



class ClusterControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ]


    def __init__(self, bNrChannels, bmChannelConfig, iChannelNames, parent_id = None):
        self.parent_id = parent_id
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames



class CommonPartOfTheEffectUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wEffectType', 2), ('bSourceID', 1), ('bmaControls_0_', 4), ('bmaControls_1_', 4),
                    ('bmaControls_ch_', 4), ('iEffects', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wEffectType, bSourceID, bmaControls_0_,
                 bmaControls_1_, bmaControls_ch_, iEffects, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wEffectType = wEffectType
        self.bSourceID = bSourceID
        self.bmaControls_0_ = bmaControls_0_
        self.bmaControls_1_ = bmaControls_1_
        self.bmaControls_ch_ = bmaControls_ch_
        self.iEffects = iEffects



class CommonPartOfTheProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('baSourceID_1_', 1), ('baSourceID__p_', 1),
                    ('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ('bmControls', 2),
                    ('iProcessing', 1), ('Process_specific', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, baSourceID_1_,
                 baSourceID__p_, bNrChannels, bmChannelConfig, iChannelNames, bmControls, iProcessing, Process_specific,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.baSourceID_1_ = baSourceID_1_
        self.baSourceID__p_ = baSourceID__p_
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iProcessing = iProcessing
        self.Process_specific = Process_specific



class ConnectorControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ]


    def __init__(self, bNrChannels, bmChannelConfig, iChannelNames, parent_id = None):
        self.parent_id = parent_id
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames



class DolbyPrologicClusterDescriptor(OrmClassBase):
    fields_sizes = [('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ]


    def __init__(self, bNrChannels, bmChannelConfig, iChannelNames, parent_id = None):
        self.parent_id = parent_id
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames



class DolbyPrologicProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('bmChannelConfig', 4),
                    ('iChannelNames', 1), ('bmControls', 2), ('iProcessing', 1), ('bNrModes', 1), ('daModes_1_', 4),
                    ('daModes_m_', 4), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, bmChannelConfig, iChannelNames, bmControls, iProcessing, bNrModes, daModes_1_, daModes_m_,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iProcessing = iProcessing
        self.bNrModes = bNrModes
        self.daModes_1_ = daModes_1_
        self.daModes_m_ = daModes_m_



class DtsDecoderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bDecoderID', 1),
                    ('bDecoder', 1), ('bmCapabilities', 1), ('bmControls', 1), ('iDecoder', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bDecoderID, bDecoder, bmCapabilities, bmControls,
                 iDecoder, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bDecoderID = bDecoderID
        self.bDecoder = bDecoder
        self.bmCapabilities = bmCapabilities
        self.bmControls = bmControls
        self.iDecoder = iDecoder



class DynamicRangeCompressorEffectUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wEffectType', 2), ('bSourceID', 1), ('bmaControls_0_', 4), ('bmaControls_1_', 4),
                    ('bmaControls_ch_', 4), ('iEffects', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wEffectType, bSourceID, bmaControls_0_,
                 bmaControls_1_, bmaControls_ch_, iEffects, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wEffectType = wEffectType
        self.bSourceID = bSourceID
        self.bmaControls_0_ = bmaControls_0_
        self.bmaControls_1_ = bmaControls_1_
        self.bmaControls_ch_ = bmaControls_ch_
        self.iEffects = iEffects



class EncoderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bEncoderID', 1),
                    ('bEncoder', 1), ('bmControls', 4), ('iParam1', 1), ('iParam2', 1), ('iParam3', 1), ('iParam4', 1),
                    ('iParam5', 1), ('iParam6', 1), ('iParam7', 1), ('iParam8', 1), ('iEncoder', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bEncoderID, bEncoder, bmControls, iParam1, iParam2,
                 iParam3, iParam4, iParam5, iParam6, iParam7, iParam8, iEncoder, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bEncoderID = bEncoderID
        self.bEncoder = bEncoder
        self.bmControls = bmControls
        self.iParam1 = iParam1
        self.iParam2 = iParam2
        self.iParam3 = iParam3
        self.iParam4 = iParam4
        self.iParam5 = iParam5
        self.iParam6 = iParam6
        self.iParam7 = iParam7
        self.iParam8 = iParam8
        self.iEncoder = iEncoder



class ExtensionUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wExtensionCode', 2), ('bNrInPins', 1), ('baSourceID_1_', 1), ('baSourceID__p_', 1),
                    ('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ('bmControls', 1),
                    ('iExtension', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wExtensionCode, bNrInPins, baSourceID_1_,
                 baSourceID__p_, bNrChannels, bmChannelConfig, iChannelNames, bmControls, iExtension, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wExtensionCode = wExtensionCode
        self.bNrInPins = bNrInPins
        self.baSourceID_1_ = baSourceID_1_
        self.baSourceID__p_ = baSourceID__p_
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iExtension = iExtension



class FeatureUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bSourceID', 1),
                    ('bmaControls_0_', 4), ('bmaControls_1_', 4), ('bmaControls_ch_', 4), ('iFeature', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bSourceID, bmaControls_0_, bmaControls_1_,
                 bmaControls_ch_, iFeature, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bSourceID = bSourceID
        self.bmaControls_0_ = bmaControls_0_
        self.bmaControls_1_ = bmaControls_1_
        self.bmaControls_ch_ = bmaControls_ch_
        self.iFeature = iFeature



class FourByteControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('dCUR', 4), ]


    def __init__(self, dCUR, parent_id = None):
        self.parent_id = parent_id
        self.dCUR = dCUR



class FourByteControlRangeParameterBlock(OrmClassBase):
    fields_sizes = [('wNumSubRanges', 2), ('dMIN__1_', 4), ('dMAX__1_', 4), ('dRES__1_', 4), ('dMIN_n_', 4),
                    ('dMAX_n_', 4), ('dRES_n_', 4), ]


    def __init__(self, wNumSubRanges, dMIN__1_, dMAX__1_, dRES__1_, dMIN_n_, dMAX_n_, dRES_n_, parent_id = None):
        self.parent_id = parent_id
        self.wNumSubRanges = wNumSubRanges
        self.dMIN__1_ = dMIN__1_
        self.dMAX__1_ = dMAX__1_
        self.dRES__1_ = dRES__1_
        self.dMIN_n_ = dMIN_n_
        self.dMAX_n_ = dMAX_n_
        self.dRES_n_ = dRES_n_



class GraphicEqualizerControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('bmBandsPresent', 4), ('bCUR_Lowest_', 1), ('bCUR_Highest_', 1), ]


    def __init__(self, bmBandsPresent, bCUR_Lowest_, bCUR_Highest_, parent_id = None):
        self.parent_id = parent_id
        self.bmBandsPresent = bmBandsPresent
        self.bCUR_Lowest_ = bCUR_Lowest_
        self.bCUR_Highest_ = bCUR_Highest_



class GraphicEqualizerControlRangeParameterBlock(OrmClassBase):
    fields_sizes = [('wNumSubRanges', 2), ('bMIN_1_', 1), ('bMAX_1_', 1), ('bRES_1_', 1), ('bMIN_n_', 1),
                    ('bMAX_n_', 1), ('bRES_n_', 1), ]


    def __init__(self, wNumSubRanges, bMIN_1_, bMAX_1_, bRES_1_, bMIN_n_, bMAX_n_, bRES_n_, parent_id = None):
        self.parent_id = parent_id
        self.wNumSubRanges = wNumSubRanges
        self.bMIN_1_ = bMIN_1_
        self.bMAX_1_ = bMAX_1_
        self.bRES_1_ = bRES_1_
        self.bMIN_n_ = bMIN_n_
        self.bMAX_n_ = bMAX_n_
        self.bRES_n_ = bRES_n_



class HighLowScalingControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('bCUR_Lo', 1), ('bCUR_Hi', 1), ]


    def __init__(self, bCUR_Lo, bCUR_Hi, parent_id = None):
        self.parent_id = parent_id
        self.bCUR_Lo = bCUR_Lo
        self.bCUR_Hi = bCUR_Hi



class HighLowScalingControlRangeParameterBlock(OrmClassBase):
    fields_sizes = [('wNumSubRanges', 2), ('bMIN_1_', 1), ('bMAX_1_', 1), ('bRES_1_', 1), ('bMIN_n_', 1),
                    ('bMAX_n_', 1), ('bRES_n_', 1), ]


    def __init__(self, wNumSubRanges, bMIN_1_, bMAX_1_, bRES_1_, bMIN_n_, bMAX_n_, bRES_n_, parent_id = None):
        self.parent_id = parent_id
        self.wNumSubRanges = wNumSubRanges
        self.bMIN_1_ = bMIN_1_
        self.bMAX_1_ = bMAX_1_
        self.bRES_1_ = bRES_1_
        self.bMIN_n_ = bMIN_n_
        self.bMAX_n_ = bMAX_n_
        self.bRES_n_ = bRES_n_



class InputTerminalDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bTerminalID', 1),
                    ('wTerminalType', 2), ('bAssocTerminal', 1), ('bCSourceID', 1), ('bNrChannels', 1),
                    ('bmChannelConfig', 4), ('iChannelNames', 1), ('bmControls', 2), ('iTerminal', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bTerminalID, wTerminalType, bAssocTerminal,
                 bCSourceID, bNrChannels, bmChannelConfig, iChannelNames, bmControls, iTerminal, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bTerminalID = bTerminalID
        self.wTerminalType = wTerminalType
        self.bAssocTerminal = bAssocTerminal
        self.bCSourceID = bCSourceID
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iTerminal = iTerminal



class LeftGroupClusterDescriptor(OrmClassBase):
    fields_sizes = [('bNrChannels', 1), ('bmChannelConfig', 4), ('iChannelNames', 1), ]


    def __init__(self, bNrChannels, bmChannelConfig, iChannelNames, parent_id = None):
        self.parent_id = parent_id
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames



class MixerUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bNrInPins', 1),
                    ('baSourceID_1_', 1), ('baSourceID__p_', 1), ('bNrChannels', 1), ('bmChannelConfig', 4),
                    ('iChannelNames', 1), ('bmMixerControls', 1), ('bmControls', 1), ('iMixer', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bNrInPins, baSourceID_1_, baSourceID__p_,
                 bNrChannels, bmChannelConfig, iChannelNames, bmMixerControls, bmControls, iMixer, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bNrInPins = bNrInPins
        self.baSourceID_1_ = baSourceID_1_
        self.baSourceID__p_ = baSourceID__p_
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmMixerControls = bmMixerControls
        self.bmControls = bmControls
        self.iMixer = iMixer



class ModulationDelayEffectUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wEffectType', 2), ('bSourceID', 1), ('bmaControls_0_', 4), ('bmaControls_1_', 4),
                    ('bmaControls_ch_', 4), ('iEffects', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wEffectType, bSourceID, bmaControls_0_,
                 bmaControls_1_, bmaControls_ch_, iEffects, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wEffectType = wEffectType
        self.bSourceID = bSourceID
        self.bmaControls_0_ = bmaControls_0_
        self.bmaControls_1_ = bmaControls_1_
        self.bmaControls_ch_ = bmaControls_ch_
        self.iEffects = iEffects



class MpegDecoderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bDecoderID', 1),
                    ('bDecoder', 1), ('bmMPEGCapabilities', 2), ('bmMPEGFeatures', 1), ('bmControls', 1),
                    ('iDecoder', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bDecoderID, bDecoder, bmMPEGCapabilities,
                 bmMPEGFeatures, bmControls, iDecoder, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bDecoderID = bDecoderID
        self.bDecoder = bDecoder
        self.bmMPEGCapabilities = bmMPEGCapabilities
        self.bmMPEGFeatures = bmMPEGFeatures
        self.bmControls = bmControls
        self.iDecoder = iDecoder



class OneByteControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('bCUR', 1), ]


    def __init__(self, bCUR, parent_id = None):
        self.parent_id = parent_id
        self.bCUR = bCUR



class OneByteControlRangeParameterBlock(OrmClassBase):
    fields_sizes = [('wNumSubRanges', 2), ('bMIN_1_', 1), ('bMAX_1_', 1), ('bRES_1_', 1), ('bMIN_n_', 1),
                    ('bMAX_n_', 1), ('bRES_n_', 1), ]


    def __init__(self, wNumSubRanges, bMIN_1_, bMAX_1_, bRES_1_, bMIN_n_, bMAX_n_, bRES_n_, parent_id = None):
        self.parent_id = parent_id
        self.wNumSubRanges = wNumSubRanges
        self.bMIN_1_ = bMIN_1_
        self.bMAX_1_ = bMAX_1_
        self.bRES_1_ = bRES_1_
        self.bMIN_n_ = bMIN_n_
        self.bMAX_n_ = bMAX_n_
        self.bRES_n_ = bRES_n_



class OutputTerminalDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bTerminalID', 1),
                    ('wTerminalType', 2), ('bAssocTerminal', 1), ('bSourceID', 1), ('bCSourceID', 1), ('bmControls', 2),
                    ('iTerminal', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bTerminalID, wTerminalType, bAssocTerminal,
                 bSourceID, bCSourceID, bmControls, iTerminal, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bTerminalID = bTerminalID
        self.wTerminalType = wTerminalType
        self.bAssocTerminal = bAssocTerminal
        self.bSourceID = bSourceID
        self.bCSourceID = bCSourceID
        self.bmControls = bmControls
        self.iTerminal = iTerminal



class ParametricEqualizerSectionEffectUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wEffectType', 2), ('bSourceID', 1), ('bmaControls_0_', 4), ('bmaControls_1_', 4),
                    ('bmaControls_ch_', 4), ('iEffects', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wEffectType, bSourceID, bmaControls_0_,
                 bmaControls_1_, bmaControls_ch_, iEffects, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wEffectType = wEffectType
        self.bSourceID = bSourceID
        self.bmaControls_0_ = bmaControls_0_
        self.bmaControls_1_ = bmaControls_1_
        self.bmaControls_ch_ = bmaControls_ch_
        self.iEffects = iEffects



class ReverberationEffectUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wEffectType', 2), ('bSourceID', 1), ('bmaControls_0_', 4), ('bmaControls_1_', 4),
                    ('bmaControls_ch_', 4), ('iEffects', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wEffectType, bSourceID, bmaControls_0_,
                 bmaControls_1_, bmaControls_ch_, iEffects, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wEffectType = wEffectType
        self.bSourceID = bSourceID
        self.bmaControls_0_ = bmaControls_0_
        self.bmaControls_1_ = bmaControls_1_
        self.bmaControls_ch_ = bmaControls_ch_
        self.iEffects = iEffects



class SamplingRateConverterUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bSourceID', 1),
                    ('bCSourceInID', 1), ('bCSourceOutID', 1), ('iSRC', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bSourceID, bCSourceInID, bCSourceOutID,
                 iSRC, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bSourceID = bSourceID
        self.bCSourceInID = bCSourceInID
        self.bCSourceOutID = bCSourceOutID
        self.iSRC = iSRC



class SelectorUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bNrInPins', 1),
                    ('baSourceID_1_', 1), ('baSourceID__p_', 1), ('bmControls', 1), ('iSelector', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bNrInPins, baSourceID_1_, baSourceID__p_,
                 bmControls, iSelector, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bNrInPins = bNrInPins
        self.baSourceID_1_ = baSourceID_1_
        self.baSourceID__p_ = baSourceID__p_
        self.bmControls = bmControls
        self.iSelector = iSelector



class StandardAcInterfaceDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bInterfaceNumber', 1), ('bAlternateSetting', 1),
                    ('bNumEndpoints', 1), ('bInterfaceClass', 1), ('bInterfaceSubClass', 1), ('bInterfaceProtocol', 1),
                    ('iInterface', 1), ]


    def __init__(self, bLength, bDescriptorType, bInterfaceNumber, bAlternateSetting, bNumEndpoints, bInterfaceClass,
                 bInterfaceSubClass, bInterfaceProtocol, iInterface, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bInterfaceNumber = bInterfaceNumber
        self.bAlternateSetting = bAlternateSetting
        self.bNumEndpoints = bNumEndpoints
        self.bInterfaceClass = bInterfaceClass
        self.bInterfaceSubClass = bInterfaceSubClass
        self.bInterfaceProtocol = bInterfaceProtocol
        self.iInterface = iInterface



class StandardAcInterruptEndpointDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bEndpointAddress', 1), ('bmAttributes', 1),
                    ('wMaxPacketSize', 2), ('bInterval', 1), ]


    def __init__(self, bLength, bDescriptorType, bEndpointAddress, bmAttributes, wMaxPacketSize, bInterval,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bEndpointAddress = bEndpointAddress
        self.bmAttributes = bmAttributes
        self.wMaxPacketSize = wMaxPacketSize
        self.bInterval = bInterval



class StandardAsInterfaceDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bInterfaceNumber', 1), ('bAlternateSetting', 1),
                    ('bNumEndpoints', 1), ('bInterfaceClass', 1), ('bInterfaceSubClass', 1), ('bInterfaceProtocol', 1),
                    ('iInterface', 1), ]


    def __init__(self, bLength, bDescriptorType, bInterfaceNumber, bAlternateSetting, bNumEndpoints, bInterfaceClass,
                 bInterfaceSubClass, bInterfaceProtocol, iInterface, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bInterfaceNumber = bInterfaceNumber
        self.bAlternateSetting = bAlternateSetting
        self.bNumEndpoints = bNumEndpoints
        self.bInterfaceClass = bInterfaceClass
        self.bInterfaceSubClass = bInterfaceSubClass
        self.bInterfaceProtocol = bInterfaceProtocol
        self.iInterface = iInterface



class StandardAsIsochronousAudioDataEndpointDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bEndpointAddress', 1), ('bmAttributes', 1),
                    ('wMaxPacketSize', 2), ('bInterval', 1), ]


    def __init__(self, bLength, bDescriptorType, bEndpointAddress, bmAttributes, wMaxPacketSize, bInterval,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bEndpointAddress = bEndpointAddress
        self.bmAttributes = bmAttributes
        self.wMaxPacketSize = wMaxPacketSize
        self.bInterval = bInterval



class StandardAsIsochronousFeedbackEndpointDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bEndpointAddress', 1), ('bmAttributes', 1),
                    ('wMaxPacketSize', 2), ('bInterval', 1), ]


    def __init__(self, bLength, bDescriptorType, bEndpointAddress, bmAttributes, wMaxPacketSize, bInterval,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bEndpointAddress = bEndpointAddress
        self.bmAttributes = bmAttributes
        self.wMaxPacketSize = wMaxPacketSize
        self.bInterval = bInterval



class StandardInterfaceAssociationDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bFirstInterface', 1), ('bInterfaceCount', 1),
                    ('bFunctionClass', 1), ('bFunctionSubClass', 1), ('bFunctionProtocol', 1), ('iFunction', 1), ]


    def __init__(self, bLength, bDescriptorType, bFirstInterface, bInterfaceCount, bFunctionClass, bFunctionSubClass,
                 bFunctionProtocol, iFunction, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bFirstInterface = bFirstInterface
        self.bInterfaceCount = bInterfaceCount
        self.bFunctionClass = bFunctionClass
        self.bFunctionSubClass = bFunctionSubClass
        self.bFunctionProtocol = bFunctionProtocol
        self.iFunction = iFunction



class StereoExtenderProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('bmChannelConfig', 4),
                    ('iChannelNames', 1), ('bmControls', 2), ('iProcessing', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, bmChannelConfig, iChannelNames, bmControls, iProcessing, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iProcessing = iProcessing



class TwoByteControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('wCUR', 2), ]


    def __init__(self, wCUR, parent_id = None):
        self.parent_id = parent_id
        self.wCUR = wCUR



class TwoByteControlRangeParameterBlock(OrmClassBase):
    fields_sizes = [('wNumSubRanges', 2), ('wMIN_1_', 2), ('wMAX_1_', 2), ('wRES_1_', 2), ('wMIN_n_', 2),
                    ('wMAX_n_', 2), ('wRES_n_', 2), ]


    def __init__(self, wNumSubRanges, wMIN_1_, wMAX_1_, wRES_1_, wMIN_n_, wMAX_n_, wRES_n_, parent_id = None):
        self.parent_id = parent_id
        self.wNumSubRanges = wNumSubRanges
        self.wMIN_1_ = wMIN_1_
        self.wMAX_1_ = wMAX_1_
        self.wRES_1_ = wRES_1_
        self.wMIN_n_ = wMIN_n_
        self.wMAX_n_ = wMAX_n_
        self.wRES_n_ = wRES_n_



class UpDownMixProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('bmChannelConfig', 4),
                    ('iChannelNames', 1), ('bmControls', 2), ('iProcessing', 1), ('bNrModes', 1), ('daModes_1_', 4),
                    ('daModes_m_', 4), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, bmChannelConfig, iChannelNames, bmControls, iProcessing, bNrModes, daModes_1_, daModes_m_,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.bmChannelConfig = bmChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iProcessing = iProcessing
        self.bNrModes = bNrModes
        self.daModes_1_ = daModes_1_
        self.daModes_m_ = daModes_m_



class ValidAlternateSettingsControlCurParameterBlock(OrmClassBase):
    fields_sizes = [('bControlSize', 1), ('bmValidAltSettings', 1), ]


    def __init__(self, bControlSize, bmValidAltSettings, parent_id = None):
        self.parent_id = parent_id
        self.bControlSize = bControlSize
        self.bmValidAltSettings = bmValidAltSettings



class WmaDecoderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bDecoderID', 1),
                    ('bDecoder', 1), ('bmWMAProfile', 2), ('bmControls', 1), ('iDecoder', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bDecoderID, bDecoder, bmWMAProfile, bmControls,
                 iDecoder, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bDecoderID = bDecoderID
        self.bDecoder = bDecoder
        self.bmWMAProfile = bmWMAProfile
        self.bmControls = bmControls
        self.iDecoder = iDecoder
