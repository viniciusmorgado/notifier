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
    # containers = docker_client.containers.list(all=True)

    # container_info = []
    #
    # for container in containers:
    #     status = container.status.split(" ")[0]
    #     container_info.append({
    #         "name": container.name,
    #         "status": status
    #     })

    # return container_info
