import builtins
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def shell_prompt(prompt: str = "$ ") -> Iterator[None]:
    """Temporarily prefix all print output with a shell-like prompt."""
    original_print = builtins.print

    def prefixed_print(*args, **kwargs):
        sep = kwargs.get("sep", " ")
        text = sep.join(map(str, args))
        original_print(prompt + text, **kwargs)

    builtins.print = prefixed_print
    try:
        yield
    finally:
        builtins.print = original_print


def main() -> None:
    print("normal")
    with shell_prompt():
        print("cat logs.txt | rg ERROR | head -n 1")
        print("ERROR: disk full")
    print("normal")


if __name__ == "__main__":
    main()
