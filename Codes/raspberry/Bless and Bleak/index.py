import asyncio
from bleak import BleakClient

address = "B8:27:EB:BE:36:81"
CHAR_UUID = "51FF12BB-3ED8-46E5-B4F9-D64E2FEC021B"

async def main():
    async with BleakClient(address) as client:
        if not client.is_connected:
            print("Failed to connect")
            return
        
        print(f"Connected: {client.is_connected}")
        
        try:
            while True:
                value = await client.read_gatt_char(CHAR_UUID)
                print("Value:", value.decode(errors="ignore"))  # or value.hex() if it's not a string
                await asyncio.sleep(1)  # Wait 1 second before next read
        except asyncio.CancelledError:
            print("Reading loop cancelled.")
        except Exception as e:                                                                                                                                                 
            print("Error:", e)

# Run the asyncio loop
asyncio.run(main())
