import os 
import sys

lib_path = os.path.abspath('./modules/RFID_lib/') 
sys.path.append(lib_path)

from py532lib.i2c import *
from py532lib.frame import *
from py532lib.constants import *

class Reader:
    def __init__(self,active=True):
        self.RFID_sensor = Pn532_i2c()
        self.RFID_sensor.SAMconfigure()
        self.tagname = None
        self.active = active
        self.new_RFID = None

    def scan(self):
        while self.active:
            card_data = list(self.RFID_sensor.read_mifare().get_data())
            self.new_RFID = card_data[-4:]
    
    # def sim_scan(self):
    #     if self.active:






# if __name__ == "__main__":
#     reader = Reader()
#     print(reader.scan())
#     print("end of scan")