import ctypes


libinterp = ctypes.CDLL('./interp.so', winmode=0)

libinterp.testInterp1d.argtypes = [ctypes.c_void_p]
libinterp.testInterp1d.restype = ctypes.c_int

libinterp.testInterp2d.argtypes = [ctypes.c_void_p]
libinterp.testInterp2d.restype = ctypes.c_int

print(libinterp.testInterp1d(None))
print(libinterp.testInterp2d(None))