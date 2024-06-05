import docker


def get_container_status(container_name: str, docker_client=None):
    if docker_client is None:
        docker_client = docker.from_env()
    try:
        container = docker_client.containers.get(container_name)
        status = container.status.split(" ")[0]
        return status

    except FileNotFoundError:
        return None
