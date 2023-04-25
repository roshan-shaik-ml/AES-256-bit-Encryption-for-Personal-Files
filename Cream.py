def creamlayer(s):
    result = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + 13 - 65) % 26 + 65)
            else:
                result += chr((ord(char) + 13 - 97) % 26 + 97)
        else:
            result += char
    return result

input_file = open("Y4C7N.txt", "r")
output_file = open("output.txt", "w")

for line in input_file:
    output_file.write(creamlayer(line))

input_file.close()
output_file.close()