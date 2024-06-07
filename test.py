import docker

from docker.models.resource import Model


if __name__ == '__main__':
    docker = docker.from_env()
    container: Model = docker.containers.get()
    container_state = container.attrs.get('State')

    print()
    # container: Model = docker.containers.get(container_name)
    # container_state = container.attrs.get('State')

    # if container_state["Status"] == 'running':
    #     print("ok")
    # else:
    #     print("not ok")

    # container_state = container.attrs["State"]
    # print(f"{container_state}")
    # print(docker.containers.list())
    # print(docker.containers.get('7c3f7c716a93'))
