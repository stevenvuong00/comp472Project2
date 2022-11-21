import sys

import numpy as np
from board import Board
from ucs import UCS


def parse_fuel(fuel_input):
    fuel = {}
    parsed = list(map(fn, fuel_input))
    for pair in parsed:
        fuel[pair[0]] = pair[1]
    return fuel


def fn(fuel):
    return [fuel[:1], int(fuel[1:])]


def do_ucs():
    # f = open('../Sample/sample-input.txt')
    f = open('Sample/sample-input.txt')
    # f = open('../Sample/test-input.txt')
    original_stdout = sys.stdout
    count = 0
    for line in f:
        if line[0] == '#' or line[0] == "\n":
            continue
        input_received = line.strip().split(" ")
        count = count + 1
        board_input = input_received[0]
        fuel_dict = parse_fuel(input_received[1:])
        # output_solution_file = "../output_files/ucs-solution-" + str(count) + ".txt"
        output_solution_file = "output_files/ucs-solution-" + str(count) + ".txt"
        f_sol = open(output_solution_file, "w")
        sys.stdout = f_sol
        UCS(Board(board_input, fuel_dict, None, line), count).search()
        Board.io_is_done_flag = False
        sys.stdout = original_stdout


do_ucs()
