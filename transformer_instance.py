from typing import Type, TypeVar

T = TypeVar("T")


class Runner:
    def run(self, s: str) -> str:
        return s.strip()


class LoudRunner(Runner):
    def run(self, s: str) -> str:
        return super().run(s).upper()


def morph_instance(obj: T, new_cls: Type[T]) -> T:
    """Swap an instance's class when the layouts are likely compatible."""
    old_cls = obj.__class__
    if not (issubclass(new_cls, old_cls) or issubclass(old_cls, new_cls)):
        raise TypeError("classes must be related for a safe __class__ swap")
    obj.__class__ = new_cls
    return obj


def main() -> None:
    r = Runner()
    print(r.run("  hi  "))

    morph_instance(r, LoudRunner)
    print(r.run("  hi  "))


if __name__ == "__main__":
    main()
