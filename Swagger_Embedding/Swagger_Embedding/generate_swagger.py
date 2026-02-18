import os
import gzip
import shutil
import subprocess
import yaml
from jinja2 import Template

def build_swagger():
    # 1. Bundle the YAML into a single HTML file (Self-contained)
    # This uses Redoc or Swagger UI Dist
    subprocess.run(["npx", "@redocly/cli", "build-docs", "openapi.yaml", "-o", "web/index.html"])

    # 2. Gzip the output for the ESP32
    with open("web/index.html", "rb") as f_in:
        with gzip.open("web/index.html.gz", "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    print("Swagger UI bundled and gzipped for ESP32.")

def generate_api(yaml_file):
    with open(yaml_file, 'r') as f:
        spec = yaml.safe_load(f)

    template_str = open('server_template.h.j2').read()
    template = Template(template_str)
    
    os.makedirs('gen', exist_ok=True)
    # Output the C++ Header
    with open('gen/generated_api.h', 'w') as f:
        f.write(template.render(paths=spec['paths']))

    print("Success: Generated generated_api.h")

if __name__ == "__main__":
    build_swagger()
    generate_api('openapi.yaml')