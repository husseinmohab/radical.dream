from hydraa.services import CaasManager, ServiceManager
from hydraa import proxy, AWS, Task, AwsVM

provider_mgr = proxy([AWS])

ec2vm = AwsVM(launch_type='EC2', instance_id='t2.micro', min_count=1, max_count=1,
              image_id='ami-0021619f6563c0914', SubnetId='subnet-0a8fc0bf69faadcbe',
              IamInstanceProfile={'Arn': 'arn:aws:iam::946358504676:instance-profile/ecsInstanceRole'})

caas_mgr = CaasManager(provider_mgr, [ec2vm], asynchronous=False)

service_mgr = ServiceManager([caas_mgr])
service_mgr.start_services()

tasks = []
for i in range(10):
    task = Task()
    task.memory = 7
    task.vcpus  = 1
    task.provider = AWS
    task.ecs_launch_type = 'EC2' 
    task.cmd    = ['python3', '-c', 'import math\nprint(math.sin(10))']
    task.ecs_kwargs = {'executionRoleArn': 'arn:aws:iam::946358504676:role/ecsTaskExecutionRole'}
    task.image  = "python:3.9-slim"
    tasks.append(task)


caas_mgr.submit(tasks)
results = [t.result() for t in tasks]
print(f"Results: {results}")
