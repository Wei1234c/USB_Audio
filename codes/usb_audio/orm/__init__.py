import universal_serial_bus
from universal_serial_bus.orm import OrmClassBase



class Topologen:
    TERMINAL_TYPES = {'0100': 'USB Undefined',
                      '0101': 'USB streaming',
                      '01FF': 'USB vendor specific',
                      '0200': 'Input Undefined',
                      '0201': 'Microphone',
                      '0202': 'Desktop microphone',
                      '0203': 'Personal microphone',
                      '0204': 'Omni-directional microphone',
                      '0205': 'Microphone array',
                      '0206': 'Processing microphone array',
                      '0300': 'Output Undefined',
                      '0301': 'Speaker',
                      '0302': 'Headphones',
                      '0303': 'Head Mounted Display Audio',
                      '0304': 'Desktop speaker',
                      '0305': 'Room speaker',
                      '0306': 'Communication speaker',
                      '0307': 'Low frequency effects speaker',
                      '0400': 'Bi-directional Undefined',
                      '0401': 'Handset',
                      '0402': 'Headset',
                      '0403': 'Speakerphone, no echo reduction',
                      '0404': 'Echo-suppressing speakerphone',
                      '0405': 'Echo-canceling speakerphone',
                      '0500': 'Telephony Undefined',
                      '0501': 'Phone line',
                      '0502': 'Telephone',
                      '0503': 'Down Line Phone',
                      '0600': 'External Undefined',
                      '0601': 'Analog connector',
                      '0602': 'Digital audio interface',
                      '0603': 'Line connector',
                      '0604': 'Legacy audio connector',
                      '0605': 'S/PDIF interface',
                      '0606': '1394 DA stream',
                      '0607': '1394 DV stream soundtrack',
                      '0608': 'ADAT Lightpipe',
                      '0609': 'TDIF',
                      '060A': 'MADI',
                      '0700': 'Embedded Undefined',
                      '0701': 'Level Calibration Noise Source',
                      '0702': 'Equalization Noise',
                      '0703': 'CD player',
                      '0704': 'DAT',
                      '0705': 'DCC',
                      '0706': 'Compressed Audio Player',
                      '0707': 'Analog Tape',
                      '0708': 'Phonograph',
                      '0709': 'VCR Audio',
                      '070A': 'Video Disc Audio',
                      '070B': 'DVD Audio',
                      '070C': 'TV Tuner Audio',
                      '070D': 'Satellite Receiver Audio',
                      '070E': 'Cable Tuner Audio',
                      '070F': 'DSS Audio',
                      '0710': 'Radio Receiver',
                      '0711': 'Radio Transmitter',
                      '0712': 'Multi-track Recorder',
                      '0713': 'Synthesizer',
                      '0714': 'Piano',
                      '0715': 'Guitar',
                      '0716': 'Drums/Rhythm',
                      '0717': 'Other Musical Instrument'}


    def __init__(self, dbo):
        self.dbo = dbo


    def _has_attr_name_like(self, attr_name):
        return [attr for attr in self.dbo.__dict__.keys() if attr_name.lower() in attr.lower()]


    def _get_source_id(self):
        return [getattr(self.dbo, attr) for attr in self._has_attr_name_like('SourceID')
                if 'CSourceID'.lower() not in attr.lower()]


    def _get_attr_by_name(self, attr_name):
        return [getattr(self.dbo, attr) for attr in self._has_attr_name_like(attr_name)]


    def _get_clock_source_id(self):
        return self._get_attr_by_name('CSourceID')


    @property
    def _class_name(self):
        return str(self.dbo.__class__).split('.')[-1][:-2].replace('Descriptor', '')


    @property
    def TerminalID(self):
        return self._get_attr_by_name('TerminalID')


    @property
    def is_terminal(self):
        return len(self.TerminalID)


    @property
    def TerminalType(self):
        if self.is_terminal:
            type_code = self._get_attr_by_name('TerminalType')[0]
            hex_reversed = OrmClassBase.hex_reversed(type_code)
            return self.TERMINAL_TYPES.get(hex_reversed, '')


    @property
    def UnitID(self):
        return self._get_attr_by_name('UnitID')


    @property
    def is_unit(self):
        return len(self.UnitID)


    @property
    def id(self):
        if self.is_terminal:
            return self.TerminalID[0]
        if self.is_unit:
            return self.UnitID[0]


    @property
    def _has_id(self):
        return len(self.TerminalID) or len(self.UnitID)


    @property
    def SourceID(self):
        return self._get_source_id()


    @property
    def CSourceID(self):
        return self._get_clock_source_id()


    @property
    def _has_source(self):
        return len(self.SourceID) or len(self.CSourceID)


    @property
    def tag(self):
        class_name = '{}: {}'.format(self.id, self._class_name)
        return class_name + ('.{}'.format(self.TerminalType.replace(' ', '_')) if self.is_terminal else '')


    @classmethod
    def _get_graph_elements(cls, db_objects):
        tps = [Topologen(dbo) for dbo in db_objects]
        nodes = set()
        source_edges = []
        clock_source_edges = []

        for tp_to in tps:
            if tp_to._has_id:
                nodes.add(tp_to.tag)

                if tp_to._has_source:
                    for tp_from in tps:
                        if tp_from._has_id:
                            if tp_from.id in tp_to.SourceID:
                                source_edges.append((tp_from.tag, tp_to.tag))
                            if tp_from.id in tp_to.CSourceID:
                                clock_source_edges.append((tp_from.tag, tp_to.tag))

        return nodes, source_edges, clock_source_edges


    @classmethod
    def _draw_graph(cls, nodes, source_edges, clock_source_edges,
                    node_size = 2000, node_color = 'blue', node_alpha = 0.5,
                    label_font_size = 16, label_font_family = 'sans-serif',
                    edge_width = 5, edge_color = 'green', edge_alpha = 0.5,
                    edge_arrowstyle = '->', edge_arrowsize = 50, connectionstyle = 'arc3, rad=0.2'):

        import networkx as nx

        G = nx.MultiDiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(source_edges)
        G.add_edges_from(clock_source_edges)

        graph_pos = nx.kamada_kawai_layout(G)
        # graph_pos = nx.spectral_layout(G)

        nx.draw_networkx_nodes(G, graph_pos, node_size = node_size, node_color = node_color, alpha = node_alpha)
        nx.draw_networkx_labels(G, graph_pos, font_size = label_font_size, font_family = label_font_family)
        nx.draw_networkx_edges(G, graph_pos, edgelist = source_edges, width = edge_width, edge_color = edge_color,
                               alpha = edge_alpha, arrowstyle = edge_arrowstyle, arrowsize = edge_arrowsize)
        nx.draw_networkx_edges(G, graph_pos, edgelist = clock_source_edges, width = edge_width, edge_color = 'red',
                               alpha = edge_alpha, arrowstyle = edge_arrowstyle, arrowsize = edge_arrowsize,
                               connectionstyle = connectionstyle)


    @classmethod
    def draw_topolograph(cls, db_objects, *args, **kwargs):
        nodes, source_edges, clock_source_edges = cls._get_graph_elements(db_objects)
        cls._draw_graph(nodes, source_edges, clock_source_edges, *args, **kwargs)



class UACdevice(universal_serial_bus.USBdevice):
    CLASS_CODE = 0x01
    INTERFACE_DESCRIPTOR_TYPE_CODE = 0x04
    AUDIO_CONTROL_SUBCLASS_CODE = 0x01
    AUDIO_STREAMING_SUBCLASS_CODE = 0x02

    DESCRIPTOR_TYPE_FIELD_IDX = 1
    INTERFACE_DESCRIPTOR_CLASS_FIELD_IDX = 5
    INTERFACE_DESCRIPTOR_SUBCLASS_FIELD_IDX = 6

    CLASS_SPECIFIC_INTERFACE_CODE = 0x24
    AUDIO_CONTROL_HEADER_SUBTYPE_CODE = 0x01
    CLASS_SPECIFIC_INTERFACE_TYPE_FIELD_IDX = 1
    CLASS_SPECIFIC_INTERFACE_SUBTYPE_FIELD_IDX = 2


    @property
    def uac_version(self):
        return OrmClassBase.byte_array_to_bcd(self.audio_control_header_descriptors[0][3:5])


    @property
    def audio_control_descriptors(self):
        return [descriptor for descriptor in self.descriptors
                if (descriptor[self.INTERFACE_DESCRIPTOR_CLASS_FIELD_IDX] == self.CLASS_CODE) and
                (descriptor[self.DESCRIPTOR_TYPE_FIELD_IDX] == self.INTERFACE_DESCRIPTOR_TYPE_CODE) and
                (descriptor[self.INTERFACE_DESCRIPTOR_SUBCLASS_FIELD_IDX] == self.AUDIO_CONTROL_SUBCLASS_CODE)]


    @property
    def audio_streaming_descriptors(self):
        return [descriptor for descriptor in self.descriptors
                if (descriptor[self.INTERFACE_DESCRIPTOR_CLASS_FIELD_IDX] == self.CLASS_CODE) and
                (descriptor[self.DESCRIPTOR_TYPE_FIELD_IDX] == self.INTERFACE_DESCRIPTOR_TYPE_CODE) and
                (descriptor[self.INTERFACE_DESCRIPTOR_SUBCLASS_FIELD_IDX] == self.AUDIO_STREAMING_SUBCLASS_CODE)]


    @property
    def audio_control_header_descriptors(self):
        return [descriptor for descriptor in self.descriptors
                if (descriptor[self.CLASS_SPECIFIC_INTERFACE_TYPE_FIELD_IDX] == self.CLASS_SPECIFIC_INTERFACE_CODE) and
                (descriptor[
                     self.CLASS_SPECIFIC_INTERFACE_SUBTYPE_FIELD_IDX] == self.AUDIO_CONTROL_HEADER_SUBTYPE_CODE)]


    def draw_topolograph(self, *args, **kwargs):
        Topologen.draw_topolograph(self.descriptors_dbos, *args, **kwargs)
