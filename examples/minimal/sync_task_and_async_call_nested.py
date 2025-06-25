import asyncio
import time
from conrun import Runner


def my_task_child(text: str) -> str:
    time.sleep(1)
    return f"[{text}]"


def my_task_parent(text: str) -> str:
    time.sleep(1)
    result = Runner(mode="thread", max_workers=3).run(
        my_task_child,
        [text for _ in range(3)]
    )
    return "".join(result)



async def main():
    result = await Runner(mode="thread", max_workers=3).arun(
        my_task_parent,
        ["message 1", "message 2", "message 3"],
    )
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
