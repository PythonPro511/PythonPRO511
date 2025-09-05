def count_tasks(task_tree):
    if not task_tree.get("subtasks"):
        return 1
    return 1 + sum(count_tasks(subtask) for subtask in task_tree['subtasks'])
    pass


if __name__ == '__main__':
    my_task_tree = {
        "name": "Main Task",
        "subtasks": [
            {"name": "Subtask 1", "subtasks": []},
            {"name": "Subtask 2", "subtasks": [
                {"name": "Sub-subtask 1", "subtasks": []},
                {"name": "Sub-subtask 2", "subtasks": []}
            ]}
        ]
    }
    print(count_tasks(my_task_tree))
