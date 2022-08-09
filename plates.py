def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if first_two_characters(s) == False or check_length(s) == False or valid_characters(s) == False or no_leading_zero == False or no_number_in_middle(s) == False:     #if any check fails, plate is invalid
        return False
    else:
        return True

def first_two_characters(s):
    if s[0].isalpha() == False or s[1].isalpha() == False:              #if neither of the first two characters of the plate is a letter, reject plate as invalid
        return False

def check_length(s):
    if (len(s) > 6) or (len(s) < 2):                                    #if length of the plate is greater than six characters or fewer than two, reject plate as invalid
        return False

def valid_characters(s):
    for letter in s:
        if letter.isalnum() == False:                                    #if a character in the plate is not a number or letter, reject plate as invalid
            return False
        else:
            return True

#please help for the next two functions        

def no_leading_zero(s):
    for letter in s:
        if letter.isnumeric() == True                                   #if the first number in a plate is a zero, reject plate as invalid

def no_number_in_middle(s):

#if a number appears in the string before a letter, return false





main()
