import os
from unittest import TestCase
from hydraa.services.caas_manager.local_caas import LocalCaas 

class VM:
        def __init__(self):
                self.LaunchType = 'testlaunch'
                self.MinCount = 1
                self.MaxCount = 1
                self.KeyPair = None
                self.FlavorId = 'flavor1'
                self.ImageId = 'image1'
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
                sandbox = 'test_sandbox'

                if not os.path.exists(sandbox):
                        os.mkdir(sandbox)

                manager_id = 'mgr123'
                cred = {'auth_url': 'http://fake', 'username': 'user', 'password': 'pass'}
                VMS = [VM()]
                asynchronous = False
                auto_terminate = False
                log = Logger()
                prof = Profiler
                obj = LocalCaas(sandbox, manager_id, cred, VMS, asynchronous, auto_terminate, log, prof)
                self.assertIsNotNone(obj)
