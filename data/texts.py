import yaml
from data.config import YAML_FILE

with open(YAML_FILE, 'r', encoding="UTF-8") as f:
    text_dict = yaml.load(f, Loader=yaml.FullLoader)