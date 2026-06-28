import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

BOT_TOKEN = "8996678780:AAHjZKleAKlPofMBTkMnl7nGIveOudQ1Ytk"
YOUR_ID = 680776755
VERONIKA_ID = 696200382

logging.basicConfig(level=logging.INFO)

async def handle_message(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    if not msg or not msg.text:
        return

    sender_id = msg.from_user.id

    if sender_id == VERONIKA_ID:
        await ctx.bot.send_message(
            chat_id=YOUR_ID,
            text=f"✉️ Вероника:\n\n{msg.text}"
        )

    elif sender_id == YOUR_ID:
        await ctx.bot.send_message(
            chat_id=VERONIKA_ID,
            text=msg.text
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
