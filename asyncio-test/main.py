import asyncio
from modules.Lamp import Lamp

async def ultra_sensor(lamp):
    print("Reading ultrasonic sensor every 1 second...")

    i = 0
    while True:
        i = i + 1
        print(f"Reading ultrasonic sensor {i}")
        if (i % 2) == 0:
            lamp.turnOn()
        await asyncio.sleep(1)

async def temperature_sensor(lamp):
    print("Reading temperature sensor every 1 seconds...")
    i = 0
    while True:
        i = i + 1
        print(f"Reading temperature sensor {i}")
        if (i % 3) == 0:
            lamp.turnOff()
        await asyncio.sleep(1)

async def main():
    lamp = Lamp(False)

    print(f"Hello, I'm learning to use asyncio.")
    ultra_task = asyncio.create_task(ultra_sensor(lamp))
    temperature_task = asyncio.create_task(temperature_sensor(lamp))

    await asyncio.wait([ultra_task, temperature_task], return_when=asyncio.FIRST_COMPLETED)

asyncio.run(main())