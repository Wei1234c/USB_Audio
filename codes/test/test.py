from universal_serial_bus.orm.usb20 import *
from array import array

desp = array('B', [18, 1, 16, 1, 0, 0, 0, 8, 63, 27, 8, 32, 0, 1, 1, 2, 0, 1])
dev_dscrpt = StandardDeviceDescriptor.from_byte_array(desp)
print(dev_dscrpt)