import argparse

parser = argparse.ArgumentParser(
    description='Welcome to Argparse',
    add_help=True
)
parser.add_argument(
        '-i',
        action='store',
        dest='input',
        help='input a name',
        default='Matt'
)


def mycustomfunct(name):
    """
    takes variable "name" and adds it to a list
    """
    a = [name]
    return a


def main():
    """
    only used when called locally
    """
    args = parser.parse_args()
    input_name = args.input
    this = mycustomfunct(input_name)
    print(this)


if __name__ == "__main__":
    """
    when calling this script locally, run main()
    """
    main()

