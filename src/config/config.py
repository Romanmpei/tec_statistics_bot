from pathlib import Path
import os
from dotenv import load_dotenv

# Задаём правильный путь к файлу .env
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(dotenv_path=BASE_DIR.parent / '.env')

BOT_TOKEN = os.getenv("BOT_TOKEN")
