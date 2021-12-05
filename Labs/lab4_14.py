user_text = input()
num_letters = 0

for item in user_text:
    if item not in ['.', ',', ' ']:
        num_letters += 1
print(num_letters)
