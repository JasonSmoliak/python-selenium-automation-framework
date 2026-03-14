import os
from config.environments import ENVIRONMENTS

ENV = os.getenv("ENV", "dev")

BASE_URL = ENVIRONMENTS.get(ENV)
