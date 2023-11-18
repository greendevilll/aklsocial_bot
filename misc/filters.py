from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from data.config import *

class IsAdmin(BoundFilter):
    async def check(self,msg: types.Message):
        return msg.from_user.id in admins
class IsGroup(BoundFilter):
    async def check(self,msg: types.Message):
        return msg.from_user.id != msg.chat.id
    
def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
    print("[+] Filters bound.")