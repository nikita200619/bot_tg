from aiogram import types, Router
from kbds import user_kb_reply
from aiogram import F
from aiogram.filters import CommandStart

user_router = Router()





@user_router.message(CommandStart())
async def start(message: types.Message):
     await message.delete()
      
     txt = ("<b>Муромский институт\n\n</b>"
           "<b>Филиал Владимирского государственного университета имени Александра и Николая Столетовых.\n\n</b>"
           "<b>Ведущий вуз Поокского региона👨‍🎓👩‍🎓\n</b>")

     await message.answer(txt, parse_mode='HTML', reply_markup=user_kb_reply.get_hello())
    

@user_router.callback_query(F.data == 'br')
async def start1(callback: types.CallbackQuery):
      
      

     txt = ("<b>Муромский институт\n\n</b>"
           "<b>Филиал Владимирского государственного университета имени Александра и Николая Столетовых.\n\n</b>"
           "<b>Ведущий вуз Поокского региона👨‍🎓👩‍🎓\n</b>")

     await callback.message.edit_text(txt, parse_mode='HTML', reply_markup=user_kb_reply.get_hello())
     await callback.answer()

@user_router.callback_query(F.data == 'us')
async def send_random_value(callback: types.CallbackQuery):
     
     txt = ("<b>❇Муромский институт❇\n\n</b>"
           "<b>Филиал Владимирского государственного университета имени Александра и Николая Столетовых.\n\n</b>"
           "<b>Ведущий вуз Поокского региона\n</b>"
           "\n"
           "<b>🎓 4500 студентов\n</b>"
           "<b>🎓 10 современных учебных корпусов\n</b>"
           "<b>🎓 52 учебные и научно-исследовательские лаборатории\n</b>"
           "<b>🎓 5 факультетов\n</b>"
           "<b>🎓 20 направлений бакалавриата\n</b>"
           "<b>🎓 8 направлений магистратуры\n</b>"
           "<b>🎓 Аспирантура и докторантура\n</b>"
           "<b>🎓 Очная, заочная и дистанционная форма обучения\n</b>"
           "<b>🎓 Возможность получения второго высшего образования\n</b>"
           "<b>🎓 Высокий профессиональный уровень преподавателей\n</b>"
           "<b>🎓 Современные практико-ориентированные технологии обучения\n</b>")
     await callback.message.edit_text(txt, parse_mode='HTML', reply_markup=user_kb_reply.nas())
     await callback.answer()
    