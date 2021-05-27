import os

from dotenv import load_dotenv

load_dotenv()

# Заберем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMIN_ID"),
]

database = str(os.getenv("Database"))

host = str(os.getenv("PG_HOST"))

PGUSER = str(os.getenv("PG_USER"))

password = str(os.getenv("PG_PASS"))

db_user = str(os.getenv("DB_USER"))

banned_users = [123456, 12345666]

POSTGRES_URI = f"postgresql://{PGUSER}:{password}@{host}/{database}"
aiogram_redis = {
    'host': host,
}

redis = {
    'address': (host, 5432),
    'encoding': 'utf8'
}
