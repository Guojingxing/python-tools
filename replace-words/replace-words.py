import os

def load_trans_rules(file_path):
    trans_rules = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                source, target = line.split(' ')
                trans_rules[source] = target
    return trans_rules

def convert_text(input_file, output_file, trans_rules):
    with open(input_file, 'r', encoding='utf-8') as input_f, open(output_file, 'w', encoding='utf-8') as output_f:
        for line in input_f:
            for source, target in trans_rules.items():
                line = line.replace(source, target)
            output_f.write(line)

# 文件路径
input_file = '1.txt'
output_file = '2.txt'
trans_file = 'trans.txt'

# 加载替换规则
trans_rules = load_trans_rules(trans_file)

# 转换文本
convert_text(input_file, output_file, trans_rules)

print('转换完成。')
