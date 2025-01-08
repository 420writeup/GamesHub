import os
import shutil

import json5


def center_format_text(text: str = '', fill_char: str = '#'):
    width = shutil.get_terminal_size().columns - 1
    width = min(width, 80)
    if not text:
        return fill_char * width
    if text[0] != ' ':
        text = f' {text}'
    if text[-1] != ' ':
        text += ' '
    return text.center(width, fill_char)


def load_json(path, method="r", init_str="{}"):
    if not os.path.exists(path):
        with open(path, "w", encoding='utf-8') as f:
            f.write(init_str)
    with open(path, method, encoding='utf-8') as f:
        data = json5.load(f)
    return data


def write_json(path, data, method="w"):
    with open(path, method, encoding='utf-8') as f:
        json5.dump(data, f, indent=4)


def record(path, data):  # write data to json file
    if len(data) != 0:
        write_json(path=path, data=data)
