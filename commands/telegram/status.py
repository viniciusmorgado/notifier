from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime

from commands.docker.container_status import get_container_status


def get_current_date():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


async def container_status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    container_name = str(context.args[0])
    result = await get_container_status(container_name)

    if result is None:
        await update.message.reply_text("Error: Could not retrieve container status.")
        return

    # Update response based on container status
    if result == "running":
        response = f"🟩 Container {container_name} online - {get_current_date()} - estado: em execução"
    if result == "created":
        response = f"🟥 Container {container_name} offline - {get_current_date()} - estado: criado"
    if result == "restarting":
        response = f"🟨 Container {container_name} offline - {get_current_date()} - estado: reiniciando"
    if result == "exited":
        response = f"🟥 Container {container_name} offline - {get_current_date()} - estado: desligado"
    if result == "paused":
        response = f"🟥 Container {container_name} offline - {get_current_date()} - estado: pausado"
    if result == "dead":
        response = f"🟥 Container {container_name} offline - {get_current_date()} - estado: morto"
    else:
        response = "🟧 Não foi possivel idêntificar o estado do container."

    await update.message.reply_text(response)
