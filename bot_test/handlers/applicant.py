from aiogram import types, Router,F
from kbds import user_kb_reply
from kbds import applicant_kb

app_router = Router()


@app_router.callback_query(F.data == 'ab')
async def app1(callback: types.CallbackQuery):
     await callback.answer()
     await callback.message.edit_text('В РАЗРАБОТКЕ (ДАНЯ - СЕРЕГА)', parse_mode='HTML', reply_markup=user_kb_reply.nas())
     
@app_router.callback_query(F.data == 'SP')
async def startTest(callback: types.CallbackQuery):
	await callback.answer("Скоро будет доступно!", show_alert=True)
