import ctypes


liblebedev = ctypes.CDLL('./lebedev/liblebedev.dll', winmode=0)

liblebedev.interp.argtypes = [
    ctypes.c_float,
    ctypes.POINTER(ctypes.c_float),
    ctypes.POINTER(ctypes.c_float),
]
liblebedev.interp.restype = ctypes.c_float

liblebedev.graph_3_2.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_2.restype = ctypes.c_float

liblebedev.graph_3_3.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_3.restype = ctypes.c_float

liblebedev.graph_3_4.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_4.restype = ctypes.c_float

liblebedev.graph_3_5.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_5.restype = ctypes.c_float

liblebedev.graph_3_13.argtypes = [
    ctypes.c_float,
]
liblebedev.graph_3_13.restype = ctypes.c_float

liblebedev.graph_3_21.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_21.restype = ctypes.c_float

liblebedev.graph_3_22.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_22.restype = ctypes.c_float

liblebedev.graph_3_25.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_25.restype = ctypes.c_float

liblebedev.graph_3_28.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_28.restype = ctypes.c_float

liblebedev.graph_3_29.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_29.restype = ctypes.c_float

liblebedev.graph_3_32.argtypes = [
    ctypes.c_float,
]
liblebedev.graph_3_32.restype = ctypes.c_float

liblebedev.graph_3_35.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_3_35.restype = ctypes.c_float

liblebedev.graph_4_2.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_2.restype = ctypes.c_float

liblebedev.graph_4_3.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_3.restype = ctypes.c_float

liblebedev.graph_4_5.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_5.restype = ctypes.c_float

liblebedev.graph_4_8.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_8.restype = ctypes.c_float

liblebedev.graph_4_9.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_9.restype = ctypes.c_float

liblebedev.graph_4_10.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_10.restype = ctypes.c_float

liblebedev.graph_4_11.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_11.restype = ctypes.c_float

liblebedev.graph_4_12.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_12.restype = ctypes.c_float

liblebedev.graph_4_13.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_13.restype = ctypes.c_float

liblebedev.graph_4_15.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_15.restype = ctypes.c_float

liblebedev.graph_4_24.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_24.restype = ctypes.c_float

liblebedev.graph_4_27.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_27.restype = ctypes.c_float

liblebedev.graph_4_28.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_28.restype = ctypes.c_float

liblebedev.graph_4_29.argtypes = [
    ctypes.c_float,
]
liblebedev.graph_4_29.restype = ctypes.c_float

liblebedev.graph_4_30.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_30.restype = ctypes.c_float

liblebedev.graph_4_32.argtypes = [
    ctypes.c_float,
]
liblebedev.graph_4_32.restype = ctypes.c_float

liblebedev.graph_4_34.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_34.restype = ctypes.c_float

liblebedev.graph_4_35.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_35.restype = ctypes.c_float

liblebedev.graph_4_36.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_36.restype = ctypes.c_float

liblebedev.graph_4_38.argtypes = [
    ctypes.c_float,
]
liblebedev.graph_4_38.restype = ctypes.c_float


liblebedev.graph_4_40.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_40.restype = ctypes.c_float

liblebedev.graph_4_42.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_42.restype = ctypes.c_float

liblebedev.graph_4_43.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_4_43.restype = ctypes.c_float

liblebedev.graph_5_7.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_5_7.restype = ctypes.c_float

liblebedev.graph_5_8.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_5_8.restype = ctypes.c_float

liblebedev.graph_5_9.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_5_9.restype = ctypes.c_float

liblebedev.graph_5_11.argtypes = [
    ctypes.c_float,
    ctypes.c_float,
]
liblebedev.graph_5_11.restype = ctypes.c_float
