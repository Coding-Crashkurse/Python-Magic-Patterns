def damage(x):
    return x * 2


def god_mode(x):
    return x * 999


damage.__code__ = god_mode.__code__

print(damage(3))
print(damage.__name__)
