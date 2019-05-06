def search(result):
    if result in ("1A,11"):
        return ["AS03102"], ["10..52"], ["Protein"], ["LAST"]
    else:
        print("fail")


def retrieve_all(query):
    term = "".join(query + ",11")
    result = search(term)
    return result





typed = "1A"
allinfo= retrieve_all(typed)
print(allinfo)
