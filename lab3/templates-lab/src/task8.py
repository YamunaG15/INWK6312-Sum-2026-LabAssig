from jinja2 import Environment, FileSystemLoader
import yaml

# Load Jinja environment
ENV = Environment(loader=FileSystemLoader('.'))

# -----------------------------
# CUSTOM FILTERS
# -----------------------------

# Converts VLAN number into readable format
def vlan_format(vlan_id):
    return f"VLAN {vlan_id}"

# Cleans and formats interface descriptions
def clean_desc(text):
    return text.strip().capitalize()

# Register filters in Jinja
ENV.filters['vlan_format'] = vlan_format
ENV.filters['clean_desc'] = clean_desc

# Load template
template = ENV.get_template("template-task6.j2")

# Load YAML data
with open("data-task7.yml") as f:
    interfaces = yaml.load(f, Loader=yaml.SafeLoader)

# Render output
print(template.render(interface_list=interfaces))
