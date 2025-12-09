string = input("Enter your string: ")
shift = int(input("Enter shift value: "))

# Normalize shift (handles big numbers)
shift = shift % len(string)

# Shift left by 'shift' positions
shifted_string = string[shift:] + string[:shift]

print("Shifted string:", shifted_string)
