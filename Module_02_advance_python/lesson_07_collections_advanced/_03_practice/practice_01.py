from collections import deque


class TaskQueue:
    def __init__(self, max_length):
        self.queue = deque(maxlen=max_length)

    def add_task(self, task):
        self.queue.append(task)

    def add_important_task(self, task):
        self.queue.appendleft(task)

    def get_tasks(self):
        return list(self.queue)


if __name__ == '__main__':
    tq = TaskQueue(4)
    tq.add_task('task1')
    tq.add_task('task2')
    tq.add_task('task3')
    tq.add_task('task4')
    print(tq.get_tasks())
    tq.add_task('task5')
    print(tq.get_tasks())
    tq.add_important_task('task0')
    print(tq.get_tasks())
