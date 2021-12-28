

class Palindrome:

    def __init__(self, word = "wow"):
        self.string = word


    def getString(self):
        return self

    def setString(self, word):
        self.string = word

    def isPalendrome(self):
        low = 0
        high = len(self.string) - 1

        while low < high:
            if self.string[low] != self.string[high]:
                return False

            low += 1
            high -= 1

        return True

def main():
    p = Palindrome()
    word = input("enter a word:")
    p.setString(word)
    if p.isPalendrome():
        print (word, "is a palindrome")

    else:
        print (word, "isnt' a palindrome")



main()