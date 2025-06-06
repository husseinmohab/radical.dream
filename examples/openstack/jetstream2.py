from hydraa.services import CaasManager
from hydraa import proxy, JET2, Task, OpenStackVM
# before running this example, make sure you have a valid jetstream2 credential
provider_mgr = proxy([JET2])

# create a list of heterogeneous vms
vms = [OpenStackVM(provider=JET2, launch_type='KVM', flavor_id='m3.xl',
                   image_id='Featured-Ubuntu20', min_count=3, max_count=3),
       OpenStackVM(provider=JET2, launch_type='KVM', flavor_id='m3.2xl',
                   image_id='CentOS', min_count=2, max_count=2),]

# start the Container as a Service manager
caas_mgr = CaasManager(provider_mgr, vms, asynchronous=False)

# create list of tasks
tasks = []
for i in range(1024):
    task = Task()
    task.memory = 7
    task.vcpus  = 1
    task.provider = JET2
    task.image  = "screwdrivercd/noop-container"
    task.cmd    = ['/bin/echo', 'noop']
    tasks.append(task)


# submit 1024 tasks for the manager
caas_mgr.submit(tasks)

# wait for all tasks to complete
all(t.result() for t in tasks)
