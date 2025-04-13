from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder

Rep = ReplyKeyboardBuilder()
Rep.row(
    types.KeyboardButton(text="🛑Отмена🛑"),
    types.KeyboardButton(text='✨ОТПРАВИТЬ✨ \n ОТЗЫВ✨')
)


def fde():
    but = [
        [types.InlineKeyboardButton(text='ОСТАВИТЬ ОТЗЫВ', callback_data='os'),
        types.InlineKeyboardButton(text='ПОСМОТРЕТЬ ОТЗЫВ', callback_data='look')]
    ]
    keyb2 = types.InlineKeyboardMarkup(inline_keyboard=but)
    return keyb2

def fd3():
    but1 = [
       [types.InlineKeyboardButton(text='МЕНЮ',callback_data='br')]
    ]
    key3 = types.InlineKeyboardMarkup(inline_keyboard=but1)
    return key3




