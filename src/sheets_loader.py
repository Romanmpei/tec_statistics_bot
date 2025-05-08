import gspread
from oauth2client.service_account import ServiceAccountCredentials
from db import SessionLocal, Statistic, init_db

# Авторизация в Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("config/credentials.json", scope)
client = gspread.authorize(creds)

# ID таблицы
SHEET_ID = "1NWzS3iXDoCa4lGGyVNGz4ri9IjyjQSwEU_FUAHAKInQ"

# Подключение к листу
sheet = client.open_by_key(SHEET_ID).sheet1
data = sheet.get_all_records()

# Инициализация базы
init_db()
db = SessionLocal()

# Загрузка данных
for row in data:
    category = row.get("category")
    year = str(row.get("year"))
    text = row.get("text")

    if not text:  # пропускаем пустые
        continue

    existing = db.query(Statistic).filter_by(category=category, year=year).first()
    if existing:
        existing.text = text
    else:
        db.add(Statistic(category=category, year=year, text=text))

db.commit()
db.close()
print("✅ Данные успешно загружены в базу.")
