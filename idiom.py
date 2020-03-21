import sys
from src.match import match_by_option


def parse_args(args):
    options = ['-e', '-t', '-v', '-h']
    option_flags = {opt:False for opt in options}
    for opt in args[1:-1]:
        assert opt in options
        option_flags[opt] = True
    hetero_flag = option_flags['-h']
    assert sum([option_flags[opt] for opt in options[:-1]]) == 1
    assert not (hetero_flag and option_flags['-e'])
    for opt in options[:-1]:
        if option_flags[opt]:
            mode = opt
    return mode, hetero_flag, args[-1]


def main():
    match_mode, hetero_flag, target = parse_args(sys.argv)
    results = match_by_option(match_mode, hetero_flag, target)
    if len(results):
        print('Results found:', *results, sep='\n  ')
    else:
        print("You're fucked. Try other options (e.g., -v -h).")
    

if __name__ == '__main__':
    main()