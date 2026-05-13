from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("template-task3.j2")

data = {
    "interface": {
        "description": "Access Port",
        "vlan": 10
    }
}

output = template.render(data)

print(output)
