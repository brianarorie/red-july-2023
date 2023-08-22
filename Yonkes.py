import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

num_names = int(input("How many names do you want to generate?: "))
random_string_length = 4  # Adjust this as needed

# Generate and output the specified number of modified names
for i in range(num_names):
    name = input(f"Enter name {i + 1}: ")
    random_suffix = generate_random_string(random_string_length)
    modified_name = name + random_suffix
    print(f"Modified name {i + 1}: {modified_name}")
