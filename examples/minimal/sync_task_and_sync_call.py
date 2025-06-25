import asyncio
import time
from conrun import Runner


def my_task(text: str) -> str:
    time.sleep(1)
    return text.upper()


async def main():
    result = await Runner(mode="thread", max_workers=3).arun(
        my_task,
        ["message 1", "message 2", "message 3"],
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
