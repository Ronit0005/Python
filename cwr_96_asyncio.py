import asyncio
import time
async def function1():
    await asyncio.sleep(3)
    print('Func1')
    return 'ronit'
async def function2():
     await asyncio.sleep(3)
     print("Func2")
async def function3():
     await asyncio.sleep(3)
     print('Func3')
async def main():
     L=await asyncio.gather(function1(),
                            function2(),
                            function3())
     print(L)
asyncio.run(main())