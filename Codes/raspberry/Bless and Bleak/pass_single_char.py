import asyncio
from bleak import BleakClient

address = "B8:27:EB:BE:36:81"
CHAR_UUID = "51FF12BB-3ED8-46E5-B4F9-D64E2FEC021B"

async def main():
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")
        
        # Read the characteristic with the given UUID
        model_number = await client.read_gatt_char(CHAR_UUID)
        
        # Print the value read (it could be in bytes, so we decode it to a string)
        print(model_number.decode())  # Decode bytes to string

# Run the asyncio loop
asyncio.run(main())
# loop.run_until_complete(main())