#!/usr/bin/python
class itr90:
    def __init__(self, address='/dev/ttyS0'):
        self.address = address
        import serial
        self.connection = serial.Serial(self.address)

    def raw(self, bytes=100):
        self.connection.flushInput()
        S = self.connection.read(bytes)
        #print(S)
        return S

    def numbers(self):
        raw = self.raw()
        raw = raw[raw.index(b'\x07\x05'):]
        raw = raw[:9]
        return [int(b) for b in raw]

    def pressure(self):
        nums = self.numbers()
        hb = float(nums[4])
        lb = float(nums[5])
        return 10**((hb*256+lb)/4000-12.5)
