import builtins
from contextlib import contextmanager


@contextmanager
def curse_print(prefix=" "):
    orig = builtins.print
    def cursed_print(*a, **kw):
        orig(prefix + " ".join(map(str, a)), **kw)
    builtins.print = cursed_print
    try:
        yield
    finally:
        builtins.print = orig


print("normal")
with curse_print():
    print("this looks haunted")
    print("even this")
print("normal again")
