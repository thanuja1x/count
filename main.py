from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery 
from pyrogram import Client , filters
import asyncio
import time
import pytz
from backports.zoneinfo import ZoneInfo

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

@bot.on_message(filters.regex('menu')) #start
def start(bot, message):
    text = START_MESSAGE
    reply_markup = InlineKeyboardMarkup(START_BUTTONS)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_callback_query()
async def cb_handler(client: bot, query: CallbackQuery):
        if query.data=="COUNT":
            dt1 = datetime(2023,11,27,00,00,00,000000,tzinfo=ZoneInfo('Asia/Kolkata'))
            dt2 = datetime.now(pytz.timezone('Asia/Kolkata'))
            dt3 = int((dt1 - dt2).total_seconds())
            user_input_time = dt3
            while user_input_time>0 and user_input_time!=0:
                da=user_input_time//(3600*24)
                h=user_input_time%(3600*24)//3600
                m=user_input_time%3600//60
                s=user_input_time%60
                Countdown_TeLe_TiPs='දින {:02d} | පැය {:02d} | මිනිත්තු {:02d} | තත්පර {:02d} යි'.format(da,h,m,s)
                update_text=str(Countdown_TeLe_TiPs)
                   
                t=int(s/2)
                e1='□'*t
                e2=(30-t)*'■'
                effect=e2+e1
                if s < 10:
                     effect_01='🔴'
                     effect_02='⚪️'
                elif s < 20:
                     effect_01='♻️'
                     effect_02='💠'
                elif s < 30:
                     effect_01='⏰'
                     effect_02='⏱'
                elif s < 40:
                     effect_01='🔵'
                     effect_02='🟢'
                elif s < 50:
                     effect_01='🕒'
                     effect_02='🕘'
                elif s <= 60:
                     effect_01='🟡'
                     effect_02='🔶'

                reply_markup = InlineKeyboardMarkup([
                     [InlineKeyboardButton('2023 උසස්පෙළ විභහගයට තව',callback_data='s')],
                     [InlineKeyboardButton(update_text,callback_data="COUNT")],
                     [InlineKeyboardButton(effect,'effect')],
                     [InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect')],
                     [InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect')],
                     [InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect')],
                     [InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect')],
                     [InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect')],
                     [InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect'),InlineKeyboardButton(effect_02,'effect'),InlineKeyboardButton(effect_01,'effect')],
                     
                     [InlineKeyboardButton('Powered By Science Edu Team ⚡️',url='https://t.me/BioVideoFullSyllubus/9337')],
             
                     ] )
                await query.edit_message_reply_markup(
                        reply_markup=reply_markup
                    )
                user_input_time -=10
                
                await asyncio.sleep(10)


bot.run()