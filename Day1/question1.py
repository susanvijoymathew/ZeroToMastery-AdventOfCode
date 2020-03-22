"""
Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module,
take its mass, divide by three, round down, and subtract 2.

For example:
    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
    The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel
    needed for the mass of each module (your puzzle input), then add together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?
"""

def calculate_fuel_requirement(mass):
    return mass//3 - 2

def totalUp(num_list):
    total = 0
    for n in num_list:
        total += n
    return sum(n + 0 for n in num_list)

module_mass_list = [125517, 140694, 65516, 98562, 75660, 133603, 114499, 81732, 119081, 50911, 96650, 98330, 145164,
    64851, 67455, 108208, 102674, 147581, 112059, 62456, 132006, 88738, 72139, 121074, 103936, 65149, 82081, 90168,
    134670, 79142, 83296, 109983, 60250, 61982, 136326, 52980, 79969, 66851, 77049, 59720, 73494, 115708, 109326,
    136399, 72950, 82041, 105467, 112321, 125019, 79213, 107186, 148340, 112833, 125646, 112509, 52396, 59446, 93967,
    73179, 88725, 98256, 143303, 57503, 120314, 147921, 130856, 95561, 145857, 54976, 100605, 77961, 143120, 84127,
    130389, 131848, 109542, 119653, 61660, 124800, 61498, 149675, 143906, 120361, 68328, 104473, 54279, 119945, 122511,
    109410, 135350, 112070, 88822, 149086, 64594, 118788, 102569, 61721, 89170, 83581, 58722]

fuel_requirements = list(map(calculate_fuel_requirement, module_mass_list))
print(totalUp(fuel_requirements))