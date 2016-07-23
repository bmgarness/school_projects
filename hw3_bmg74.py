#!/usr/bin/python3
# Benjamin Garness
# CS0008 HW 3

def main():
    out = open('decoded.txt', 'w')
    file1 = open('file1.txt')
    file2 = open('file2.txt')
    file3 = open('file3.txt')
    
    line1 = get_line_from_file1(file1)
    line2 = get_line_from_file2(file2)
    line3 = get_line_from_file3(file3)
    while line1 or line2 or line3:
        out.write(line1.rstrip() + '\n')
        out.write(line2.rstrip() + '\n')
        out.write(line3.rstrip() + '\n')
        line1 = get_line_from_file1(file1)
        line2 = get_line_from_file2(file2)
        line3 = get_line_from_file3(file3)
    
    out.close()
    file1.close()
    file2.close()
    file3.close()

def get_line_from_file1(file1):
    line = file1.readline()
    line = line.strip('\n')
    while True:
        if not line.startswith('ZZ'):
            line = file1.readline()
            if line == '':
                break
        else:
            break
    line = line.strip('ZZ')
    line = line.strip('\n')
    return line
        

def get_line_from_file2(file2):
    good_line = ''
    line = file2.readline()
    line = line.replace('\n', '')
    if line == '':
        return line
    else:
        line = line.split(' ')
        for l in line:
            l = l[::-1]
            good_line += l
            good_line += ' '
    return good_line

def get_line_from_file3(file3):
    line = file3.readline()
    line = line.replace('\n', '')
    if line == '':
        return line
    else:
        line = line.split(' ')
        good_line = ''
        for l in line:
            last = l[-1:]
            if last == last.lower():
                last = last.upper()
            else:
                last = last.lower()
            first = l[:-1]
            good_line += last
            good_line += first
            good_line += ' '
        return good_line
                
            

main()
