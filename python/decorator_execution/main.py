from concrete import test_func
from decorator import REGISTRY, get_registered_item

a = get_registered_item(concrete_type=1, index=1)
print(REGISTRY)


"""
At the time we import test_func the deocrator executed event though we do not import decorated function

"""