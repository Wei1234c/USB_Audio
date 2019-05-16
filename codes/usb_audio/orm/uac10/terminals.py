from universal_serial_bus.orm import OrmClassBase



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
