from db import SessionLocal, UserAction
from collections import Counter
from tabulate import tabulate

db = SessionLocal()
actions = db.query(UserAction).all()
db.close()

total_actions = len(actions)
unique_users = len(set(a.user_id for a in actions))

categories = Counter(a.category for a in actions if a.action == "select_category")
years = Counter(a.year for a in actions if a.action == "select_year")

print(f"📊 Всего записей: {total_actions}")
print(f"👥 Уникальных пользователей: {unique_users}")

print("\n📈 Популярные категории:")
print(tabulate(categories.items(), headers=["Категория", "Запросов"]))

print("\n📅 Популярные года:")
print(tabulate(years.items(), headers=["Год", "Запросов"]))
