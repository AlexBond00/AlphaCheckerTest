"""MVP json parser."""
import os


def parse_json(python_json_dict: dict):
    """Replaces all '$'-variables with env variables."""
    for key, variable in python_json_dict.items():
        if not isinstance(variable, (dict, list)):
            if variable.startswith("$"):
                python_json_dict[key] = os.getenv(variable[1:])
        elif isinstance(variable, list):
            continue
        else:
            parse_json(variable)
    return python_json_dict
