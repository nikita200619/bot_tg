from aiogram import types

def get_hello():
    buttons = [
        [types.InlineKeyboardButton(text='Студент🧑‍🎓', callback_data='s'),
         types.InlineKeyboardButton(text='Абитуриент👩‍🎓', callback_data='ab') 
        ],
        [types.InlineKeyboardButton(text='О нас', callback_data='us')],
        [types.InlineKeyboardButton(text='ОТЗЫВЫ📒', callback_data='fb')],
        ]
    
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard




def nas():
    buttons2 = [
         [types.InlineKeyboardButton(text="САЙТ", url='https://www.mivlgu.ru/',callback_data='st'),
         types.InlineKeyboardButton(text="ВК",   url='https://vk.com/mivlgu',callback_data='vk')
        ],
        [types.InlineKeyboardButton(text='🔄НАЗАД🔄',callback_data='br')]
    ]
    
    keyb1 = types.InlineKeyboardMarkup(inline_keyboard=buttons2)
    return keyb1


