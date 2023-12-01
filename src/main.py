def find_needle(haystack, needle):
    comparisons = 0
    last_index = -1
    len_haystack = len(haystack)
    len_needle = len(needle)

    for i in range(len_haystack - len_needle + 1):
        match = True
        for j in range(len_needle):
            comparisons += 1
            if haystack[i + j] != needle[j]:
                match = False
                break

        if match:
            last_index = i

    return last_index, comparisons


haystack = "needle in a haystack"
needle = "needle"
result_index, comparison_count = find_needle(haystack, needle)
print("Індекс останнього входження підстрічки:", result_index)
print("Кількість порівнянь:", comparison_count)
