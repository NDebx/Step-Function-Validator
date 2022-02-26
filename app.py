from jsonschema import validate
import yaml

yaml_schema = open("test.yaml", "r")
json_schema = open("test.json", "r")


validate(yaml.full_load(json_schema.read()), yaml.full_load(yaml_schema.read())) # passes
