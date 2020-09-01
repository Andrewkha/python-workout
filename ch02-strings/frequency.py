def frequency(sentence: str):
    sentence_set = set(sentence.split())
    result = {}

    for one in sentence_set:
        result[one] = sentence.count(one)

    print(result)

frequency('cat dog cat')


def frequency2(sequence: str):

    result = {}
    for char in sequence:
        result[char] = result.get(char, 0) + 1

    return max(result, key=result.get)


print(frequency2('assdzs232@!(#&*@&^#2123231'))
