import os
from typing import Final
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

from commands.docker.container_status import get_container_status
from commands.telegram.custom import custom_command
from commands.telegram.help import help_command
from commands.telegram.start import start_command

load_dotenv()

TOKEN: Final = os.getenv('TOKEN')
BOT_USERNAME: Final = os.getenv('BOT_USERNAME')


def main():
    print('Starting bot... OK')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('status', get_container_status))

    print('Polling... OK')
    app.run_polling()


if __name__ == '__main__':
    main()
