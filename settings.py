from environs import Env

env = Env()
env.read_env()

POSTGRES_USER = env.str("POSTGRES_USER", "flinbus")
POSTGRES_PASSWORD = env.str("POSTGRES_PASSWORD", "password")
POSTGRES_HOST = env.str("POSTGRES_HOST", "localhost")
POSTGRES_DB = env.str("POSTGRES_DB", "flinbus")
