from os import listdir, path
from .. import exceptions as ex
from json import load

DIR = path.dirname(path.abspath(__file__))


def list_available_templates() -> str :
    all_templates = "Available templates: \n\n"
    all_templates += "\n".join(
        [
            f"> {key.title()}\t" for key in templates.keys()
        ]
        )
    return all_templates

def format_project_structure(template, project_name):
    formatted_structure = {k: [] for k in template.keys()}  
    try:
        for folder in template['folders']:
            formatted_structure['folders'].append(folder.format(project_name))

        for file_path in template['files']:
            formatted_structure['files'].append(file_path.format(project_name))
    except Exception :
        raise ex.NotValidJson()
        
    return formatted_structure

def open_load(file_path):
    with open(path.join(DIR, file_path), "rt") as file:
        data = load(file)

    return data



templates = {
    filename.removesuffix(".json"): open_load(path.join(DIR, filename))  
    for filename in listdir(DIR) 
    if filename.endswith(".json")
}

