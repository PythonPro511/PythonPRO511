import asyncio


async def process_data(task_id, delay):
    print(f'Задача: {task_id} началась')
    await asyncio.sleep(delay)
    print(f'Задача: {task_id} завершена. Время выполнения: {delay}')
    return f'Результат задачи: {task_id}'


async def monitor_task_progress(task_params):
    tasks = []
    for params in task_params:
        task = asyncio.create_task(process_data(*params))
        tasks.append(task)

    while any(not task.done() for task in tasks):
        # while крутится до тех пор, пока все значения not task.done() не будут равны False
        print(f'Прогресс: некоторые задачи еще выполняются...')
        await asyncio.sleep(2)

    results = [await task for task in tasks]
    print(f'Все задачи завершены!')
    return results


if __name__ == '__main__':
    params_list = [
        (1, 6),
        (2, 4),
        (3, 8),
    ]
    task_results = asyncio.run(monitor_task_progress(params_list))
    print(task_results)
