from decorator import register


@register(index=1, concrete_type=1)
def concrete1(num):
    return num + 1

def test_func():
    print("abc")
