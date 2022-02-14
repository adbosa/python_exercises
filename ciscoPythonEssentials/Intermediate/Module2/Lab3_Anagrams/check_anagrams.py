#!/home/alex/.asdf/shims/python

def is_anagram(phrase1, phrase2):
    text1 = clean_phrase(phrase1)
    text2 = clean_phrase(phrase2)

    text1 = sorted(list(text1))
    text2 = sorted(list(text2))

    if text1  == text2:
        return "Anagram"
    else:
        return "Not Anagram"

def clean_phrase(phrase):
    new_string = ""
    for  letter in phrase:
        if letter.isalpha():
            new_string += letter.upper()
    return new_string

if __name__ == "__main__":
    test = [["Listen", "Silent", "Anagram"], ["modern", "norman", "Not Anagram"]]
    test_num = 0
    for pair in test:
        test_num += 1
        print(f"Teste {test_num}: ", end="")
        if is_anagram(pair[0], pair[1]) == pair[2]:
            print("Pass")
        else:
            print("Fail")
