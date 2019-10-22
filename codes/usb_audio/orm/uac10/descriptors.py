from universal_serial_bus.orm import ModelBuilder, OrmClassBase



def map_db_objects(db_url):
    engine, meta, tables, session = ModelBuilder.get_db_objects(db_url)
    script = ModelBuilder._gen_mapping_strings(db_url, print_out = False)
    exec(script)
    return engine, meta, tables, session



class AssociatedInterfacesDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bInterfaceNr', 1),
                    ('Association_specific', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bInterfaceNr, Association_specific,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bInterfaceNr = bInterfaceNr
        self.Association_specific = Association_specific



class ChorusProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bControlSize', 1), ('bmControls', 1), ('iProcessing', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing



class ClassSpecificAcInterfaceHeaderDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bcdADC', 2),
                    ('wTotalLength', 2), ('bInCollection', 1), ('baInterfaceNr_1_', 1), ('baInterfaceNr_n_', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bcdADC, wTotalLength, bInCollection,
                 baInterfaceNr_1_, baInterfaceNr_n_, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bcdADC = bcdADC
        self.wTotalLength = wTotalLength
        self.bInCollection = bInCollection
        self.baInterfaceNr_1_ = baInterfaceNr_1_
        self.baInterfaceNr_n_ = baInterfaceNr_n_



class ClassSpecificAsInterfaceDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bTerminalLink', 1),
                    ('bDelay', 1), ('wFormatTag', 2), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bTerminalLink, bDelay, wFormatTag,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bTerminalLink = bTerminalLink
        self.bDelay = bDelay
        self.wFormatTag = wFormatTag



class ClassSpecificAsIsochronousAudioDataEndpointDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bmAttributes', 1),
                    ('bLockDelayUnits', 1), ('wLockDelay', 2), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bmAttributes, bLockDelayUnits, wLockDelay,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bmAttributes = bmAttributes
        self.bLockDelayUnits = bLockDelayUnits
        self.wLockDelay = wLockDelay



class CommonPartOfTheProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('baSourceID_1_', 1), ('baSourceID__p_', 1),
                    ('bNrChannels', 1), ('wChannelConfig', 2), ('iChannelNames', 1), ('bControlSize', 1),
                    ('bmControls', 1), ('iProcessing', 1), ('Process_specific', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, baSourceID_1_,
                 baSourceID__p_, bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing,
                 Process_specific, parent_id = None):
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
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing
        self.Process_specific = Process_specific



class DolbyPrologicProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bControlSize', 1), ('bmControls', 1), ('iProcessing', 1), ('bNrModes', 1),
                    ('waModes_1_', 2), ('waModes_m_', 2), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing, bNrModes,
                 waModes_1_, waModes_m_, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing
        self.bNrModes = bNrModes
        self.waModes_1_ = waModes_1_
        self.waModes_m_ = waModes_m_



class DynamicRangeCompressorProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bControlSize', 1), ('bmControls', 1), ('iProcessing', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing



class ExtensionUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wExtensionCode', 2), ('bNrInPins', 1), ('baSourceID_1_', 1), ('baSourceID__p_', 1),
                    ('bNrChannels', 1), ('wChannelConfig', 2), ('iChannelNames', 1), ('bControlSize', 1),
                    ('bmControls', 1), ('iExtension', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wExtensionCode, bNrInPins, baSourceID_1_,
                 baSourceID__p_, bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iExtension,
                 parent_id = None):
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
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iExtension = iExtension



class FeatureUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bSourceID', 1),
                    ('bControlSize', 1), ('bmaControls_0_', 1), ('iFeature', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bSourceID, bControlSize, bmaControls_0_,
                 iFeature, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bSourceID = bSourceID
        self.bControlSize = bControlSize
        self.bmaControls_0_ = bmaControls_0_
        self.iFeature = iFeature



class InputTerminalDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bTerminalID', 1),
                    ('wTerminalType', 2), ('bAssocTerminal', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('iTerminal', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bTerminalID, wTerminalType, bAssocTerminal,
                 bNrChannels, wChannelConfig, iChannelNames, iTerminal, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bTerminalID = bTerminalID
        self.wTerminalType = wTerminalType
        self.bAssocTerminal = bAssocTerminal
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.iTerminal = iTerminal



class MixerUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bNrInPins', 1),
                    ('baSourceID_1_', 1), ('baSourceID__p_', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bmControls', 1), ('iMixer', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bNrInPins, baSourceID_1_, baSourceID__p_,
                 bNrChannels, wChannelConfig, iChannelNames, bmControls, iMixer, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bNrInPins = bNrInPins
        self.baSourceID_1_ = baSourceID_1_
        self.baSourceID__p_ = baSourceID__p_
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bmControls = bmControls
        self.iMixer = iMixer



class OutputTerminalDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bTerminalID', 1),
                    ('wTerminalType', 2), ('bAssocTerminal', 1), ('bSourceID', 1), ('iTerminal', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bTerminalID, wTerminalType, bAssocTerminal,
                 bSourceID, iTerminal, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bTerminalID = bTerminalID
        self.wTerminalType = wTerminalType
        self.bAssocTerminal = bAssocTerminal
        self.bSourceID = bSourceID
        self.iTerminal = iTerminal



class ReverberationProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bControlSize', 1), ('bmControls', 1), ('iProcessing', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing



class SelectorUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1), ('bNrInPins', 1),
                    ('baSourceID_1_', 1), ('baSourceID__p_', 1), ('iSelector', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, bNrInPins, baSourceID_1_, baSourceID__p_,
                 iSelector, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.bNrInPins = bNrInPins
        self.baSourceID_1_ = baSourceID_1_
        self.baSourceID__p_ = baSourceID__p_
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
                    ('wMaxPacketSize', 2), ('bInterval', 1), ('bRefresh', 1), ('bSynchAddress', 1), ]


    def __init__(self, bLength, bDescriptorType, bEndpointAddress, bmAttributes, wMaxPacketSize, bInterval, bRefresh,
                 bSynchAddress, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bEndpointAddress = bEndpointAddress
        self.bmAttributes = bmAttributes
        self.wMaxPacketSize = wMaxPacketSize
        self.bInterval = bInterval
        self.bRefresh = bRefresh
        self.bSynchAddress = bSynchAddress



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
                    ('wMaxPacketSize', 2), ('bInterval', 1), ('bRefresh', 1), ('bSynchAddress', 1), ]


    def __init__(self, bLength, bDescriptorType, bEndpointAddress, bmAttributes, wMaxPacketSize, bInterval, bRefresh,
                 bSynchAddress, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bEndpointAddress = bEndpointAddress
        self.bmAttributes = bmAttributes
        self.wMaxPacketSize = wMaxPacketSize
        self.bInterval = bInterval
        self.bRefresh = bRefresh
        self.bSynchAddress = bSynchAddress



class StandardAsIsochronousSynchEndpointDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bEndpointAddress', 1), ('bmAttributes', 1),
                    ('wMaxPacketSize', 2), ('bInterval', 1), ('bRefresh', 1), ('bSynchAddress', 1), ]


    def __init__(self, bLength, bDescriptorType, bEndpointAddress, bmAttributes, wMaxPacketSize, bInterval, bRefresh,
                 bSynchAddress, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bEndpointAddress = bEndpointAddress
        self.bmAttributes = bmAttributes
        self.wMaxPacketSize = wMaxPacketSize
        self.bInterval = bInterval
        self.bRefresh = bRefresh
        self.bSynchAddress = bSynchAddress



class ThreeDStereoExtenderProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bControlSize', 1), ('bmControls', 1), ('iProcessing', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing



class UpDownMixProcessingUnitDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bUnitID', 1),
                    ('wProcessType', 2), ('bNrInPins', 1), ('bSourceID', 1), ('bNrChannels', 1), ('wChannelConfig', 2),
                    ('iChannelNames', 1), ('bControlSize', 1), ('bmControls', 1), ('iProcessing', 1), ('bNrModes', 1),
                    ('waModes_1_', 2), ('waModes_m_', 2), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bUnitID, wProcessType, bNrInPins, bSourceID,
                 bNrChannels, wChannelConfig, iChannelNames, bControlSize, bmControls, iProcessing, bNrModes,
                 waModes_1_, waModes_m_, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bUnitID = bUnitID
        self.wProcessType = wProcessType
        self.bNrInPins = bNrInPins
        self.bSourceID = bSourceID
        self.bNrChannels = bNrChannels
        self.wChannelConfig = wChannelConfig
        self.iChannelNames = iChannelNames
        self.bControlSize = bControlSize
        self.bmControls = bmControls
        self.iProcessing = iProcessing
        self.bNrModes = bNrModes
        self.waModes_1_ = waModes_1_
        self.waModes_m_ = waModes_m_
