import inspect
import types
from typing import Callable


def swap_code(target: Callable, replacement: Callable) -> None:
    """Swap bytecode in-place so all existing references change behavior."""
    if not isinstance(target, types.FunctionType):
        raise TypeError("target must be a Python function")
    if not isinstance(replacement, types.FunctionType):
        raise TypeError("replacement must be a Python function")

    if target.__code__.co_freevars != replacement.__code__.co_freevars:
        raise ValueError("closure mismatch; free vars must match")

    if inspect.signature(target) != inspect.signature(replacement):
        raise ValueError("signature mismatch; keep args compatible")

    target.__code__ = replacement.__code__
    target.__defaults__ = replacement.__defaults__
    target.__kwdefaults__ = replacement.__kwdefaults__


def cmd(s: str) -> str:
    return s.strip()


alias = cmd


def hotfix(s: str) -> str:
    return s.strip().upper()


def main() -> None:
    swap_code(cmd, hotfix)
    print(alias("  hi  "))


if __name__ == "__main__":
    main()
