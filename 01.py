def calculate_fuel_part_two(module):
    sum_of_fuels = 0
    while int(module/3) - 2 > 0:
        module = int(module/3) - 2
        sum_of_fuels += module
    return sum_of_fuels

part_one = 0
part_two = 0

with open('inputs/01.txt', 'r') as f:
    for mass in f:
        part_one += int(int(mass.rstrip())/3) - 2
        part_two += calculate_fuel_part_two(int(mass.rstrip()))

print(part_one, part_two)