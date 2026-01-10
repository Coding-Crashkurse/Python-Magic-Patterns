class Spell:
    def __init__(self, path=()):
        self._path = path

    def __getattr__(self, name):
        return Spell(self._path + (name,))

    def __call__(self, *args, **kwargs):
        return f" invoked {'.'.join(self._path)} args={args} kwargs={kwargs}"


api = Spell()

print(api.users.list(limit=3))
print(api.billing.invoices.get("INV-7"))
print(api.what.ever.you.want(1, 2, x=3))
