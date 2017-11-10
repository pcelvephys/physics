from time import sleep
import numpy as np
class HPOA:
    def __init__(self, port = '/dev/ttyUSB0', timeout = 0.1):
        import serial
        self.EDFA_serial = serial.Serial(port, timeout=timeout)
        self.SPC = self.SPCmW

    def flush(self):
        self.EDFA_serial.flush()

    def write(self, cmd):
        if not cmd.endswith('\r\n'):
            cmd += '\r\n'
        self.EDFA_serial.write(cmd)

    def readline(self):
        return self.EDFA_serial.readline()

    def readlines(self):
        return self.EDFA_serial.readlines()

    def ask(self, inp):
        #self.flush()
        self.write(inp)
        return self.readlines()

    def RPM(self):
        """reports the power level on the monitoring PDs (in/dBm, out/dBm, in/mW, out/mW)"""
        answer = self.ask("RPM")
        val1 = float(answer[0].split()[1])
        val2 = float(answer[1].split()[1])
        #print("%f\tdBm" % val1)
        #print("%f\tdBm" % val2)
        val1_mW = 10**(val1/10)
        val2_mW = 10**(val2/10)
        #print("%f\tmW" % val1_mW)
        #print("%f\tmW\n" % val2_mW)
        return (val1, val2, val1_mW, val2_mW)

    def RV(self):
        """reports the device power supply voltage"""
        response = self.ask("RV")
        response = float(response[0].split()[1])
        return response

    def RI(self):
        """reports the device information"""
        response = self.ask("RI")
        response = "".join(response)
        return response

    def RIT(self):
        """reports the device internal temperature in deg C"""
        response = self.ask("RIT")
        response = float(response[0].split()[1])
        return response

    def RLC(self):
        """reports the pump amplifiers current in mA"""
        response1 = self.ask("RLC 1")
        response1 = float(response1[0].split()[2])
        sleep(0.1)
        response2 = self.ask("RLC 2")
        response2 = float(response2[0].split()[2])
        return (response1, response2)

    def RA(self):
        """reports the device alarms status"""
        response = self.ask("RA")
        response = response[0].split()[1:]
        return response

    def RCC(self):
        """reports the laser current setting used in current control mode in mA"""
        response1 = self.ask("RCC 2")
        print("R1 >{}<".format(response1))
        response1 = float(response1[0].split()[2])
        sleep(0.1)
        response2 = self.ask("RCC 3")
        print("R2 >{}<".format(response2))
        response2 = float(response2[0].split()[2])
        return (response1, response2)

    def RGC(self):
        """reports the EDFA gain setting used in gain control mode - DOESNT SEEM TO WORK"""
        response = self.ask("RGC")
        return response

    def RPC(self):
        """reports the EDFA output power setting used in output power control mode"""
        response = self.ask("RPC")
        val1 = float(response[0].split()[1])
        val1_mW = 10**(val1/10)
        return (val1, val1_mW)

    def RMODE(self):
        """reports the EDFA operating mode"""
        response = self.ask("RMODE")
        response = response[0].strip().split()[1]
        return response

    def RRS(self):
        """reports the device RS232 Baud rate - DOESNT SEEM TO WORK"""
        response = self.ask("RRS")
        return response

    def SCC(self, laser, current):
        """sets the lasers current consign used in current control mode"""
        str_val_laser = str(laser)
        str_val_current = str(current)
        response = self.ask("SCC " + str_val_laser + " " + str_val_current)
        return response[0].strip()

    def    SGC(self, gain):
        """sets the lasers gain consign used in gain control mode"""
        str_val = str(gain)
        response = self.ask("SGC "+str_val)
        return response[0].strip()

    def    SPCmW(self, power_mW):
        """sets the lasers power (in mW) consign used in power control mode"""
        str_val = str(np.log10(power_mW)*10)
        response = self.ask("SPC "+str_val)
        return response[0].strip()

    def    SPCdBm(self, power_dBm):
        """sets the lasers power (in dBm) consign used in power control mode"""
        str_val = power_dBm
        response = self.ask("SPC "+str_val)
        return response[0].strip()

    def    SMODE(self, mode):
        """sets the lasers mode"""
        str_val = str(mode)
        response = self.ask("SMODE "+str_val)
        return response[0].strip()

    def    SRS(self, rate):
        """sets the lasers RS232 baud rate"""
        str_val = str(rate)
        response = self.ask("SRS "+str_val)
        return response[0].strip()
