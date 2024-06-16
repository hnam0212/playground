import asyncio
import time


async def test_function():
    print("func 1")
    time.sleep(3)
    print("end func 1")

async def test_function_2():
    print("func 2")
    time.sleep(1)
    print("end func 2")

async def main():
    await asyncio.gather(test_function(), test_function_2())

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    print(f"exec time {time.time() - start_time}")

    ## exec time : 4.003
    ## It work as well but we don't actually achieve asynchronously running coroutine 