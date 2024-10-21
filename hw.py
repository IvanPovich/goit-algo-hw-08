import heapq

lists = [1, 4, 5, 1, 3, 4, 2, 6]
print("\n")

def cost_min_connection(arr):
    heapq.heapify(arr)

    total_coast = 0

    while len(arr) > 1:
        first_cab = heapq.heappop(arr)
        second_cab = heapq.heappop(arr)

        coast = first_cab + second_cab
        total_coast += coast

        heapq.heappush(arr, coast)

    return total_coast

print(f"Мінімальна вартість зєднань: {cost_min_connection(lists)}")

### Task 2

def merge_k_lists(lists):
    marge_list = list(heapq.merge(*lists))

    return marge_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
