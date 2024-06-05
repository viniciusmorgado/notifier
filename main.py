from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

from commands.telegram.custom import custom_command
from commands.telegram.help import help_command
from commands.telegram.start import start_command
from commands.telegram.status import container_status_command

TOKEN: Final = "Your safe token"
BOT_USERNAME: Final = "@your_ser"


def get_current_date():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'status: x' in processed:
        return f'🟥 Container X offline - {get_current_date()}'
    if 'status: y' in processed:
        return f'🟩 Container X online - {get_current_date()}'
    if 'Você está bem?' in processed:
        return 'Everything cool with me! 😎'
    if 'deploy' in processed:
        return 'Deploy - Nova Versão Disponivel! 🚀🚀🚀'
    else:
        return 'Nothing to say'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'user ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


def main():
    print('Starting bot')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('status', container_status_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Error
    app.add_error_handler(error)

    print('Polling')
    app.run_polling(pool_timeout=3)


if __name__ == '__main__':
    main()
