#!/home/alex/.asdf/shims/python

def is_anagram(phrase1, phrase2):
    return False

if __name__ == "__main__":
    test = [["Listen", "Silent", "Anagram"], ["modern", "norman", "Not Anagrm"]]
    for pair in test:
        print("Teste: ", end="")
        if is_anagram(pair[0], pair[1]) == pair[2]:
            print("Pass")
        else:
            print("Fail")
