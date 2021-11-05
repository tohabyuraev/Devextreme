import ctypes


liblebedev = ctypes.CDLL('./lebedev/lebedev.dll', winmode=0)

liblebedev.graph_5_11.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_5_11.restype = ctypes.c_float