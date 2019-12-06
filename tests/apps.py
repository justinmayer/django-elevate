import sys

from elevate import apps

from .base import BaseTestCase


class AppConfigTestCase(BaseTestCase):
    def test_ready(self):
        try:
            del sys.modules["elevate.signals"]
        except KeyError:
            pass

        apps.ElevateConfig("elevate", apps).ready()
        self.assertIn("elevate.signals", sys.modules)

    def test_names(self):
        config = apps.ElevateConfig("elevateTest", apps)
        self.assertEqual(apps.ElevateConfig.name, "elevate")
        self.assertEqual(config.name, "elevateTest")
        self.assertEqual(config.verbose_name, "Django Elevate")
