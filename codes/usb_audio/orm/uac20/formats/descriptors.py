from universal_serial_bus.orm import ModelBuilder, OrmClassBase



def map_db_objects(db_url):
    engine, meta, tables, session = ModelBuilder.get_db_objects(db_url)
    script = ModelBuilder._gen_mapping_strings(db_url, print_out = False)
    exec(script)
    return engine, meta, tables, session



class ExtendedTypeIFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('bSubslotSize', 1), ('bBitResolution', 1), ('bHeaderLength', 1), ('bControlSize', 1),
                    ('bSideBandProtocol', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, bSubslotSize, bBitResolution,
                 bHeaderLength, bControlSize, bSideBandProtocol, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.bSubslotSize = bSubslotSize
        self.bBitResolution = bBitResolution
        self.bHeaderLength = bHeaderLength
        self.bControlSize = bControlSize
        self.bSideBandProtocol = bSideBandProtocol



class ExtendedTypeIiFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('wMaxBitRate', 2), ('wSamplesPerFrame', 2), ('bHeaderLength', 1), ('bSideBandProtocol', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, wMaxBitRate, wSamplesPerFrame,
                 bHeaderLength, bSideBandProtocol, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.wMaxBitRate = wMaxBitRate
        self.wSamplesPerFrame = wSamplesPerFrame
        self.bHeaderLength = bHeaderLength
        self.bSideBandProtocol = bSideBandProtocol



class ExtendedTypeIiiFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('bSubslotSize', 1), ('bBitResolution', 1), ('bHeaderLength', 1), ('bSideBandProtocol', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, bSubslotSize, bBitResolution,
                 bHeaderLength, bSideBandProtocol, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.bSubslotSize = bSubslotSize
        self.bBitResolution = bBitResolution
        self.bHeaderLength = bHeaderLength
        self.bSideBandProtocol = bSideBandProtocol



class HiResPresentationTimestampLayout(OrmClassBase):
    fields_sizes = [('bmFlags', 4), ('qNanoSeconds', 8), ]


    def __init__(self, bmFlags, qNanoSeconds, parent_id = None):
        self.parent_id = parent_id
        self.bmFlags = bmFlags
        self.qNanoSeconds = qNanoSeconds



class TypeIFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('bSubslotSize', 1), ('bBitResolution', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, bSubslotSize, bBitResolution,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.bSubslotSize = bSubslotSize
        self.bBitResolution = bBitResolution



class TypeIiFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('wMaxBitRate', 2), ('wSlotsPerFrame', 2), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, wMaxBitRate, wSlotsPerFrame,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.wMaxBitRate = wMaxBitRate
        self.wSlotsPerFrame = wSlotsPerFrame



class TypeIiiFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1),
                    ('bSubslotSize', 1), ('bBitResolution', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, bSubslotSize, bBitResolution,
                 parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
        self.bSubslotSize = bSubslotSize
        self.bBitResolution = bBitResolution



class TypeIvFormatTypeDescriptor(OrmClassBase):
    fields_sizes = [('bLength', 1), ('bDescriptorType', 1), ('bDescriptorSubtype', 1), ('bFormatType', 1), ]


    def __init__(self, bLength, bDescriptorType, bDescriptorSubtype, bFormatType, parent_id = None):
        self.parent_id = parent_id
        self.bLength = bLength
        self.bDescriptorType = bDescriptorType
        self.bDescriptorSubtype = bDescriptorSubtype
        self.bFormatType = bFormatType
