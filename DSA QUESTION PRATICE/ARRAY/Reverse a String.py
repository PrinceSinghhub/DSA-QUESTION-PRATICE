def reverseWord(s):
    rev = s[::-1]
    return rev


if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        print(reverseWord(s))
        t = t-1
