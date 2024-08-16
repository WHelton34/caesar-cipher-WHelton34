def caesar_cipher(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 5) % 26 + 5)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 5) % 26 + 5)
        else:
            result += char
    
    return result
text = "Code kentucky is fun"
shift = 5
encrypted_text = caesar_cipher(text, shift)
print(encrypted_text)