"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class footsteps(object):
    __slots__ = ["xpos", "ypos", "zpos"]

    __typenames__ = ["float", "float", "float"]

    __dimensions__ = [[4], [4], [4]]

    def __init__(self):
        self.xpos = [ 0.0 for dim0 in range(4) ]
        self.ypos = [ 0.0 for dim0 in range(4) ]
        self.zpos = [ 0.0 for dim0 in range(4) ]

    def encode(self):
        buf = BytesIO()
        buf.write(footsteps._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack('>4f', *self.xpos[:4]))
        buf.write(struct.pack('>4f', *self.ypos[:4]))
        buf.write(struct.pack('>4f', *self.zpos[:4]))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != footsteps._get_packed_fingerprint():
            raise ValueError("Decode error")
        return footsteps._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = footsteps()
        self.xpos = struct.unpack('>4f', buf.read(16))
        self.ypos = struct.unpack('>4f', buf.read(16))
        self.zpos = struct.unpack('>4f', buf.read(16))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if footsteps in parents: return 0
        tmphash = (0x5a1eaf779d25ac7a) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if footsteps._packed_fingerprint is None:
            footsteps._packed_fingerprint = struct.pack(">Q", footsteps._get_hash_recursive([]))
        return footsteps._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

