#!/usr/bin/env python3
import pyperclip

def parse_code(s):
    result = []
    lines = s.splitlines()
    end = len(lines)
    for index, line in enumerate(lines):
        next_index = index + 1
        if line.startswith('>>>') and next_index != end:
            block = [line[4:]]
            while next_index != end and lines[next_index].startswith('...'):
                block.append(lines[next_index][4:])
                next_index += 1
            while next_index != end and not any(lines[next_index].startswith(s) for s in ('>>>', 'Trace', '  File')):
                next_index +=1

            if next_index != end and lines[next_index].startswith('>>>'):
                result.append('\n'.join(block))

    if lines[-1].startswith('>>>'):
        result.append(lines[-1][4:])
    return '\n'.join(result)

def copy(to_end=False):
    if to_end:
        with open('/Users/john/Terminal Saved Output', 'r') as f:
            output = f.read().replace('bpython', 'Python')
            code = output.split('\nPython')[-1]
    else:
        code = pyperclip.paste()
    pyperclip.copy(parse_code(code))
    return None

