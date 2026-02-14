input_str = input("Enter a string: ")

character_frequency = {}

for letter in input_str:
    if letter in character_frequency:
        character_frequency[letter] += 1
    else:
        character_frequency[letter] = 1

result_parts = []
for letter, frequency in character_frequency.items():
    result_parts.append(f"{letter}:{frequency}")

print(", ".join(result_parts))
