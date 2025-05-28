import os
from unittest import TestCase
from hydraa.services.caas_manager.local_caas import LocalCaas 

class VM:
        def __init__(self):
                self.LaunchType = ''
                self.MinCount = 1
                self.MaxCount = 1
                self.KeyPair = None
                self.FlavorId = ''
                self.ImageId = ''
                self.Network = None
                self.UserData = ''

class Logger:
        def trace(self, msg):
                pass

class Profiler:
        def __init__(self, name, path):
                pass
        def prof(self, *args, **kwargs):
                pass

class LocalCaaSTestClass(TestCase):
        def test_init(self):
                # self.sandbox  = '{0}/{1}.{2}'.format(sandbox, JET2, self.run_id)
                # os.mkdir(self.sandbox, 0o777), expects a string
                sandbox = 'test_sandbox'

                # avoiding the parent constructor failing to make "test_sandbox/jetstream2.<uuid>" due to the abscence of test_sandbox
                if not os.path.exists(sandbox):
                        os.mkdir(sandbox)

                manager_id = 'mgr123' # most likely a string

                # self.client = self.create_op_client(cred)
                # def create_op_client(self, cred):
                # jet2_client = openstack.connect(**cred)
                # return jet2_client

                # passed to create_op_client which calls openstack.connect(**cred) which expects keyword arguments
                cred = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}

                # self.launch_type = VMS[0].LaunchType.lower()
                # self.vms = VMS       
                # list of objects
                VMS = [VM()] # object has .LaunchType, .MinCount, .MaxCount, .KeyPair, .FlavorId, .ImageId, .Network, .UserData

                # self.asynchronous = asynchronous
                # self.auto_terminate = auto_terminate
                # bool values
                asynchronous = False
                auto_terminate = False

                # self.logger = log
                # self.logger.trace()
                # so log is an object with method trace
                log = Logger()

                # self.profiler = prof(name=__name__, path=self.sandbox)
                # self.profiler.prof(...)
                # prof is a class that returns an object with a .prof() method
                prof = Profiler

                obj = LocalCaas(sandbox, manager_id, cred, VMS, asynchronous, auto_terminate, log, prof)
                self.assertIsNotNone(obj)
