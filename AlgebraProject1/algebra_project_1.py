import copy
from itertools import permutations


def generate_set_of_elements(set_cardinality):
    """
    Generates a set that will be used for partitioning
    :param set_cardinality: number of elements received from input
    :return: a set of elements in the for ai
    """
    set_of_elements = []
    for i in range(1, set_cardinality + 1):
        set_of_elements.append(f'a{i}')
    return set_of_elements


def calculate_number_of_partitions(set_cardinality):
    """
    Calculates the number of partitions using Bell's number triangle scheme
    :param set_cardinality: number of elements received from input
    :return: the number of partitions from a set with set_cardinality elements
    """
    bell_number_triangle_scheme = [[1]]
    for i in range(1, set_cardinality):
        previous_line = bell_number_triangle_scheme[i - 1]
        line = [previous_line[-1]]
        for j in range(1, len(previous_line) + 1):
            line.append(line[j - 1] + previous_line[j - 1])
        bell_number_triangle_scheme.append(line)
    return bell_number_triangle_scheme[-1][-1]


def generate_all_partitions(set_of_elements, index_current_element, number_of_partitions,
                            current_partition, all_partitions):
    """
    It generates all the partitions of a set by using a rotted tree method and implementing it as backtracking
    :param set_of_elements: the set from which the partitions are generated
    :param index_current_element: the current element which we add to the current partition
    :param number_of_partitions: the total number of partitions calculated before using Bell's number triangle scheme
    :param current_partition:
    :param all_partitions: a list where we store all the partitions
    :return: all_partitions
    """
    number_of_elements_in_current_partition = 0
    # calculates the number of elements already added to the partition
    for index_current_subset in range(len(current_partition)):
        number_of_elements_in_current_partition += len(current_partition[index_current_subset])
    if number_of_elements_in_current_partition == len(set_of_elements):
        all_partitions.append(copy.deepcopy(current_partition))
        return
    # using a rotted tree with the root being the first element in the set
    # create a new branches by adding the next element in each subset at a time
    for index_current_subset in range(len(current_partition)):
        current_partition[index_current_subset].append(set_of_elements[index_current_element])
        generate_all_partitions(set_of_elements, index_current_element + 1, number_of_partitions,
                                current_partition, all_partitions)
        current_partition[index_current_subset].pop()
    current_partition.append([set_of_elements[index_current_element]])
    generate_all_partitions(set_of_elements, index_current_element + 1, number_of_partitions,
                            current_partition, all_partitions)
    current_partition.pop()
    if len(all_partitions) == number_of_partitions:
        return all_partitions


def generate_equivalence_relation_graph(partition):
    """
    It generates the equivalence relation graph for a partition
    by generating all the possible pairs of the elements in each subset of the partition
    plus the pairs of identical elements
    :param partition: a partition of a given set
    :return: the equivalence relation graph of that partition
    """
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
            print(f'({pair[0]},', end='')
            print(f'{pair[1]}', end='), ')
        print(f'{equivalence_relation_graph[-1][0]},', end='')
        print(f'{equivalence_relation_graph[-1][1]})', end='')
        print('}', end=' ')
        print('')


if __name__ == '__main__':
    run()
