num_names = int(input('how many name do you want?: '))

for i in range(num_names):
    name = input(f'enter name {i + 1}: ')
print(f'unique name {i + 1}}: {name}')