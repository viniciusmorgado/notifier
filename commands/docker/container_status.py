import docker
from docker import DockerClient
from docker.models.resource import Model
from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime


def get_current_date():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


async def get_container_status(update: Update, context: ContextTypes.DEFAULT_TYPE, container_name: str):
    docker_client: DockerClient = docker.from_env()

    # container_name = context.args[0]
    container: Model = docker_client.containers.get(container_name)
    container_state = container.attrs.get('State')

    if container_state == 'running':
        await update.message.reply_text(f'🟩 Container {container_name} online, status:{container_state["Status"]} '
                                        f'- {get_current_date()}')

    if container_state == 'restarting':
        await update.message.reply_text(f'🟨 Container {container_name} reiniciando, status:{container_state["Status"]}'
                                        f'- {get_current_date()}')

    if (container_state == 'created' or container_state == 'exited' or
            container_state == 'paused' or container_state == 'Dead'):
        await update.message.reply_text(f'🟥 Container {container_name} offline, status:{container_state["Status"]} '
                                        f'- {get_current_date()}')
