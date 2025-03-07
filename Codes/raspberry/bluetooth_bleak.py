import asyncio
from bleak import BleakScanner, BleakClient

class DeviceBle():
        def __init__(self):
                self.client = None
                self.uuid_battery_service = '0000180f-0000-1000-8000-00805f9b34fb'
                self.uuid_battery_char = '00002a19-0000-1000-8000-00805f9b34fb'

        async def discover(self):
                device_searched = input("Digite o nome do dispositivo que você quer conectar? ")
                devices = await BleakScanner.discover(5.0, return_adv=True)
                for device in devices:
                        advertisement_data = devices[device][1]
                        if(advertisement_data.local_name == device_searched):
                        #if(advertisement_data.rssi > -90):
                                #self.device = devices[device]
                                return device
        async def connect(self):
                address = await self.discover()
                if address is not None:
                        try:
                                print("Found device at address: %s" % (address))
                                print("Attempting to connect...")
                                self.client = BleakClient(address)
                                await self.client.connect()
                                print("Connected")
                        except:
                                raise Exception("Failed to connect")
                else:
                        raise Exception("Did not find available devices")
        async def disconnect(self):
                try:
                        print("Disconnecting...")
                        await self.client.disconnect()
                        print("Disconnected!")
                except:
                        raise Exception("Warning: Failed to disconnect. Check for hanging>")      
        
        async def read_char(self, uuid):
                try:
                        print(uuid)
                        await self.client.read_gatt_char(uuid)
                except:
                        raise Exception("Failed to read characteristic")
        async def read_battery_level(self):
                battery_level = await self.read_char(self.uuid_battery_char)
                return int.from_bytes(battery_level);