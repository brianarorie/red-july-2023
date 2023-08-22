import string
import random

N = 5

uni = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
x = int(input('How Many Instance Names Do You Need?: '))
for num in range(x):
    request = input('What Is The Name Of Your Department?: ')
    instance_name = request + uni

    print(f'The Unique Instance Name Is: {instance_name}')