from environs import Env

env = Env()
env.read_env()

POSTGRES_USER = env.str("POSTGRES_USER", "flinbus")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", "password")
POSTGRES_HOST = env.str("POSTGRES_HOST", "localhost")
POSTGRES_DB = env.str("POSTGRES_DB", "flinbus")

FLINBUSMERGE_URL = env.str("FLINBUSMERGE_URL", "http://localhost:8080")
FLINBUSMERGE_HOST_ADDRESS = env.str("FLINBUSMERGE_HOST_ADDRESS", "0.0.0.0:8080")

FLINBUSML_URL = env.str("FLINBUSML_URL", "http://localhost:8081")
