with open('./input.txt') as data:
    lines = data.readlines()
    predictions_sum = 0
    for line in lines:
        readings = list(map(lambda x: int(x), line.strip().split(' ')))
        first_vals = [readings[0]]
        all_zeros = False
        while not all_zeros:
            all_zeros = True
            readings_diffs = []
            for reading_idx in range(1, len(readings)):
                reading_diff = readings[reading_idx] - readings[reading_idx - 1]
                if not reading_diff == 0:
                    all_zeros = False
                readings_diffs.append(reading_diff)
            first_vals.insert(0, readings_diffs[0])
            readings = readings_diffs
        prediction = first_vals[0]
        for last_val_idx in range(1, len(first_vals)):
            prediction = -prediction + first_vals[last_val_idx]
        predictions_sum += prediction
    print(predictions_sum)