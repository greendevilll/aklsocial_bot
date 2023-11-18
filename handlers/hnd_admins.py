from misc.loader import dp, bot
from aiogram.dispatcher import FSMContext
from misc.filters import IsAdmin
from aiogram.types import *
from data.db import select_random
from os import remove


@dp.message_handler(IsAdmin(), commands=['get_random'], state = "*")
async def get_random(msg: Message, state: FSMContext):
    await state.finish()
    try:
        range_ = int(msg.text.split()[1])
    except IndexError:
        await msg.reply("❌ Не указан размер выборки")
        return
    r = await select_random(range_)
    if not r:
        await msg.reply("❌ Публичных писем не найдено.")
        return
    if len(r) >= 5:
        fp = "temp/buffer.txt"
        with open(fp, 'w', encoding="UTF-8") as f:
            for text in r:
                f.write('\n\n<...>\n'+text)
        await bot.send_document(msg.from_user.id, open(fp, 'rb'))
        await msg.reply(f"🟢 Возвращено {len(r)}шт. текстов.")
        remove(fp)
    else:
        for text in r:
            await msg.reply(f"<code>{text}</code>")
        await msg.reply(f"🟢 Возвращено {len(r)}шт. текстов.")
            