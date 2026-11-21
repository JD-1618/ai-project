import asyncio
#1. Define an async function (like sending a lab sample)
async def call_ai_agent(task_name):
    print(f"starting {task_name}...")
    await asyncio.sleep(1) # simulates waiting 1 sec for an ai API
    return f"{task_name} done!"
#2.Run two AI calls at the exact same time
async def main():
    results = await asyncio.gather(
        call_ai_agent("fetch latest labtest reports"),
        call_ai_agent("check current symptoms of patient"),
        call_ai_agent("check past h/o any disease")
    )
    print(results)

asyncio.run(main())
