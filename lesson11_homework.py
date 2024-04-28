class Human:
    HUMAN: dict()

    def __init__(self, name, age):
        self.HUMAN = {name: age}


    def add_human(self, human = dict()):
        self.HUMAN.update(human)

    def get_human(self):
        return self.HUMAN


a1 = Human('Oleg', 23)

a2 = Human('Masha', 13)

a3 = Human('Katya', 39)



a1.add_human(a3.get_human())
a1.add_human(a2.get_human())

d1 = a1.get_human()
print(d1)


def import_yaml(name, d):
    import yaml

    with open(f'{str(name)}.yaml', 'w') as file:
        doc = yaml.dump(d, file)

def open_yaml(name_file):
    import yaml
    with open(f'{str(name_file)}') as file:
        con = yaml.load(file, Loader=yaml.FullLoader)
        return con

print(open_yaml('proverka.yaml'))
import_yaml('proverka', d1)

def import_json(name, basa):
    import json
    json_object = json.dumps(basa, indent=1)
    with open(f'{str(name)}.json', 'w') as file:
        file.write(json_object)

def open_json(name_file):
    import json
    with open(f'{str(name_file)}', 'r') as opfile:
        json_object = json.load(opfile)
        return json_object

import_json('proverka', d1)

print(open_json('proverka.json'))
