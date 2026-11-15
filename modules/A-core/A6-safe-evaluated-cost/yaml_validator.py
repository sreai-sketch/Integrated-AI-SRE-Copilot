import yaml
def validate_yaml(text):
    value=yaml.safe_load(text)
    if not isinstance(value,dict): raise ValueError("Expected YAML object")
    return value
