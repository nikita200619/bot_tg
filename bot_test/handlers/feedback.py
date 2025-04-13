from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqdb.datebase_fback import FEED
from kbds import feedback_kb

datebase = FEED()
fd_router = Router()

class Feed(StatesGroup):
    name = State()
    mark = State()
    message_ot = State()
    true = State()



# Выбор оставить отзыв или посмотреть 

@fd_router.callback_query(F.data == 'fb')
async def fd0(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('🌟Сделайте свой выбор: \n Оставить отзыв  |  Посмотреть🌟',reply_markup = feedback_kb.fde())


# Оставить ОТЗЫВ
@fd_router.callback_query(F.data == 'os')
async def fd1(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.edit_text("Напиши свое ФИО👨‍🏫\n(Можно Анонимно)")
    await state.set_state(Feed.name)


@fd_router.message(Feed.name)
async def fd2(message: types.Message, state: FSMContext):
    if message.text is not None   and message.text.isdigit() is False:
        await state.update_data(name=message.text)
        await message.delete()
        await message.answer("Оцените наш институт от 1 до 5 ⭐⭐⭐")
        await state.set_state(Feed.mark)
    else:
        await message.delete()
        await message.answer("Пожалуйста, введите свое ФИО или псевдоним.\n🛑🛑🛑")
   

@fd_router.message(Feed.mark)
async def fd3(message: types.Message, state: FSMContext):
    if message.text.isdigit() and 1 <= int(message.text) <= 5:
        await state.update_data(mark=message.text)
        await message.delete()
        await message.answer("Напишите отзыв📜(не более 50 символов)")
        await state.set_state(Feed.message_ot)
    else:
        await message.delete()
        await message.answer("Пожалуйста, введите число от 1 до 5!\n🛑🛑🛑")


@fd_router.message(Feed.message_ot)
async def fd4(message: types.Message, state: FSMContext):
    if len(message.text) <= 50:
        await state.update_data(message_ot=message.text)
        await message.delete()
        data = await state.get_data()
        name = data.get("name", "Анонимно")
        mark = data.get("mark")
        feedback = data.get("message_ot")
        await state.set_state(Feed.true)
        sml = ['😒','😐','🙂','😃', '😊']
        response = (
        f"✳ВАШ ОТЗЫВ ✳\n\n"
        f"ФИО: {name}\n"
        f"Оценка: {mark} {(sml[(int(mark)-1)])}\n"
        f"Отзыв: {feedback}\n"
        "Варианты действий с отзывом:\n✨Подтвердить публикацию отзыва✨ \n🚫Отменить и удалить отзыв🚫")
        
        await message.answer(response,reply_markup = feedback_kb.Rep.as_markup(resize_keyboard=True))
    else:
        await message.delete()
        await message.answer("Пожалуйста, введите не более 50 символов!\n🛑🛑🛑")
       
    
@fd_router.message(Feed.true)
async def fd5(message: types.Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name", "Анонимно")
    mark = data.get("mark")
    feedback = data.get("message_ot")
    
    if message.text == '✨ОТПРАВИТЬ✨ \n ОТЗЫВ✨':
        await message.delete()
        datebase.fd(feedback, name, mark)
        
        sml = ['😒','😐','🙂','😃', '😊']
        response = (
        f"✳ СПАСИБО БОЛЬШОЕ ЗА ОТЗЫВ ✳\n\n"
        f"ФИО: {name}\n"
        f"Оценка: {mark} {(sml[(int(mark)-1)])}\n"
        f"Отзыв: {feedback}\n"
        "МЕНЮ --> /start")
        await message.answer(response, reply_markup=types.ReplyKeyboardRemove())
 
        await state.clear()
        
    elif message.text == '🛑Отмена🛑':
        await message.delete()
        await message.answer('✨Отзыв отменен и удален.✨ \n\n"МЕНЮ --> /start"', reply_markup=types.ReplyKeyboardRemove())
        await state.clear()
    else:
        await message.delete()
        await message.answer("Варианты действий с отзывом:\n✨Подтвердить публикацию отзыва✨ \n🚫Отменить и удалить отзыв🚫")

# ПОСМОТРЕТЬ ОТЗЫВ

@fd_router.callback_query(F.data == 'look')
async def get1(callback: types.CallbackQuery):
    await callback.answer()
    await callback.message.edit_text('В РАЗРАБОТКЕ (НИКИТА) -> /start', parse_mode='HTML')