def check1(word):
    if word[0] == word[1]:
        return True

def check2(word):
    char_list = []
    cursor = 0
    for char in word:
        if char in char_list:
            break
        else:
            char_list.append(char)
            for




total = 0
word = input()
