from typing import Callable, Generic, Optional, TypeVar

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")


class Pipe(Generic[T, U]):
    """Wrap a single-argument function so `value | pipe` runs it."""

    def __init__(self, func: Callable[[T], U], name: Optional[str] = None) -> None:
        self.func = func
        self.name = name or getattr(func, "__name__", "pipe")

    def __ror__(self, value: T) -> U:
        return self.func(value)

    def __or__(self, other: "Pipe[U, V]") -> "Pipe[T, V]":
        if not isinstance(other, Pipe):
            return NotImplemented
        return Pipe(lambda x: other.func(self.func(x)), name=f"{self.name}|{other.name}")

    def __call__(self, value: T) -> U:
        return self.func(value)

    def __repr__(self) -> str:
        return f"Pipe({self.name})"


strip = Pipe(str.strip, "strip")
lower = Pipe(str.lower, "lower")


def replace(old: str, new: str) -> Pipe[str, str]:
    return Pipe(lambda s: s.replace(old, new), name=f"replace({old!r},{new!r})")


def main() -> None:
    out = " Error: disk full " | strip | lower | replace(":", " ->")
    print(out)

    combined = strip | lower | replace(":", " ->")
    print(" Error: disk full " | combined)


if __name__ == "__main__":
    main()
