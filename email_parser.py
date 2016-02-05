def text_parser(line):
    end_index = line.find(".edu")
    if end_index == -1:
        raise ValueError('Email address not found')

    return line[0:(end_index + 4)]
