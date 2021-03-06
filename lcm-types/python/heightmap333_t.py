"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class heightmap333_t(object):
    __slots__ = ["map"]

    __typenames__ = ["float"]

    __dimensions__ = [[300, 300]]

    def __init__(self):
        self.map = [ [ 0.0 for dim1 in range(300) ] for dim0 in range(300) ]

    def encode(self):
        buf = BytesIO()
        buf.write(heightmap333_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        for i0 in range(300):
            buf.write(struct.pack('>300f', *self.map[i0][:300]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != heightmap333_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return heightmap333_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = heightmap333_t()
        self.map = []
        for i0 in range(300):
            self.map.append(struct.unpack('>300f', buf.read(1200)))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if heightmap333_t in parents: return 0
        tmphash = (0x2efdeed0a0439083) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if heightmap333_t._packed_fingerprint is None:
            heightmap333_t._packed_fingerprint = struct.pack(">Q", heightmap333_t._get_hash_recursive([]))
        return heightmap333_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

