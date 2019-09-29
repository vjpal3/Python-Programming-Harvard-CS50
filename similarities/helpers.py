from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # TODO
    aList = a.splitlines()
    bList = b.splitlines()
    matches = set()

    for line in aList:
        try:
            index = bList.index(line)
        except ValueError:
            index = -1

        if not index == -1:
            matches.add(line)

    # print(list(matches))
    return list(matches)


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    aSentences = sent_tokenize(a)
    bSentences = sent_tokenize(b)
    print(aSentences)
    print(bSentences)

    matches = set()
    for sentence in aSentences:
        try:
            index = bSentences.index(sentence)
        except ValueError:
            index = -1

        # print(index)
        if not index == -1:
            matches.add(sentence)

    # print(list(matches))
    return list(matches)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    aSubstringList = extractSubstr(a, n)
    bSubstringList = extractSubstr(b, n)

    matches = set()
    for substr in aSubstringList:
        try:
            index = bSubstringList.index(substr)
        except ValueError:
            index = -1

        # print(index)
        if not index == -1:
            matches.add(substr)

    # print(list(matches))
    return list(matches)


def extractSubstr(a, n):
    sList = []
    for i in range(len(a)):
        if i+n > len(a):
            break;
        sList.append(a[i:i+n])

    return sList