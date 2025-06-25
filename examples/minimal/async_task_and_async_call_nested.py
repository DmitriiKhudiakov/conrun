import asyncio
from conrun import Runner


async def my_task_child(text: str) -> str:
    await asyncio.sleep(1)
    return f"[{text}]"


async def my_task_parent(text: str) -> str:
    await asyncio.sleep(1)
    result = await Runner(mode="async", max_workers=3).arun(
        my_task_child,
        [text for _ in range(3)]
    )
    return "".join(result)


async def main():
    result = await Runner(mode="async", max_workers=3).arun(
        my_task_parent,
        ["message 1", "message 2", "message 3"],
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
