# Python Dark Arts: 5 tricks that look like illegal code

Small, self-contained demos of import hooks, attribute chaining, and runtime mutation.
For education and demos only; do not use in production.

phantom_import.py <- pattern that hijacks the import system to conjure modules that do not exist on disk.
infinite_attribute_chain.py <- pattern that builds infinite attribute chains using `__getattr__` and `__call__`.
soul_swap.py <- pattern that hot-swaps a function's `__code__` and even its bytecode constants.
transformer_instance.py <- pattern that mutates an instance into a different class via `__class__`.
cursed_builtins.py <- pattern that temporarily overrides `builtins.print` to alter output globally.

Run any file directly, for example: `python infinite_attribute_chain.py`.
