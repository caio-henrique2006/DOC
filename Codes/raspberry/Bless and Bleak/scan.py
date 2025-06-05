import asyncio
from bleak import BleakScanner

async def main():
    scan = BleakScanner()
    devices = await scan.discover()
    
    for device in devices:
        print("Device:", {device.name}, "Address:", {device.address})


asyncio.run(main())