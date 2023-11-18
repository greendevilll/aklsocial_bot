from aiogram.dispatcher.filters.state import StatesGroup, State

class StorageText(StatesGroup):
    text = State()
    is_publish = State()