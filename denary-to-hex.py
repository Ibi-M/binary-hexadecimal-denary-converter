number = int(input("Enter a number: ")) # Asks input for number to convert

digit1 = number // 16 # Gets the first digit in hex by finding how many times 16 exactly goes into the number
digit2 = number % 16 # The remainder

digits = [digit1, digit2]

for i in range(len(digits)): # Loop to convert any digits above 9 to correct letters
    if digits[i] == 10:
        digits[i] = "A"
    elif digits[i] == 11:
        digits[i] = "B"
    elif digits[i] == 12:
        digits[i] = "C"
    elif digits[i] == 13:
        digits[i] = "D"
    elif digits[i] == 14:
        digits[i] = "E"
    elif digits[i] == 15:
        digits[i] = "F"

hex_value = str(digits[0]) + str(digits[1]) # Joins the digits together
print(f"Hexadecimal value: {hex_value}") 
