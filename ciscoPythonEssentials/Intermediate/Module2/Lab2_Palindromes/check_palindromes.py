#!/usr/bin/python

def main():
    user_input = ""
    while user_input.strip() == "":
        user_input = input("Insert some text: ")
    return is_palindrome(user_input)

def is_palindrome(string):
    sentence = ""
    for char in string:
        if char != " ":
            sentence += char.upper()

    phrase_len = len(sentence)
    reverse_sequence = -1

    for i in range(phrase_len//2):
        if sentence[i] != sentence[reverse_sequence]:
            return False
        else:
            reverse_sequence -= 1
    return True
    
            

### Tests ###
if __name__ == "__main__":
    phrases = ["Ten animals I slam in a net",
            "Eleven animals I slam in a net"]
    for phrase in phrases:
        if is_palindrome(phrase):
            print("It's a palindrome")
        else:
            print("It's not a palindrome")
