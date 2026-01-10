import importlib.abc
import importlib.machinery
import sys
from contextlib import contextmanager
from types import ModuleType
from typing import Callable, Dict, Iterator, Set

ModuleFactory = Callable[[ModuleType], None]


class Ghost(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Make specific module names importable without any files on disk."""

    def __init__(self, registry: Dict[str, ModuleFactory]) -> None:
        self._registry = dict(registry)
        self.names: Set[str] = set(self._registry)

    def find_spec(self, fullname: str, path=None, target=None):
        if fullname in self._registry:
            return importlib.machinery.ModuleSpec(fullname, self, origin="ghost")
        return None

    def create_module(self, spec):
        return None  # Default module creation is fine.

    def exec_module(self, module: ModuleType) -> None:
        factory = self._registry.get(module.__name__)
        if factory is None:
            raise ImportError(f"Ghost cannot build module: {module.__name__}")
        factory(module)


@contextmanager
def install_ghost(ghost: Ghost, cleanup: bool = True) -> Iterator[Ghost]:
    before = set(sys.modules)
    sys.meta_path.insert(0, ghost)
    try:
        yield ghost
    finally:
        if ghost in sys.meta_path:
            sys.meta_path.remove(ghost)
        if cleanup:
            for name in ghost.names:
                if name not in before:
                    sys.modules.pop(name, None)


def build_cmd_strip(module: ModuleType) -> None:
    module.__all__ = ["run"]
    module.run = lambda s: s.strip()


def main() -> None:
    ghost = Ghost({"cmd_strip": build_cmd_strip})
    sys.modules.pop("cmd_strip", None)

    with install_ghost(ghost):
        import cmd_strip

        print(cmd_strip.run("  hi  "))


if __name__ == "__main__":
    main()
