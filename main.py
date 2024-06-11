import os
from typing import Final
from telegram import Update
from telegram.ext import ContextTypes
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

from commands.docker.container_status import get_container_status
from commands.telegram.custom import custom_command
from commands.telegram.help import help_command
from commands.telegram.start import start_command

load_dotenv()

TOKEN: Final = os.getenv('TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME')

async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        container_name = context.args[0]
        # container_name = "sharp_sutherland"
        await get_container_status(update, context, container_name)
    else:
        await update.message.reply_text('Please provide a container name. Usage: /status <container_name>')


def main():
    print('Starting bot... OK')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('status', status_command))

    print('Polling... OK')
    app.run_polling()


if __name__ == '__main__':
    main()
