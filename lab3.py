def characterCount():

    frames = []
    ans = 'y'

    while ans == 'y':

        word = input("enter a word: ")
        frame = list(word)
        leng = 0
        for index in word:

            leng += 1
        frame.insert(0, leng+1)
        frames.append(frame)
        ans = input("do you want to continue [y/n]? ")
    print(frames)

if __name__ == "__main__":

    characterCount()