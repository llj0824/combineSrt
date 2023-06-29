def read_srt(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read().strip().split('\n\n')

def write_srt(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(content)

def merge_srt(file1, file2, output_file):
    srt1 = read_srt(file1)
    srt2 = read_srt(file2)

    if len(srt1) != len(srt2):
        raise ValueError('Mismatch in number of blocks')

    merged = []
    for i, (block1, block2) in enumerate(zip(srt1, srt2), start=1):
        lines1 = block1.split('\n')
        lines2 = block2.split('\n')

        if lines1[1] != lines2[1] or lines1[1] != lines2[1]:
            breakpoint()
            raise ValueError(f'Mismatch in block headers at block {i}\n'
                             f'File 1: {lines1[0]}, {lines1[1]}\n'
                             f'File 2: {lines2[0]}, {lines2[1]}')

        merged.append('\n'.join(lines1 + lines2[2:]))

    write_srt(output_file, '\n\n'.join(merged))

file1 = input('Enter the first srt file: ')
file2 = input('Enter the second srt file: ')
output_file = 'merged.srt'

merge_srt(file1, file2, output_file)