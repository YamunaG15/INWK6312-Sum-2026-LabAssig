from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("."))

template = env.get_template("template-task4.j2")

data = {
    "interface": {
        "description": "Configured via Jinja",
        "vlan": 20
    }
}

output = template.render(data)

print(output)
