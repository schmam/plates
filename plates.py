def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if check_length(s) == False or valid_characters(s) == False or first_two_characters(s) == False or no_leading_zero(s) == False or no_number_in_middle(s) == False:     #if any check fails, plate is invalid
        return False
    else:
        return True

def check_length(s):
    if (len(s) > 6) or (len(s) < 2):                                    #if length of the plate is greater than six characters or fewer than two, reject plate as invalid
        return False

def valid_characters(s):
    if s.isalnum() == False:                                            #if a character in the plate is not a number or letter, reject plate as invalid
        return False
    else:
        return True

def first_two_characters(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:              #if neither of the first two characters of the plate is a letter, reject plate as invalid
        return False

def no_leading_zero(s):                                                 #if the first number in a plate is a zero, reject plate as invalid
    i = 0                                                               #creating temporary variable to help with determining whether zero is the first number in the string
    for letter in s:
        if letter.isnumeric() == True and letter != "0":                  #if "letter" is a number and is not zero, increment i
            i += 1
        elif letter == "0":                                               #if "letter" is a zero and no numbers have been identified before it (indicated by i), return false
            if i == 0:
                return False

def no_number_in_middle(s):                                             #if a number appears in the string before a letter, return false
    i = 0                                                               #creating temporary variable to help with determining whether a number appears before a letter in the string
    for letter in s:
        if letter.isnumeric() == True:                                  #if "letter" is a number, increment i
            i += 1
        elif letter.isalpha() == True and i > 0:                        #if "letter" is a number appearing before a letter (indicated by i), return false
            return False

main()
