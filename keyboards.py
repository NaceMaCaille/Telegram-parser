from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Інформація", callback_data='info')]
    ])

button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Інфо Чернігів/область')]
    ], resize_keyboard=True)

button1 = button
