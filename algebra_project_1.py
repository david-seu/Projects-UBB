import copy
from itertools import permutations


def generate_set_of_elements(set_cardinality):
    """
    Generates a set that will be used for partitioning
    :param set_cardinality: number of elements received from input
    :return: a set of elements in the for ai
    """
    set_of_elements = []
    for i in range(1, set_cardinality+1):
        set_of_elements.append(f'a{i}')
    return set_of_elements


def calculate_number_of_partitions(set_cardinality):
    """
    Calculates the number of partitons using Bell's number triangle scheme
    :param set_cardinality: number of elements received from input
    :return: the number of partitions from a set with set_cardinality elements
    """
    bell_number_triangle_scheme = [[1]]
    for i in range(1, set_cardinality):
        previous_line = bell_number_triangle_scheme[i-1]
        line = [previous_line[-1]]
        for j in range(1, len(previous_line)+1):
            line.append(line[j-1]+previous_line[j-1])
        bell_number_triangle_scheme.append(line)
    return bell_number_triangle_scheme[-1][-1]


def generate_all_partitions(set_of_elements, index_current_element, number_of_partitions,
                            current_partition, all_partitions):
    """

    :param set_of_elements:
    :param index_current_element:
    :param number_of_partitions:
    :param current_partition:
    :param all_partitions:
    :return:
    """
    number_of_elements_in_current_partition = 0
    for index_current_subset in range(len(current_partition)):
        number_of_elements_in_current_partition += len(current_partition[index_current_subset])
    if number_of_elements_in_current_partition == len(set_of_elements):
        all_partitions.append(copy.deepcopy(current_partition))
        return
    for index_current_subset in range(len(current_partition)):
        current_partition[index_current_subset].append(set_of_elements[index_current_element])
        generate_all_partitions(set_of_elements, index_current_element+1, number_of_partitions,
                                current_partition, all_partitions)
        current_partition[index_current_subset].pop()
    current_partition.append([set_of_elements[index_current_element]])
    generate_all_partitions(set_of_elements, index_current_element + 1, number_of_partitions,
                            current_partition, all_partitions)
    current_partition.pop()
    if len(all_partitions) == number_of_partitions:
        return all_partitions


def generate_equivalence_relation_graph(partition):
    equivalence_relation_graph = []
    for subset in partition:
        for element in subset:
            equivalence_relation_graph.append((element, element))
        equivalence_relation_graph += list(permutations(subset, 2))
    return equivalence_relation_graph


def run():
    number_of_elements = int(input('Enter a non-zero natural number: '))
    number_of_partitions = calculate_number_of_partitions(number_of_elements)
    generated_set_of_elements = generate_set_of_elements(number_of_elements)
    print(f"The number of partitions for a set with {number_of_elements} elements is: {number_of_partitions}")
    all_partitions = generate_all_partitions(generated_set_of_elements, 1,
                                             number_of_partitions, [[generated_set_of_elements[0]]], [])
    print(f'The partitions of a set with {number_of_elements} elements '
          f'and their corresponding equivalence relations are: ')
    for partition in all_partitions:
        for subset in partition:
            print('{', end='')
            for element in subset[:-1]:
                print(f'{element},', end='')
            print(f'{subset[-1]}', end='')
            print('}', end=' ')
        print('-->>', end=' ')
        equivalence_relation_graph = generate_equivalence_relation_graph(partition)
        print('{', end='')
        for pair in equivalence_relation_graph[:-1]:
            print(f'{pair},', end='')
        print(f'{equivalence_relation_graph[-1]}', end='')
        print('}', end=' ')
        print('')


if __name__ == '__main__':
    run()
