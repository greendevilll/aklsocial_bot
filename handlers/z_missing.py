from misc.loader import dp
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

@dp.message_handler(state="*")
async def z_missing_command(msg: Message, state: FSMContext):
    await state.finish()
    
    await msg.reply("❌ Неизвестная команда.", reply=False)