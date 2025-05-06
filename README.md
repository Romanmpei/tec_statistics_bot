# 📊 tec_statistics_bot — Telegram-бот статистики ТЭК

**Разработчик:** Roman MPEI  
**Описание:**  
Бот предоставляет пользователю статистические данные по различным направлениям Топливно-энергетического комплекса (ТЭК) России за 2021–2024 гг.

## 📂 Основной функционал

- Выбор категории ТЭК: электроэнергетика, теплоснабжение, нефть, газ, уголь
- Выбор года
- Вывод статистических данных
- Удобное меню с кнопками
- Хранение данных в SQLite (через SQLAlchemy)

## 🚀 Быстрый запуск (Docker)

```bash
git clone <repo-url>
cd tec_statistics_bot
cp .env.example .env  # Указать токен Telegram-бота
docker compose up --build -d```

## 🧱 Стек технологий
Python 3.11+

aiogram 3

SQLite + SQLAlchemy

Docker + docker-compose

VPS (Ubuntu 22.04)

## 🗂 Структура проекта
tec_statistics_bot/
├── src/
│   ├── bot.py
│   ├── db.py
│   ├── handlers/
│   │   ├── menu.py
│   │   └── ...
│   └── statistics.db
├── config/
│   └── config.py
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md

## 🔄 План доработок
📥 Интеграция с Google Sheets или PostgreSQL

📈 Учёт пользователей и действий

🌐 Добавление веб-интерфейса

🧩 Расширение тем (вторичные показатели, ЕИСС)

⏱ Автоматизация обновлений

## 📬 Контакты
Telegram: @intodex
Email: mail@tointodex.ru
Website: https://intodex.ru
