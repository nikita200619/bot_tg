from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import Text
from kbds import user_kb_reply
user_router = Router()


@user_router.message()
async def start(message:types.Message):
    URL='https://avatars.mds.yandex.net/i?id=fcb1d761a8fa0f2893588e63a748fd270dd90e60-9151021-images-thumbs&n=13'
   
    txt = (
    
    "         🎓 Муромский институт 🎓          \n\n"
    
    
    
    "<b>Основные факты:</b>"
    "•<b>4500 студентов</b>\n"
    "• <b>10 учебных корпусов</b>\n"
    "• <b>52 лаборатории</b>\n"
    "• <b>5 факультетов</b>\n"
    "• <b>20 направлений бакалавриата</b>\n"
    "• <b>8 направлений магистратуры</b>\n"
    "• Аспирантура и докторантура\n"
    "• Очное, заочное и дистанционное обучение\n"
    "• Второе высшее образование\n"
    "• Сильный преподавательский состав\n"
    "• Современные технологии обучение\n"
    )
    
    
    await message.answer_photo(photo=URL,caption=txt,parse_mode='HTML',reply_markup=user_kb_reply.get_hello())
    
