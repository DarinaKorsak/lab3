def sortedWords(listWords):
    return sorted(listWords, key=str.lower)


if __name__ == '__main__':
    listWords = input().split(' ')
    print(*sortedWords(listWords))