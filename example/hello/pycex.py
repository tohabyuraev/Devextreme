import ctypes


hellolib = ctypes.CDLL('./hellolib.so')

hellolib.sayHello.argtypes = (
    ctypes.c_int,
)
hellolib.sayHello.restype = \
    ctypes.c_void_p