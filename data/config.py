import os

from dotenv import load_dotenv

load_dotenv()

# Заберем токен нашего бота (прописать в файле ".env")
BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

admins = [
    os.getenv("ADMIN_ID"),
]

host = str(os.getenv("PG_HOST"))

PGUSER = str(os.getenv("PG_USER"))

password = str(os.getenv("PG_PASS"))

banned_users = [123456, 12345666]


