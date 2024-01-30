import heapq


def min_summa(cable_lengths):
    heapq.heapify(cable_lengths)
    cost = 0
    i = 0
    print(f"Order of connection cables with lengths {cable_lengths}")
    while len(cable_lengths) > 1:
        first_min_el = heapq.heappop(cable_lengths)
        second_min_el = heapq.heappop(cable_lengths)
        summa = first_min_el + second_min_el
        cost += summa
        i += 1
        print(f"{i}. {first_min_el} + {second_min_el} --> {summa}")
        heapq.heappush(cable_lengths, summa)
    return f"For connecting cables with a total length of {cable_lengths[0]}, the min cost is equal {cost}"


if __name__ == "__main__":
    cable_lengths = [2, 5, 25, 23, 12, 8, 6, 11]
    print(min_summa(cable_lengths))
