def genrange(start_idx, end_idx):
    current_idx = start_idx
    while current_idx <= end_idx:
        yield current_idx
        current_idx += 1


print(list(genrange(1, 10)))