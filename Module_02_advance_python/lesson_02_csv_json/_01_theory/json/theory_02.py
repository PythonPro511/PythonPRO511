import json


def write_data_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(obj=data, fp=file, ensure_ascii=False, indent=4)
    return True


def get_json_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(fp=file)
    return data


def make_json_string(data):
    json_string = json.dumps(data, ensure_ascii=False, indent=4)
    return json_string


def convert_json_string(data):
    python_data = json.loads(data)
    return python_data


if __name__ == '__main__':
    emp_data = {
        "Name": "Алиса",
        "Age": 30,
        "Skills": ["Python", "Анализ Данных"]
    }
    write_data_json(filepath='json_files/emp_data.json', data=emp_data)
    emp_json_data = make_json_string(emp_data)
    print(emp_json_data)
    print(type(emp_json_data))
    print()

    emp_data = get_json_data('json_files/emp_data.json')
    print(emp_data)
    print(type(emp_data))
    print(convert_json_string(emp_json_data))
    print(type(convert_json_string(emp_json_data)))
