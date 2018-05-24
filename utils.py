import os
from datetime import datetime


def get_filename(path):
    return os.path.splitext(os.path.basename(path))[0]


def singularize(noun):
    if noun[-1] in ['s', 'S']:
        return noun[:len(noun) - 1]

    return noun


def convert_reverse_camel_case(string_list):
    return ''.join([string_list[0]] + [
        part.capitalize()
        for part in string_list[1:]
    ])

def convert_camel_case(string_list, capitalize_first=True):
    if capitalize_first:
        return ''.join([
            part.capitalize()
            for part in string_list
        ])

    head = string_list[0]
    tail = [
        part.capitalize()
        for part in string_list[1:]
    ]
    composed = [head]
    composed.extend(tail)
    return ''.join(composed)


def convert_const_case(string_list):
    return '_'.join([
        part.upper()
        for part in string_list
    ])


def create_folder(foldername):
    if not os.path.exists(foldername):
        try:
            os.makedirs(foldername)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


CODE_COLOR_RELATION = {
    'standard': '',
    'header': '\033[95m',
    'okblue': '\033[94m',
    'okgreen': '\033[92m',
    'warning': '\033[93m',
    'fail': '\033[91m',
    'endc': '\033[0m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}


def log(msg, code='standard'):
    nw = datetime.now()
    color = CODE_COLOR_RELATION[code]

    # return "log"

    return "[%s:%s:%s] \t%s%s%s" % (
        nw.hour,
        nw.minute,
        nw.second,
        color,
        msg,
        CODE_COLOR_RELATION['endc'])


def log_title(message):
    return "%s\n%s\n%s\n%s" % (
        log(""),
        log("=" * (len(message) + 2)),
        log(" %s " % message),
        log("=" * (len(message) + 2))
    )


def log_subtitle(message):
    return "%s\n%s\n%s" % (
        log(""),
        log(" %s " % message),
        log("-" * (len(message) + 2))
    )