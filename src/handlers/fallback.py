from aiogram import Router, types

router = Router()

@router.message()
async def unknown_message(message: types.Message):
    await message.answer("Извините, я не понимаю эту команду. Введите /help, чтобы посмотреть список доступных команд.")
