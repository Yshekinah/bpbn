from django.test import TestCase

from domainmanager.models import *


# models test
class DomainTest(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        pass
        # Test definitions as before call_setup_methods()

    def test_domain(self):
        # A test that uses the fixtures.
        domain = Domain.objects.get(name="Budapest")
        self.assertEqual(str(domain), 'Budapest')
