from db import Statistic, SessionLocal, init_db

init_db()
session = SessionLocal()

# Ввод данных
category = input("Категория (например, ⚡ Электроэнергетика): ").strip()
year = input("Год (например, 2024): ").strip()

print("Вводите текст статистики (для завершения нажмите Enter на пустой строке):")
lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)
text = "\n".join(lines)

# Проверка существующей записи
existing = session.query(Statistic).filter_by(category=category, year=year).first()

if existing:
    print(f"\n🔄 Запись для '{category}' {year} уже существует.")
    choice = input("Хотите перезаписать? (y/n): ").strip().lower()
    if choice == "y":
        existing.text = text
        session.commit()
        print("✅ Обновлено!")
    else:
        print("❌ Отмена.")
else:
    new_entry = Statistic(category=category, year=year, text=text)
    session.add(new_entry)
    session.commit()
    print("✅ Новая запись добавлена!")

session.close()
