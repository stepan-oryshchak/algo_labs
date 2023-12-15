from collections import defaultdict


def build_adjacency_list(file_name):
    adjacency_list = defaultdict(list)
    with open(file_name, 'r') as file:
        lines = file.readlines()
        root = int(lines[0].strip())
        for line in lines[1:]:
            edge = list(map(int, line.strip().split(',')))
            adjacency_list[edge[0]].append(edge[1])

    return root, adjacency_list


def min_depth_with_path(root, adjacency_list):
    if root not in adjacency_list:
        return 0, ""

    queue = [(root, [str(root)])]

    while queue:
        node, path = queue.pop(0)
        neighbors = adjacency_list[node]

        if not neighbors:
            return len(path), " —> ".join(path)

        for neighbor in neighbors:
            new_path = path + [str(neighbor)]
            queue.append((neighbor, new_path))


def write_to_output(result, output_file):
    with open(output_file, 'w') as file:
        file.write(result)


input_file = 'input.txt'
output_file = 'output.txt'

root, adjacency_list = build_adjacency_list(input_file)
min_depth_value, path = min_depth_with_path(root, adjacency_list)

result_string = f"Мінімальна глибина дерева: {min_depth_value}\nШлях: {path}"
write_to_output(result_string, output_file)
