def damage(x):
    return x * 2


def god_mode(x):
    return x * 999


damage.__code__ = god_mode.__code__

print(damage(3))      # 2997
print(damage.__name__)  # "damage" bleibt


def banner():
    return "hello-prod"


consts = tuple("hello-staging" if c == "hello-prod" else c for c in banner.__code__.co_consts)
banner.__code__ = banner.__code__.replace(co_consts=consts)

print(banner())  # "hello-staging"
