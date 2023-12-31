with open('./input.txt') as data:
    hailstones = [tuple(map(int, line.replace(' @', ',').split(','))) for line in data.readlines()]

    def get_slope_and_intercept(hs):
        p1 = hs[0:2]
        p2 = tuple(map(lambda i, j: i + j, hs[0:2], hs[3:5]))
        slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
        int_y = p1[1] - (p1[0] * slope)
        return slope, int_y
    
    def get_intercept(hs1, hs2):
        m1, b1 = get_slope_and_intercept(hs1)
        m2, b2 = get_slope_and_intercept(hs2)
        try:
            x_int = (b1 - b2) / (m2 - m1)
            y_int = m1 * x_int + b1
            return x_int, y_int
        except:
            return None

    lims = (200000000000000, 400000000000000)
    hailstones_crossing = 0

    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[i + 1:]:
            if intercept := get_intercept(hs1, hs2):
                x_int, y_int = intercept
                if hs1[3] > 0 and x_int < hs1[0]:
                    continue
                elif hs1[3] < 0 and x_int > hs1[0]:
                    continue
                if hs2[3] > 0 and x_int < hs2[0]:
                    continue
                elif hs2[3] < 0 and x_int > hs2[0]:
                    continue
                if hs1[4] > 0 and y_int < hs1[1]:
                    continue
                elif hs1[4] < 0 and y_int > hs1[1]:
                    continue
                if hs2[4] > 0 and y_int < hs2[1]:
                    continue
                elif hs2[4] < 0 and y_int > hs2[1]:
                    continue
                if lims[0] <= x_int <= lims[1] and lims[0] <= y_int <= lims[1]:
                    hailstones_crossing += 1
    
    print(hailstones_crossing)
        