import sympy

with open('./input.txt') as data:
    hailstones = [tuple(map(int, line.replace(' @', ',').split(','))) for line in data.readlines()]
    p_x, p_y, p_z, v_x, v_y, v_z = sympy.symbols('p_x p_y p_z v_x v_y v_z')
    equations = []
    for i, hailstone in enumerate(hailstones[:20]):
        h_p_x, h_p_y, h_p_z, h_v_x, h_v_y, h_v_z = hailstone
        t = sympy.symbols(f't_{i}')
        equations.append(sympy.Eq(h_p_x + (t * h_v_x), p_x + (t * v_x)))
        equations.append(sympy.Eq(h_p_y + (t * h_v_y), p_y + (t * v_y)))
        equations.append(sympy.Eq(h_p_z + (t * h_v_z), p_z + (t * v_z)))
    values = sympy.solve(equations)[0]
    print(values[p_x] + values[p_y] + values[p_z])