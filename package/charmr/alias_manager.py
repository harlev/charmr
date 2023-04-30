import unicodedata
import re


def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def get_file_name(alias):
    return f"{slugify(alias)}.charmr"


def save_code(code_str, alias):
    file_name = get_file_name(alias)
    with open(file_name, 'w') as f:
        f.write(code_str)


def load_code(alias):
    file_name = get_file_name(alias)
    with open(file_name, 'r') as f:
        code_str = f.read()

    return code_str
