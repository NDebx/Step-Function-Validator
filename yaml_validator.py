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
    """
    json_file = sys.argv[2]
    if not json_file: 
        print("error no json file")
    yaml_file = sys.argv[4]
    if not yaml_file: 
        print("error no yaml file")

    json_schema = open(json_file, "r")
    yaml_schema = open(yaml_file, "r")

    validate(yaml.full_load(yaml_schema.read()), yaml.safe_load(json_schema.read())) # passes

if __name__ == "__main__":

    main()