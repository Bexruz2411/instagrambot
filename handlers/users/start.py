from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}!\n Вы можете скинуть мне ссылку на пост в Instagram — через пару секунд эта фотка или видос будут у вас!")
