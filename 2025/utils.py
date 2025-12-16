import argparse

def start(day, call_back_1, call_back_2):
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--part", required=True, choices=["1", "2"])
    parser.add_argument('-m', '--mode', required=True, choices=["simple", "input"])
    args = parser.parse_args()
    part, mode = args.part, args.mode

    inputs_folder = "inputs"
    filename = inputs_folder + "/" + mode + str(day)
    try:
        match part:
            case "1":
                call_back_1(filename)
            case "2":
                call_back_2(filename)
    except FileNotFoundError:
        print(f"File not found: {filename}")
