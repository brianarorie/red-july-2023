num_inputs = int(input("How many names do you want to input?: "))
user_inputs = []

# Taking names from the user
for _ in range(num_inputs):
    name = input("Enter a name: ")
    user_inputs.append(name)

# Output the user inputs
print("User inputs:")
for name in user_inputs:
    print(name)
