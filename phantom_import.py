import sys
import importlib.abc
import importlib.machinery
from types import ModuleType


class GhostImporter(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path=None, target=None):
        if fullname.startswith("api_"):
            return importlib.machinery.ModuleSpec(fullname, self)
        return None

    def create_module(self, spec):
        return ModuleType(spec.name)

    def exec_module(self, module):
        endpoint = module.__name__[4:]  # "api_users" -> "users"

        def get():
            return f" fetching /{endpoint} (but there is no file)"

        module.get = get
        print(f" conjured module: {module.__name__}")


sys.meta_path.insert(0, GhostImporter())

import api_users
print(api_users.get())
