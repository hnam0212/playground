from tasks import add

result = add.delay(4,6)

result_value = result.get(timeout=10)
print('Task result:', result_value)