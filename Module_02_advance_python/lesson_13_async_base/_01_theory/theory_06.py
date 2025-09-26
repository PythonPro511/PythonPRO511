import asyncio


async def fetch_data(task_id, delay):
    print(f'Task: {task_id} started')
    await asyncio.sleep(delay)  # Имитация запроса к API
    print(f'Task: {task_id} finished')
    return f'Data from task {task_id}'


async def main():
    tasks = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    ]
    task_list = []
    task_results = []

    for task in tasks:
        t = asyncio.create_task(task)
        task_list.append(t)

    for task in task_list:
        await task
        task_results.append(task.result())

    print(task_results)


if __name__ == '__main__':
    asyncio.run(main())
