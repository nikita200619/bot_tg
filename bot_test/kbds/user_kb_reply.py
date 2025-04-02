from aiogram.utils.keyboard import  InlineKeyboardBuilder
from aiogram import types
def get_hello():
    buttons = [
        [types.InlineKeyboardButton(text='Отзывы', callback_data='feedback'),
         types.InlineKeyboardButton(text='Новости', callback_data='news') 
        ],
        
        [types.InlineKeyboardButton(text='Общежитие', callback_data='hostel'),
         types.InlineKeyboardButton(text='О нас', callback_data='us')
        ],
        
        [types.InlineKeyboardButton(text='Запись на экзамен', callback_data='exam')],
        
        [types.InlineKeyboardButton(text='Информация о поступлении', callback_data='prv')]
         
        
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard