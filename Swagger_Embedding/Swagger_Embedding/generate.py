import yaml
from jinja2 import Template

def generate_api(yaml_file):
    with open(yaml_file, 'r') as f:
        spec = yaml.safe_load(f)

    template_str = open('server_template.h.j2').read()
    template = Template(template_str)

    # Output the C++ Header
    with open('main/generated_api.h', 'w') as f:
        f.write(template.render(paths=spec['paths']))

    print("Success: Generated main/generated_api.h")

if __name__ == "__main__":
    generate_api('openapi.yaml')