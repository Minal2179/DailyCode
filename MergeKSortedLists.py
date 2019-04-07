import heapq


def mergeKLists(lists):
    merged_list = []

    heap = [(each[0], ind, 0) for ind, each in enumerate(lists) if each]
    heapq.heapify(heap)

    while heap:
        val, list_index, element_index = heapq.heappop(heap)

        merged_list.append(val)

        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)

            heapq.heappush(heap, next_tuple)

    return merged_list


if __name__ == "__main__":
    lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    lists = [[], [], []]
    merged_list = mergeKLists(lists)
    print(merged_list)

