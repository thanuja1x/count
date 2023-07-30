from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from pyrogram import Client , filters
import asyncio
import time
import pytz




bot = Client(
    'MY first project',
    api_id=7009965,
    api_hash="06651b174c4f0591deb0ed1e5663c996",
    bot_token="6347727550:AAGaKj1TaI2bcz43RhlpWwURHMV5G2crGOA"
    
)
START_MESSAGE='EXAM COUNT DOWN'

START_BUTTONS=[
    [InlineKeyboardButton('📛COUNT📛',callback_data='COUNT')],
]
@bot.on_message(filters.photo & filters.private)
def photo(bot , message):
     message.reply(message.photo.file_id)
@bot.on_message(filters.regex('menu')) #start
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    bot.send_photo(
        chat_id='-1001764080153',
        photo = 'AgACAgUAAxkBAANXZMasRjBiLFcVXVsUlKGviBozmbAAAly8MRsGYTBWAXE2nryHgxIACAEAAwIAA3gABx4E',
        caption =text,
        reply_markup=reply_markup,
    )

@bot.on_callback_query(group=5)

async def cb_handler(client: bot, query: CallbackQuery):
        user_input_time = 10
        if query.data=="COUNT":
            while user_input_time>0 and user_input_time!=0:
                dt11 = datetime(2023,11,27,00,00,00,000000,tzinfo=ZoneInfo('Asia/Kolkata'))
                dt22 = datetime.now(pytz.timezone('Asia/Kolkata'))
                dt3 = int((dt11 - dt22).total_seconds())
                user_input_time = dt3
                da=user_input_time//(3600*24)
                h=user_input_time%(3600*24)//3600
                m=user_input_time%3600//60
                s=user_input_time%60
                Countdown_TeLe_TiPs='දින {:02d} | පැය {:02d} | මිනිත්තු {:02d} | තත්පර {:02d} යි'.format(da,h,m,s)
                update_text=str(Countdown_TeLe_TiPs)
                td=datetime.now().date() 
                td2=td
                todaydate = f'📅 අද : {td2}'
                tt=datetime.now().strftime("%I:%M %p")
                tt2=tt
                todaytime= f'⏰ වෙලාව : {tt2}'
                t=int(s/6)
                e1='ㅤ▱ㅤ'*t
                e2=(10-t)*'ㅤ▰ㅤ'
                effect=e2+e1
                if s < 7:
                     effect_01='🔴'
                     effect_02='✥'
                elif s < 14:
                     effect_01='◇'
                     effect_02='◆'
                elif s < 21:
                     effect_01='⏱'
                     effect_02='✥'
                elif s < 28:
                     effect_01='🔘'
                     effect_02='❖'
                elif s < 35:
                     effect_01='🥇'
                     effect_02='❖'
                elif s < 42:
                     effect_01='💠'
                     effect_02='✥'
                elif s < 49:
                     effect_01='🇱🇰'
                     effect_02='❆'
                elif s < 54:
                     effect_01='🏆'
                     effect_02='◆'
                elif s <= 60:
                     effect_01='☘️'
                     effect_02='◆'

                reply_markup = InlineKeyboardMarkup([
                     [InlineKeyboardButton('2023 උසස්පෙළ විභහගයට තව',callback_data='effect')],
                     [InlineKeyboardButton(update_text,callback_data="effect")],
                     [InlineKeyboardButton(effect,callback_data='effect')],
                     [InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect')],
                     [InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect')],
                     [InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect')],
                     [InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect')],
                     [InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect')],
                     [InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect')],
                     [InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect'),InlineKeyboardButton(effect_01,callback_data='effect'),InlineKeyboardButton(effect_02,callback_data='effect')],
                     [InlineKeyboardButton(todaydate,callback_data='effect'),InlineKeyboardButton(todaytime,callback_data='effect')],
                     [InlineKeyboardButton('Powered By Science Edu Team ⚡️',url='https://t.me/BioVideoFullSyllubus/9337')],
             
                     ] )
                
                await query.edit_message_reply_markup(
                        reply_markup=reply_markup
                    )
                user_input_time -=10
                
                await asyncio.sleep(10)


bot.run()
