class Topologen:

    def __init__(self, dbo):
        self.dbo = dbo


    def _has_attr_name_like(self, attr_name):
        for attr in self.dbo.__dict__.keys():
            if attr_name.lower() in attr.lower():
                return attr
        return None


    def _get_source_id(self):
        attr = self._has_attr_name_like('SourceID')
        if attr is not None:
            if 'CSourceID'.lower() not in attr.lower():
                return getattr(self.dbo, attr)


    def _get_attr_by_name(self, attr_name):
        attr = self._has_attr_name_like(attr_name)
        if attr is not None:
            return getattr(self.dbo, attr)


    def _get_clock_source_id(self):
        return self._get_attr_by_name('CSourceID')


    @property
    def class_name(self):
        return str(self.dbo.__class__).split('.')[-1]


    @property
    def TerminalID(self):
        return self._get_attr_by_name('TerminalID')


    @property
    def UnitID(self):
        return self._get_attr_by_name('UnitID')


    @property
    def id(self):
        return self.TerminalID or self.UnitID


    @property
    def has_id(self):
        return self.id


    @property
    def SourceID(self):
        return self._get_source_id()


    @property
    def CSourceID(self):
        return self._get_clock_source_id()


    @property
    def has_source(self):
        return self.SourceID or self.CSourceID


    @property
    def is_topologen(self):
        return self.has_id or self.has_source


    @property
    def tag(self):
        return '{}: {}'.format(self.id, self.class_name)


    @classmethod
    def get_topology_graph_array(cls, db_objects):
        tps = [Topologen(dbo) for dbo in db_objects]
        graph_array = []

        for tp_to in tps:
            if tp_to.has_source:
                for tp_from in tps:
                    if tp_from.has_id:
                        if tp_from.id == tp_to.SourceID or tp_from.id == tp_to.CSourceID:
                            graph_array.append((tp_from.tag, tp_to.tag))
        return graph_array
