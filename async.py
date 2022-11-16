import aiohttp
from aiohttp import ClientSession
import asyncio
import argparse
import emoji
from codetiming import Timer

async def check_connection(work_queue):

    async with ClientSession() as session:
        while not work_queue.empty():
            url = await work_queue.get()
            timer = Timer(text=f"Site {url} elapsed time: {{:.1f}}")
            timer.start()
            async with session.get(url) as response:
                await response.text()
            timer.stop()



async def main():
    myparser  = argparse.ArgumentParser(description = 'Site connectivity checker')
    myparser.add_argument('-c','--check', type = str , help = 'Checks the site connectivity status', nargs= '*')
    args = myparser.parse_args()
    urls = args.check
    work_queue = asyncio.Queue()
    for url in urls:
        await work_queue.put(url)
    with Timer(text="\nTotal elapsed time: {:.1f}"):
        await asyncio.gather(
            asyncio.create_task(check_connection(work_queue)),asyncio.create_task(check_connection(work_queue))
        )
        

if __name__=='__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())