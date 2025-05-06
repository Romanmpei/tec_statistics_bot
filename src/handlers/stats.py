from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("stats"))
async def cmd_stats(message: types.Message):
    text = (
        "📊 <b>Статистика ТЭК (заглушка)</b>\n\n"
        "<b>Нефть:</b>\n"
        "• Добыча: 520 млн тонн\n"
        "• Экспорт: 250 млн тонн\n\n"
        "<b>Газ:</b>\n"
        "• Добыча: 700 млрд м³\n"
        "• Экспорт: 210 млрд м³"
    )
    await message.answer(text, parse_mode="HTML")
