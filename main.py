import handlers
from aiogram import executor
from misc.loader import dp, bot
import logging
import misc.filters as filters


async def on_startup(dp):
    logging.warning("Binding filters...")
    filters.setup(dp)
    logging.warning("Done. Bot is working.")
    print("\n--\nThx for using ATOMSET STUDIO's scripts <3")


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
