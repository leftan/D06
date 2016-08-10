def write_name_with_e():
    with open('d06_ex4.txt', 'w') as fin:
        name_list, count = find_name_with_e()
        fin.write(str(name_list) + '\n')
        fin.write('count = {}'.format(count))


def find_name_with_e():
    with open('roster.txt', 'r') as fin:
        count = 0
        name_list = []
        for line in fin:
            first_name = line.split()[0]
            if 'e' in first_name.lower():
                count += 1
                name_list.append(first_name)
        return name_list, count

def main():
    write_name_with_e()
    

if __name__ == '__main__':
    main()        
