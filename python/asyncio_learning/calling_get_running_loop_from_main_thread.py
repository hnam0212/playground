import asyncio
import time


async def test_function():
    print("func 1")
    time.sleep(1)
    print("end func 1")

async def test_function_2():
    print("func 2")
    await test_function()
    time.sleep(3)
    
    print("end func 2")

async def main():
    loop = asyncio.get_running_loop()
    loop.create_task(test_function_2())

if __name__ == "__main__":
    asyncio.run(main())
    """
    Work, output:
    func 2
    func 1
    end func 1
    end func 2

    However with this one:
    loop = asyncio.get_running_loop()
    loop.create_task(test_function_2())
    -> raise:
    RuntimeError: no running event loop

    => can only get event loop inside a corountine
    """
    
