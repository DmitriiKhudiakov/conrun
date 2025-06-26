import asyncio
from conrun import Runner


async def child_function(text: str) -> str:
    await asyncio.sleep(1)


async def parent_unction(text: str) -> str:
    await asyncio.sleep(1)
    return text.upper()


async def main():
    result = await Runner(mode="async", max_workers=3).arun(
        my_function,
        ["a", "b", "c"],
    )
    print(result)  # ['A', 'B', 'C']


if __name__ == "__main__":
    asyncio.run(main())