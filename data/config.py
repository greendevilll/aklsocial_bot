from dotenv import load_dotenv
import os
load_dotenv()

bot_token = os.environ['bot_token']
admins = [int(x) for x in os.environ['admins'].split(',')]
db_fn = os.environ['db_fn']
YAML_FILE = os.environ['yaml']