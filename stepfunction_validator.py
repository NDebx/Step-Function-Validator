from jsonschema import validate
import yaml
import sys
import click

# click is a library to create this whole command line tool
@click.command()
@click.option('-c', default='File', help='Your YAML file/schema')
@click.option('-s', help='Your JSON file/schema')

# c and s are the parameters for the command line arguments that are required
def main(c,s):
    """
    YAML validator for the CLI 
    
    Example: python app.py -c <test.yaml> -s <test.json>
    This will validate a YAML file against the schema you provided in CLI

    Created by Nilesh 
    https://github.com/NileshDebix
    """

    # Load the step_function_yaml_file from the command line that was given as a argument
    step_function_yaml_file = sys.argv[2]
    if not step_function_yaml_file: 
        print("error no json file")

    # Load the json_file from the command line that was given as a argument
    json_file = sys.argv[4]
    if not json_file: 
        print("error no yaml file")

    # Open the json schema and yaml file with a nested "with open"
    with open(step_function_yaml_file, 'r') as step_function_f:
            with open(json_file, 'r') as json_f:
                
                # load the file data into a variable
                step_function_file = step_function_f
                json_schema = json_f

                # insert loaded variables into the validator, this line will validate the file
                validate(instance=yaml.full_load(step_function_file), schema=yaml.full_load(json_schema)) # if 0 message is received in terminal then validation is successful performed

if __name__ == "__main__":
    main()