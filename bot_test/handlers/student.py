from aiogram import types, Router, F
from kbds import user_kb_reply

student_router = Router()


@student_router.callback_query(F.data == 's')
async def student1(callback: types.CallbackQuery):
     await callback.answer()
     await callback.message.edit_text('В РАЗРАБОТКЕ (Кирилл)', parse_mode='HTML', reply_markup=user_kb_reply.nas())