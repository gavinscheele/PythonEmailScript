import re


def text_parser(line):
    # Regex to pull out
    match = re.findall(r'[\w\.-]+@[\w\.-]+', line)
    if len(match) == 0:
        raise ValueError('Email address not found')

    return match
