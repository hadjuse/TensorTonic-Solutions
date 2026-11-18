def target_encoding(categories: list, targets: list) -> list:
    """
    Returns each category replaced by its mean target.
    """
    frequencies = {}
    target_sum = {}
    encodings = [0] * len(targets)
    
    for category in categories:
        frequencies[category] = frequencies.get(category, 0 ) + 1
        target_sum[category] = target_sum.get(category, 0)

    for j in range(len(targets)):
        target_sum[categories[j]] += targets[j]

    for i in range(len(encodings)):
        encodings[i] = (1 / frequencies[categories[i]]) * target_sum[categories[i]]
    return encodings