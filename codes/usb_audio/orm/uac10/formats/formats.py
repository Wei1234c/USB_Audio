from universal_serial_bus.orm import ModelBuilder, OrmClassBase



def map_db_objects(db_url):
    engine, meta, tables, session = ModelBuilder.get_db_objects(db_url)
    script = ModelBuilder._gen_mapping_strings(db_url, print_out = False)
    exec(script)
    return engine, meta, tables, session



class Ac3ControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value



class AudioDataFormatTypeICode(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, wformattag):
        self.name = name
        self.wformattag = wformattag



class AudioDataFormatTypeIiCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, wformattag):
        self.name = name
        self.wformattag = wformattag



class AudioDataFormatTypeIiiCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, name, wformattag):
        self.name = name
        self.wformattag = wformattag



class FormatTypeCode(OrmClassBase):
    fields_sizes = []


    def __init__(self, format_type_code, value):
        self.format_type_code = format_type_code
        self.value = value



class MpegControlSelector(OrmClassBase):
    fields_sizes = []


    def __init__(self, control_selector, value):
        self.control_selector = control_selector
        self.value = value
