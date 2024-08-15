
REGISTRY = {}

def register(**kwargs):
    print("decorator")
    def decorator(fn):
        key = frozenset(kwargs)
        REGISTRY[key] = fn
        return fn
    return decorator

def get_registered_item(**kwargs):
    key = frozenset(kwargs)
    return REGISTRY.get(key)

