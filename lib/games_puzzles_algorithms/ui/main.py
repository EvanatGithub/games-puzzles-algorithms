import argparse
from interface import Interface


def main():
    """
    Main function to get and respond to user input.
    """
    parser = argparse.ArgumentParser(
        description='Run the CMPUT 396 puzzles Currently sliding_tile and maze are defined.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--puzzle', type=str, default='maze', help='puzzle to run')
    parser.add_argument('--search', type=str, default='A*', help='search algorithm to use')

    args = parser.parse_args()
    interface = Interface(args.puzzle, args.search)
    interface.prompt = ">"
    interface.cmdloop()


if __name__ == "__main__":
    main()
