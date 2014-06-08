import xcffib
import struct
import six
_events = {}
_errors = {}
class AxisInfo(xcffib.Struct):
    def __init__(self, parent, offset, size):
        xcffib.Struct.__init__(self, parent, offset, size)
        base = offset
        self.resolution, self.minimum, self.maximum = struct.unpack_from("Iii", parent, offset)
        offset += 12
        self.bufsize = offset - base
class ValuatorInfo(xcffib.Struct):
    def __init__(self, parent, offset, size):
        xcffib.Struct.__init__(self, parent, offset, size)
        base = offset
        self.class_id, self.len, self.axes_len, self.mode, self.motion_size = struct.unpack_from("BBBBI", parent, offset)
        offset += 8
        self.axes = xcffib.List(parent, offset, self.axes_len, AxisInfo, 12)
        offset += self.axes.bufsize
        self.bufsize = offset - base
xcffib._add_ext(xcffib.ExtensionKey("struct"), structExtension, _events, _errors)
