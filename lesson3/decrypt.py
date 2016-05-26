def decrypt_character(char):
    value=ord(char)
    upper=char.upper()
    if upper >= 'D' and upper <= 'Z':
        value=value-3
    elif upper >= 'A' and upper <= 'C':
        value=value+23
    return chr(value)
        
encrypted_message=input("Type your encrypted message: ")
message=''
for char in encrypted_message:
    message = message + decrypt_character(char)
print(message)
