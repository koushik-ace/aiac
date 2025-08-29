def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            try:
                denominator = values[j] - values[i]
                ratio = values[i] / denominator
                results.append((i, j, ratio))
            except ZeroDivisionError:
                results.append((i, j, None))  # or handle division by zero as needed
    return results

nums = [5, 10, 15, 20, 25]
print(compute_ratios(nums))
