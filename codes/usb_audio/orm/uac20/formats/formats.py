from universal_serial_bus.orm import OrmClassBase



class AudioDataFormatTypeIBitAllocation(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, bmformats):
        self.name = name
        self.bmformats = bmformats



class AudioDataFormatTypeIiBitAllocation(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, bmformats):
        self.name = name
        self.bmformats = bmformats



class AudioDataFormatTypeIiiBitAllocation(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, bmformats):
        self.name = name
        self.bmformats = bmformats



class AudioDataFormatTypeIvBitAllocation(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, bmformats):
        self.name = name
        self.bmformats = bmformats



class FormatTypeCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, format_type_code, value):
        self.format_type_code = format_type_code
        self.value = value



class SideBandProtocolCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, protocol_code, value):
        self.protocol_code = protocol_code
        self.value = value
