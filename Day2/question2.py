"""
Intcode programs (previous program opcode.py) are given as a list of integers; these values are used as the initial
state for the computer's memory. When you run an Intcode program, make sure to start by initializing memory to the
program's values. A position in memory is called an address (for example, the first value in memory is at "address 0").

Opcodes (like 1, 2, or 99) mark the beginning of an instruction. The values used immediately after an opcode, if any,
are called the instruction's parameters. For example, in the instruction 1,2,3,4, 1 is the opcode; 2, 3, and 4 are the
parameters. The instruction 99 contains only an opcode and has no parameters.

The address of the current instruction is called the instruction pointer; it starts at 0. After an instruction finishes,
the instruction pointer increases by the number of values in the instruction; until you add more instructions to the
computer, this is always 4 (1 opcode + 3 parameters) for the add and multiply instructions. (The halt instruction would
increase the instruction pointer by 1, but it halts the program instead.)

"With terminology out of the way, we're ready to proceed. To complete the gravity assist, you need to determine what
pair of inputs produces the output 19690720."

The inputs should still be provided to the program by replacing the values at addresses 1 and 2, just like before.
In this program, the value placed in address 1 is called the noun, and the value placed in address 2 is called the verb.
Each of the two input values will be between 0 and 99, inclusive.

Once the program has halted, its output is available at address 0, also just like before. Each time you try a pair of
inputs, make sure you first reset the computer's memory to the values in the program (your puzzle input) - in other
words, don't reuse memory from a previous attempt.

Find the input noun and verb that cause the program to produce the output 19690720. What is 100 * noun + verb? (For
example, if noun=12 and verb=2, the answer would be 1202.)
"""

opcodes_input_original = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0"

# Modify the input to contain 12 at index 1 and 2 at index 2.
# opcodes_input_modified = "1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0"

# Remove the commas and convert the numbers from string to integers.
opcodes_original = list(map(int, opcodes_input_original.split(",")))
numCount = len(opcodes_original)
noun_verb_found = False
noun, verb = -1, -1

# for n in range(99, -1, -1):
for n in range(100):
    if noun_verb_found:
        break

    for v in range(100):
        # Reset input to original values
        opcodes = opcodes_original[:]
        opcodes[1] = n
        opcodes[2] = v
        indx = 0

        while indx < numCount and opcodes[indx] != 99:
            if opcodes[indx] == 1:
                num1_loc, num2_loc = opcodes[indx + 1], opcodes[indx + 2]
                result_loc = opcodes[indx + 3]
                opcodes[result_loc] = opcodes[num1_loc] + opcodes[num2_loc]
                indx += 4
                continue

            if opcodes[indx] == 2:
                num1_loc, num2_loc = opcodes[indx + 1], opcodes[indx + 2]
                result_loc = opcodes[indx + 3]
                opcodes[result_loc] = opcodes[num1_loc] * opcodes[num2_loc]
                indx += 4
                continue

            indx += 1
        # end while loop

        if opcodes[0] == 19690720:
            noun, verb = n, v
            noun_verb_found = True
            break
    # end for v loop
# end for n loop

print(100 * noun + verb)

