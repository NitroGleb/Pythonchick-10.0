import random
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'токен'


# ‘🎲’, ‘🎯’, ‘🏀’, ‘⚽’, ‘🎳’, or ‘🎰’

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['dice'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎲')
    await bot.send_message(message.chat.id, f'значение кубика {data.dice.value}')

@dp.message_handler(commands=['dart'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎯')
    await bot.send_message(message.chat.id, f'значение дартс {data.dice.value}')

@dp.message_handler(commands=['bask'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🏀')
    await bot.send_message(message.chat.id, f'значение баскет {data.dice.value}')

@dp.message_handler(commands=['foot'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='⚽')
    await bot.send_message(message.chat.id, f'значение футбол {data.dice.value}')

@dp.message_handler(commands=['bowl'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎳')
    await bot.send_message(message.chat.id, f'значение боулинг {data.dice.value}')

@dp.message_handler(commands=['slot'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    await bot.send_message(message.chat.id, f'значение слоты {data.dice.value}')
def get_combo_text(dice_value: int):
    """
    Возвращает то, что было на конкретном дайсе-казино
    :param dice_value: значение дайса (число)
    :return: массив строк, содержащий все выпавшие элементы в виде текста

    Альтернативный вариант (ещё раз спасибо t.me/svinerus):
        return [casino[(dice_value - 1) // i % 4]for i in (1, 4, 16)]
    """
    #           0       1         2        3
    values = ["BAR", "виноград", "лимон", "семь"]

    dice_value -= 1
    result = []
    for _ in range(3):
        result.append(values[dice_value % 4])
        dice_value //= 4
    return result

@dp.message_handler(commands=['slot'])
async def roll_dice(message: types.Message):
    data = await bot.send_dice(message.chat.id, emoji='🎰')
    await bot.send_message(message.chat.id, f'значение слоты {get_combo_text(data.dice.value)}')

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)