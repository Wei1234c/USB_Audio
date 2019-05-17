from universal_serial_bus.orm import OrmClassBase


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
                  '0307': 'Low frequency effects speaker'}



class Topologen:

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
            return TERMINAL_TYPES.get(hex_reversed, '')
        return None


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
    def is_topologen(self):
        return self._has_id or self._has_source


    @property
    def tag(self):
        class_name = '{}: {}'.format(self.id, self._class_name)
        return class_name + ('.{}'.format(self.TerminalType) if self.is_terminal else '')


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
