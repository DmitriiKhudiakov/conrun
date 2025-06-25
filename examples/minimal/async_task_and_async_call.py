import asyncio
from conrun import Runner


async def my_task(text: str) -> str:
    await asyncio.sleep(1)
    return text.upper()


def main():
    result = Runner(mode="async", max_workers=3).run(
        my_task,
        ["message 1", "message 2", "message 3"],
    )
    print(result)


if __name__ == "__main__":
    main()