from db import Statistic, SessionLocal, init_db

init_db()

session = SessionLocal()

# Добавляем примеры
data = [
    Statistic(category="⚡ Электроэнергетика", year="2024", text="🔌 Выработка: 1150 млрд кВт⋅ч\n📈 Рост: +2,3%"),
    Statistic(category="⚡ Электроэнергетика", year="2023", text="🔌 Выработка: 1124 млрд кВт⋅ч\n📉 Снижение: −1,1%"),
    Statistic(category="🔥 Теплоснабжение", year="2023", text="♨️ Подача тепла: 1560 млн Гкал\n📈 Рост: +0,9%"),
]

session.add_all(data)
session.commit()
session.close()
