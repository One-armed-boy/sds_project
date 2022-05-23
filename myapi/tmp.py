from pathlib import Path
import os
import json
import sys
BASE_DIR=Path(__file__).resolve().parent.parent
SECRETS_PATH=os.path.join(BASE_DIR,'Secrets.json')
print(BASE_DIR)
print(SECRETS_PATH)
secrets=json.loads(open(SECRETS_PATH).read())
print(secrets)
print(sys.modules[__name__])