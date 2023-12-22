def count_of_pairs(pairs):
    t = [set(pairs[0])]
    count = 0
    for pair in pairs[1:]:
        for tribe in t:
            if any(person in tribe for person in pair):
                tribe.update(pair)
                break
            elif set(pair) in t:
                break
            else:
                t.append(set(pair))
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            for first_person in t[i]:
                for second_person in t[j]:
                    if first_person % 2 != second_person % 2:
                        count += 1
    return count


def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        pairs = [tuple(map(int, line.split())) for line in lines[1:]]
    return n, pairs


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


def main(input_filename, output_filename):
    n, pairs = read_input(input_filename)
    result = count_of_pairs(pairs)
    write_output(output_filename, result)


if __name__ == "__main__":
    input_filename = 'input.txt'
    output_filename = 'output.txt'

    main(input_filename, output_filename)