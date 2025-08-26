import json


class MyCat:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_data(self):
        return self.name, self.age, self.gender


class MyCatEncoder(json.JSONEncoder):
    def default(self, o):
        return {'ClassName': o.__class__.__name__,
                'fields': {
                    'name': o.name,
                    'age': o.age,
                    'gender': o.gender},
                'methods': {
                    'get_name': o.get_data()}
                }


def write_data_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(obj=data, fp=file,
                  cls=MyCatEncoder,
                  ensure_ascii=False, indent=4)
        return True


if __name__ == '__main__':
    cat = MyCat('Мурзик', 4, 'самец')
    cat_json_string = json.dumps(cat, cls=MyCatEncoder, ensure_ascii=False, indent=4)
    print(cat_json_string)
    write_data_json('json_files/new_cat.json', cat)
