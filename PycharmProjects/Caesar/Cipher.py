import sys
print(sys.argv)


def encrypt(text,s):
    #stores the encrypted words
    theCode = []

    #encrypts the code word by word
    for word in text.split():
        result = ""

        for i in range(len(word)):
            character = word[i]

            if character.isupper():
                result += chr((ord(character) + s - 65) % 26 + 65)

            elif character.islower():
                result += chr((ord(character) + s - 97) % 26 + 97)

            else:
                result += character



        theCode.append(result)

    #combines the list of words as a single sentance
    finalCode = " ".join(word for word in theCode )
    return finalCode



def main():
    text = open(input())
    text = text.read()
    rotation = input() or "0"
    s = int(rotation)

    if rotation == "0":
        for i in range(25):
            print(" =======================\n",
                  "Rotated by ", i, " positions\n",
                  "=======================\n",
                  encrypt(text, i), "\n")


    elif s > 25 or s < 0 :
        print("Error: rotation distance must be between 0 and 25")

    else:
        print(" =======================\n",
            "Rotated by ", s, " positions\n",
            "=======================\n",
            encrypt(text, s), "\n")
main()


