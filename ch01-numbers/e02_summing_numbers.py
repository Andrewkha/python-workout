def mysum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


def mysum_two_args(lst, start=0):
    sum = start
    for i in lst:
        sum += i
    return sum


def average(args):
    sum = mysum_two_args(args)
    return sum / len(args)


def strings_length(strings):
    lengths = []
    for word in strings:
        lengths.append(len(word))
    return max(lengths), min(lengths), average(lengths)


def objects(lst):
    filtered = []

    for item in lst:
        try:
            filtered.append(int(item))
        except Exception:
            continue

    return mysum_two_args(filtered)

print(mysum(3, 5, 6, 7, 79))
print(mysum_two_args([1, 2, 3], 4))
print(average([1, 2, 3]))
print(strings_length(['hello', 'd', 'thisisfuckingstring']))
print(objects([1, 2.5, '1', 'sdsdsdsd', '10', [1, 2, 3], {'a': 1, 'b': 2}]))

