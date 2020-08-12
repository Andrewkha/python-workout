def frequency(sentence: str):
    sentence_set = set(sentence.split())
    result = {}

    for one in sentence_set:
        result[one] = sentence.count(one)

    print(result)

frequency('cat dog cat')