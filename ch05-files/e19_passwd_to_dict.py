#!/usr/bin/env python3
"""Solution to chapter 5, exercise 19: passwd_to_dict"""


def passwd_to_dict(filename):
    """Expects to get a string argument, the name of a file in passwd format.
    Returns a dictionary in which the keys are the usernames from the file,
    and the values are the user IDs from the file.  The user IDs should be
    returned as integers.
    """
    result = {}
    for line in open(filename):
        if not line.startswith('#') and line.strip():
            data = line.split(':')
            result[data[0]] = int(data[2])

    return result


def login_shells():
    """
     Read through /etc/passwd, creating a dict in which user login shells (the final
    field on each line) are the keys. Each value will be a list of the users for whom
    that shell is defined as their login shell
    """
    result = {}
    for line in open('linux-etc-passwd.txt'):
        if not line.startswith('#') and line.strip():
            name = line.split(':')[0]
            shell = line.split('/')[-1].rstrip()
            result[shell] = result.get(shell, []) + [name]

    return result


def parse_lnx():
    """
     From /etc/passwd, create a dict in which the keys are the usernames (as in the
    main exercise) and the values are themselves dicts with keys (and appropriate
    values) for user ID, home directory, and shell
    """
    result = {}
    for line in open('linux-etc-passwd.txt'):
        if not line.startswith('#') and line.strip():
            splitted_line = line.split(':')
            name = splitted_line[0]
            id = splitted_line[2]
            home = splitted_line[5]
            shell = splitted_line[-1].rstrip()

            result[name] = {'id': id, 'home': home, 'shell': shell}

    return result


# print(passwd_to_dict('linux-etc-passwd.txt'))
# print(login_shells())
print(parse_lnx())
