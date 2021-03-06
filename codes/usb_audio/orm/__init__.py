import math
from array import array

import universal_serial_bus
from orm.tools import AttrDict
from universal_serial_bus.legacy import *
from universal_serial_bus.orm import OrmClassBase


byte_array_to_bcd = OrmClassBase.byte_array_to_bcd
byte_array_to_int = OrmClassBase.byte_array_to_int
int_to_byte_array = OrmClassBase.int_to_byte_array
hex_to_int = OrmClassBase.hex_to_int
hex_reversed = OrmClassBase.hex_reversed
byte_array_to_float = OrmClassBase.byte_array_to_float
float_to_byte_array = OrmClassBase.float_to_byte_array

LEN_FREQ_BYTES = 4
SAMPLING_FREQ_CONTROL_ID = 1
LEN_MUTE_VALUE = 1
MUTE_CONTROL_ID = 1
LEN_VOLUME_VALUE = 2
VOLUME_CONTROL_ID = 2
AUDIO_CLASS_SPECIFIC_REQUEST_CODE = AttrDict({'REQUEST_CODE_UNDEFINED': 0,
                                              'CUR'                   : 1,
                                              'RANGE'                 : 2,
                                              'MEM'                   : 3})



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
        return [getattr(self.dbo, attr) for attr in self._has_attr_name_like('SourceID') if
                'CSourceID'.lower() not in attr.lower()]


    def _get_attr_by_name(self, attr_name):
        return [getattr(self.dbo, attr) for attr in self._has_attr_name_like(attr_name)]


    def _get_clock_source_id(self):
        return self._get_attr_by_name('CSourceID')


    @property
    def _class_name(self):
        return str(self.dbo.__class__).split('.')[-1][:-2].replace('Descriptor', '')


    @property
    def ClockID(self):
        return self._get_attr_by_name('ClockID')


    @property
    def is_clock(self):
        return len(self.ClockID)


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
            hex_reved = hex_reversed(type_code)
            return self.TERMINAL_TYPES.get(hex_reved, '')


    @property
    def UnitID(self):
        return self._get_attr_by_name('UnitID')


    @property
    def is_unit(self):
        return len(self.UnitID)


    @property
    def id(self):
        if self.is_clock:
            return self.ClockID[0]
        if self.is_terminal:
            return self.TerminalID[0]
        if self.is_unit:
            return self.UnitID[0]


    @property
    def _has_id(self):
        return len(self.ClockID) or len(self.TerminalID) or len(self.UnitID)


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
    def _draw_graph(cls, nodes, source_edges, clock_source_edges, node_size = 2000, node_color = 'blue',
                    node_alpha = 0.5, label_font_size = 16, label_font_family = 'sans-serif', edge_width = 5,
                    edge_color = 'green', edge_alpha = 0.5, edge_arrowstyle = '->', edge_arrowsize = 50,
                    connectionstyle = 'arc3, rad=0.2'):

        import networkx as nx

        G = nx.MultiDiGraph()
        G.add_nodes_from(nodes)
        G.add_edges_from(source_edges)
        G.add_edges_from(clock_source_edges)

        graph_pos = nx.kamada_kawai_layout(G)

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


    @classmethod
    def get_wMaxPacketSize(cls, n_channels = 1, sampling_freq_max = 48000, bytes_per_sample = 4,
                           frame_freq = 1000 * 8, max_packet_bytes = 2 ** 10, max_packets = 3):

        samples_per_frame = math.ceil(sampling_freq_max / frame_freq)
        bytes_per_frame = samples_per_frame * bytes_per_sample * n_channels

        max_frame_bytes = max_packet_bytes * max_packets
        max_channels = int(max_frame_bytes / (samples_per_frame * bytes_per_sample))
        assert bytes_per_frame <= max_frame_bytes, 'Max {} channels.'.format(max_channels)

        wMaxPacketSize = super().get_wMaxPacketSize(bytes_per_frame = bytes_per_frame,
                                                    max_packet_bytes = max_packet_bytes,
                                                    max_packets = max_packets)
        return wMaxPacketSize


    @property
    def uac_version(self):
        return byte_array_to_bcd(self.audio_control_header_descriptors[0][3:5])


    @property
    def audio_control_descriptors(self):
        return [descriptor for descriptor in self.descriptors if
                (descriptor[self.INTERFACE_DESCRIPTOR_CLASS_FIELD_IDX] == self.CLASS_CODE) and (
                        descriptor[self.DESCRIPTOR_TYPE_FIELD_IDX] == self.INTERFACE_DESCRIPTOR_TYPE_CODE) and (
                        descriptor[self.INTERFACE_DESCRIPTOR_SUBCLASS_FIELD_IDX] == self.AUDIO_CONTROL_SUBCLASS_CODE)]


    @property
    def audio_streaming_descriptors(self):
        return [descriptor for descriptor in self.descriptors if
                (descriptor[self.INTERFACE_DESCRIPTOR_CLASS_FIELD_IDX] == self.CLASS_CODE) and (
                        descriptor[self.DESCRIPTOR_TYPE_FIELD_IDX] == self.INTERFACE_DESCRIPTOR_TYPE_CODE) and (
                        descriptor[self.INTERFACE_DESCRIPTOR_SUBCLASS_FIELD_IDX] == self.AUDIO_STREAMING_SUBCLASS_CODE)]


    @property
    def audio_control_header_descriptors(self):
        return [descriptor for descriptor in self.descriptors if
                (descriptor[self.CLASS_SPECIFIC_INTERFACE_TYPE_FIELD_IDX] == self.CLASS_SPECIFIC_INTERFACE_CODE) and (
                        descriptor[
                            self.CLASS_SPECIFIC_INTERFACE_SUBTYPE_FIELD_IDX] == self.AUDIO_CONTROL_HEADER_SUBTYPE_CODE)]


    def draw_topolograph(self, *args, **kwargs):
        Topologen.draw_topolograph(self.descriptors_dbos, *args, **kwargs)


    def _access_control_attributes(self, entity_id = 0, control_id = 0x01,
                                   bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['CUR'],
                                   interface_or_endpoint_id = 0x00, is_interface = True, channel_no = 0x00,
                                   data_or_wLength = 1024, direction = CONTROL_REQUEST.DIRECTION.IN):

        bmRequestType = (direction & CONTROL_REQUEST.DIRECTION.MASK) | (
                CONTROL_REQUEST.TYPE.CLASS & CONTROL_REQUEST.TYPE.MASK) | (
                                (
                                    CONTROL_REQUEST.RECIPIENT.INTERFACE if is_interface else CONTROL_REQUEST.RECIPIENT.ENDPOINT) & CONTROL_REQUEST.RECIPIENT.MASK)

        return self.ctrl_transfer(bmRequestType = bmRequestType,
                                  bRequest = bRequest,
                                  wValue = control_id << 8 | channel_no,
                                  wIndex = entity_id << 8 | interface_or_endpoint_id,
                                  data_or_wLength = data_or_wLength)


    def get_control_attributes(self, entity_id = 0, control_id = 0x01,
                               bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['CUR'],
                               interface_or_endpoint_id = 0x00, is_interface = True, channel_no = 0x00,
                               data_or_wLength = 1024):

        return self._access_control_attributes(entity_id = entity_id,
                                               control_id = control_id,
                                               bRequest = bRequest,
                                               interface_or_endpoint_id = interface_or_endpoint_id,
                                               is_interface = is_interface,
                                               channel_no = channel_no,
                                               data_or_wLength = data_or_wLength,
                                               direction = CONTROL_REQUEST.DIRECTION.IN)


    def set_control_attributes(self, entity_id = 0, control_id = 0x01,
                               bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['CUR'],
                               interface_or_endpoint_id = 0x00, is_interface = True, channel_no = 0x00,
                               data_or_wLength = 1024):

        return self._access_control_attributes(entity_id = entity_id,
                                               control_id = control_id,
                                               bRequest = bRequest,
                                               interface_or_endpoint_id = interface_or_endpoint_id,
                                               is_interface = is_interface,
                                               channel_no = channel_no,
                                               data_or_wLength = data_or_wLength,
                                               direction = CONTROL_REQUEST.DIRECTION.OUT)


    @classmethod
    def _gen_sampling_freq_bytes(cls, freq, length = LEN_FREQ_BYTES):
        return int_to_byte_array(freq, length = length)


    @classmethod
    def _gen_sampling_freqs_range(cls, freqs, length = LEN_FREQ_BYTES):
        freqs = sorted(set(freqs))
        zero_bytes = cls._gen_sampling_freq_bytes(0, length = length)
        range_bytes = int_to_byte_array(len(freqs), length = 2)

        for freq in freqs:
            freq_bytes = cls._gen_sampling_freq_bytes(freq, length = length)
            range_bytes += freq_bytes + freq_bytes + zero_bytes

        return range_bytes


    @classmethod
    def _get_sampling_freqs(cls, range_bytes, length = LEN_FREQ_BYTES):
        count = byte_array_to_int(range_bytes[:2])
        len_min_max_res = length * 3
        return sorted([byte_array_to_int(range_bytes[2 + len_min_max_res * i:2 + len_min_max_res * i + length])
                       for i in range(count)])


    def get_sampling_freqs(self, entity_id, length = LEN_FREQ_BYTES):
        range_bytes = self.get_control_attributes(entity_id = entity_id,
                                                  bRequest = AUDIO_CLASS_SPECIFIC_REQUEST_CODE['RANGE'])
        return self._get_sampling_freqs(range_bytes, length)


    @classmethod
    def get_sampling_freq_from_byte_array(cls, byte_array):
        return byte_array_to_int(byte_array)


    @classmethod
    def get_sampling_freq_from_hex(cls, hex_string):
        return hex_to_int(hex_string)


    def get_sampling_freq(self, entity_id, data_or_wLength = LEN_FREQ_BYTES):
        freq = self.get_control_attributes(entity_id = entity_id, data_or_wLength = data_or_wLength)
        return byte_array_to_int(freq)


    def set_sampling_freq(self, entity_id, freq = 44100, length = LEN_FREQ_BYTES):
        return self.set_control_attributes(entity_id = entity_id,
                                           data_or_wLength = self._gen_sampling_freq_bytes(freq, length))


    @classmethod
    def _volume_bytes_to_db(cls, volume_bytes):
        return byte_array_to_float(volume_bytes, int_bytes = 1, signed = True)


    @classmethod
    def _db_to_volume_bytes(cls, db):
        return float_to_byte_array(db, int_bytes = 1, decimal_bytes = 1, signed = True)


    def get_mute(self, entity_id):
        mute = self.get_control_attributes(entity_id = entity_id, control_id = MUTE_CONTROL_ID,
                                           data_or_wLength = LEN_MUTE_VALUE)
        return mute[0] == 1


    def set_mute(self, entity_id, mute = False):
        return self.set_control_attributes(entity_id = entity_id, control_id = MUTE_CONTROL_ID,
                                           data_or_wLength = array('B', [int(mute)]))


    def get_volume(self, entity_id):
        volume_bytes = self.get_control_attributes(entity_id = entity_id, control_id = VOLUME_CONTROL_ID,
                                                   data_or_wLength = LEN_VOLUME_VALUE)
        return self._volume_bytes_to_db(volume_bytes)


    def set_volume(self, entity_id, volume_db = -60):
        return self.set_control_attributes(entity_id = entity_id, control_id = VOLUME_CONTROL_ID,
                                           data_or_wLength = self._db_to_volume_bytes(volume_db))
