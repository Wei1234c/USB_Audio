from universal_serial_bus.orm import ModelBuilder, OrmClassBase



def map_db_objects(db_url):
    engine, meta, tables, session = ModelBuilder.get_db_objects(db_url)
    script = ModelBuilder._gen_mapping_strings(db_url, print_out = False)
    exec(script)
    return engine, meta, tables, session



class BiDirectionalTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description



class EmbeddedTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description



class ExternalTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description



class InputTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description



class OutputTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description



class TelephonyTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description



class UsbTerminalType(OrmClassBase):
    fields_sizes = []


    def __init__(self, terminal_type, code, i_o, description):
        self.terminal_type = terminal_type
        self.code = code
        self.i_o = i_o
        self.description = description
