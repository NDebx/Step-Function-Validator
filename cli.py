import yaml
def load_doc():
    with open('./step_function.yml', 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exception:
            raise exception

## Now, validating the yaml file is straightforward:
from cerberus import Validator
schema = eval(open('./test.json', 'r').read())
v = Validator(schema)
doc = load_doc()
print(v.validate(doc, schema))
print(v.errors)