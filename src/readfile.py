import sys
from random import randint

import numpy as np
from board import Board
from ucs import UCS
from gbfs import GBFS
from a import A

import csv


def parse_fuel(fuel_input):
    fuel = {}
    parsed = list(map(fn, fuel_input))
    for pair in parsed:
        fuel[pair[0]] = pair[1]
    return fuel


def fn(fuel):
    return [fuel[:1], int(fuel[1:])]


def do_ucs(line, count):
    input_received = line.strip().split(" ")
    board_input = input_received[0]
    fuel_dict = parse_fuel(input_received[1:])
    output_solution_file = "../output_files/ucs-solution-" + str(count) + ".txt"
    # output_solution_file = "output_files/ucs-solution-" + str(count) + ".txt"
    f_sol = open(output_solution_file, "w")
    sys.stdout = f_sol
    data = UCS(Board(board_input, fuel_dict, None, line), count).search()
    Board.io_is_done_flag = False
    return data


def do_gbfs(line, count):
    input_received = line.strip().split(" ")
    board_input = input_received[0]
    fuel_dict = parse_fuel(input_received[1:])
    heuristic_list = ["h1", "h2", "h3", "h4"]
    data = []
    for heuristic in heuristic_list:
        # output_solution_file = "output_files/gbfs-" + heuristic + "-solution-" + str(count) + ".txt"
        output_solution_file = "../output_files/gbfs-" + heuristic + "-solution-" + str(count) + ".txt"
        f_sol = open(output_solution_file, "w")
        sys.stdout = f_sol
        data.append(GBFS(Board(board_input, fuel_dict, None, line), count, heuristic).search())
        Board.io_is_done_flag = False
    return data


def do_a(line, count):
    input_received = line.strip().split(" ")
    board_input = input_received[0]
    fuel_dict = parse_fuel(input_received[1:])
    heuristic_list = ["h1", "h2", "h3", "h4"]
    data = []
    for heuristic in heuristic_list:
        # output_solution_file = "output_files/gbfs-" + heuristic + "-solution-" + str(count) + ".txt"
        output_solution_file = "../output_files/a-" + heuristic + "-solution-" + str(count) + ".txt"
        f_sol = open(output_solution_file, "w")
        sys.stdout = f_sol
        data.append(A(Board(board_input, fuel_dict, None, line), count, heuristic).search())
        Board.io_is_done_flag = False
    return data


def randomize_fuels():
    f = open("../input_files/50_board_inputs.txt", "r")
    f_out = open("../input_files/50_board_inputs_with_fuels.txt", "w")
    for line in f:
        if line[0] == "#" or line[0] == "\n":
            f_out.write(line)
            continue
        add_fuel = randint(0, 100)
        if add_fuel < 51:
            f_out.write(line)
            continue
        line = line.strip()
        board = np.empty(shape=1*36, dtype=str)
        for char in range(0, len(line)):
            v = line[char]
            board = np.append(board, v)
        vehicles = np.unique(board)
        vehicles = vehicles[1:]
        fuels = []
        for elem in vehicles[1:]:
            fuels.append(elem + str(randint(0, 10)))
        fuel_line = ""
        for fuel in fuels:
            fuel_line = fuel_line + fuel + " "
        f_out.write(line + " " + fuel_line)

    f.close()


def run():
    original_stdout = sys.stdout
    count = 0
    # f = open('../Sample/sample-input.txt')
    # f = open('Sample/sample-input.txt')
    # f = open('../Sample/test-input.txt')
    # f = open("../input_files/50_board_inputs.txt")
    f = open("../input_files/50_board_inputs_with_fuels.txt")

    with open("../analysis/summary.csv", "w+", encoding="UTF8", newline="") as f_summary:
        csv_writer = csv.writer(f_summary)
        headers = ['Puzzle Number', 'Algorithm', 'Heuristic', 'Length of the Solution',
                   'Length of the Search Path', 'Execution Time (in seconds)']
        csv_writer.writerow(headers)

        for line in f:
            if line[0] == '#' or line[0] == "\n":
                continue
            count = count + 1
            csv_writer.writerow(do_ucs(line, count))
            gbfs_data = do_gbfs(line, count)
            for data in gbfs_data:
                csv_writer.writerow(data)

            a_data = do_a(line, count)
            for data in a_data:
                csv_writer.writerow(data)

    sys.stdout = original_stdout


randomize_fuels()
run()
