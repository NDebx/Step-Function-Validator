from jsonschema import validate
import yaml
import sys
import click

@click.command()
@click.option('-c', default='File', help='Your YAML file/schema')
@click.option('-s', help='Your JSON file/schema')

def main(c,s):
    """YAML validator for the CLI 
    
    Example: python app.py -c <test.yaml> -s <test.json>
    This will validate a YAML file against the schema you provided in CLI

    Created by Nilesh 
    https://github.com/NileshDebix
    """
    yaml_file = sys.argv[2]
    if not yaml_file: 
        print("error no json file")
    json_file = sys.argv[4]
    if not json_file: 
        print("error no yaml file")

    yaml_schema = open(yaml_file, "r")
    json_schema = open(json_file, "r")

    validate(instance=yaml.full_load(json_schema.read()), schema=yaml.full_load(yaml_schema.read())) # passes

if __name__ == "__main__":

    main()