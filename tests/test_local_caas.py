from unittest import TestCase
from hydraa.services.caas_manager.local_caas import LocalCaas 

class LocalCaaSTestClass(TestCase):

        def test_init(self):
                local_caas = LocalCaas()
                self.assertIsNotNone(local_caas)


