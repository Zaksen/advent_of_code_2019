with open('inputs/02.txt', 'r') as f:
   program = [int(i) for i in f.read().rstrip().split(',')]

def apply_op_code(program, op_code, position_1, position_2, position_3):
    if op_code == 1:
        program[position_3] = program[position_1] + program[position_2]
    elif op_code == 2:
        program[position_3] = program[position_1] * program[position_2]
    else:
        pass
    return program

def run_program(program, noun, verb):
    program[1] = noun
    program[2] = verb
    for i in range(0, len(program), 4):
        if program[i] == 99:
            break
        else:
            program = apply_op_code(program, program[i], program[i+1], program[i+2], program[i+3])
    return program[0]


def find_noun_verb(program, value):
    for i in range(100):
        for j in range(100):
            if run_program(program[:], i, j) == value:
                return(i, j)

noun, verb = find_noun_verb(program, 19690720)
print(noun * 100 + verb)
