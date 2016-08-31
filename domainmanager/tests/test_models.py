from django.test import TestCase

from domainmanager.models import Domain


# models test
class Domain(TestCase):
    def create_domain(self, name="Budapest"):
        return Domain.objects.create(name="Budapest")

    def test_whatever_creation(self):
        w = self.create_domain()
        self.assertTrue(isinstance(w, Domain))
        self.assertEqual(w.__unicode__(), w.name)
