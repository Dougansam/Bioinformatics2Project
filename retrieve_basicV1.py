def search(result):
    if result in ("1A,5"):
        return ["AS03102"], ["10..52"], ["Protein"], ["LAST"]
    else:
        print("fail")


def retrieve_basic(query):
    term = "".join(query + ",5")
    result = search(term)
    return result





typed = "1A"
basic= retrieve_basic(typed)
print(basic)
