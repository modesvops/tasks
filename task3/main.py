import boto3


class task3:

    session = boto3.Session()

    client = session.client('ecs')

    cluster = client.list_clusters()["clusterArns"]
    for i in cluster:
        services = client.list_services(i)["serviceArns"]
        print(services)
        for j in services:
            tasks = client.list_tasks(cluster=i, serviceName=j)
            print(tasks)
