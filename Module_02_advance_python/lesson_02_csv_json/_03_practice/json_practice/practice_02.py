import json
from collections import defaultdict


def generate_report(json_file_path):
    report = defaultdict(int)

    with open(json_file_path, 'r', encoding='utf-8') as file:
        tasks = json.load(file)
        for task in tasks:
            if task['status'] == 'completed':
                report[task['assignee']] += 1

    return dict(report)


if __name__ == '__main__':
    my_report = generate_report('files/emp_tasks.json')
    print(my_report)