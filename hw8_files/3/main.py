import os

file_result = 'result.txt'

if file_result in os.listdir('.'):
    os.remove(file_result)

files = [file for file in os.listdir('.') if file.endswith('.txt')]
info = {}

for file in files:
    with open(file, 'rt', encoding='utf-8') as f:
        lines = f.readlines()
        info[file] = {
            'length': len(lines),
            'text': ''.join(lines),
        }

info_sorted = sorted(info.items(), key=lambda x: x[1]['length'])

with open('result.txt', 'w', encoding='utf-8') as f:
    for file_name, file_info in info_sorted:
        f.write(file_name + '\n')
        f.write(str(file_info['length']) + '\n')
        f.write(file_info['text'] + '\n')
