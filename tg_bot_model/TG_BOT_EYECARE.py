"""
BI_ML - Telegram Bot for eye_care.
Project team members:
     - Yulia P
     - Anton Zhelonkin
     - Dmitriy Podgalo
     - Artyom
     - Leonid Zhozhikov
"""
import logging
import random
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text
from aiogram.types import ParseMode
from config import TOKEN
from model_pred import ml_for_eye_care  # ml_for_eye_care

# enable logging
logging.basicConfig(
    filename='eye_care_logger.log',
    filemode='a',  # appendn?
    format=u'%(filename)s [ LINE:%(lineno)+3s ]'u'#%(levelname)+8s [%(asctime)s]  %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG
)

# global objects
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
logger = logging.getLogger()


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет, офтальмолог!\nДавай попробуем предсказать ретинопатию у твоего диабетника.'
                        'Тыкай /help для того, чтобы узнать как.')
    logger.info('start typed')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text('Отправь фото ДЗН пациента и жди, '
               'как только, так сразу появится результат в этом чате.')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
    logger.info('help typed')


@dp.message_handler(content_types=['photo'])
async def process_document_message(msg: types.Message):
    # # download image

    img_name = '../data/photo/' + str(random.randint(1, 999)) + '.png'
    await msg.photo[-1].download(img_name)
    await msg.reply('Second, plase wait...')
    
    answer = ml_for_eye_care(img_name) 

    if answer == 0:  # например
        await msg.reply('No diabetic retinopathy')
    elif answer == 1:
        await msg.reply('Mild diabetic retinopathy')
    elif answer == 2:
        await msg.reply('Moderate  diabetic retinopathy')
    elif answer == 3:
        await msg.reply('Severe diabetic retinopathy')
    elif answer == 4:
        await msg.reply('Proliferative diabetic retinopathy')
    else:
        await msg.reply('Что-то пошло не так!')
    logger.info('END')


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text('Отправь фото глазного дна \nили нажми еще раз /help.')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
    logger.info('unknown thing sent instead of a document')


if __name__ == '__main__':
    # start bot
    executor.start_polling(dp)
