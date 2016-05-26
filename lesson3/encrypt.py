def encrypt_character(char):
    value=ord(char)
    upper=char.upper()
    if upper >= 'A' and upper <= 'W':
        value=value+3
    elif upper >= 'X' and upper <= 'Z':
        value=value-23
    return chr(value)
        
message=input("Type your secret message: ")
encrypted_message=''
for char in message:
    encrypted_message = encrypted_message + encrypt_character(char)
print(encrypted_message)
