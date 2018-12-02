
_over = False
while _over != True:
    print("q for exit")
    _list = input("Word:")
    if _list == "q":
        _over = True
    else:
        _return = ""
        _list2 = []
        i = -1

        for words in _list:
            _list2.append(words)

        for _words in _list2:
            _return = _return + _list2[i]
            i = i - 1
        print(_return)

