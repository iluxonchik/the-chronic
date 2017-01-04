from thechronic.thechronic import TheChronic

import argparse

def positive_int(value):
        MSG = 'Argument must be a positive integer.'
        try:
            arg = int(value)
            if arg > 0:
                return arg
            else:
                raise argparse.ArgumentTypeError(MSG)
        except ValueError:
            raise arparse.ArgumentTypeError(MSG)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate passwords by combining words from provided files(s)')
    parser.add_argument('--min', type=int, default=1, help='Minimum output word length.')
    parser.add_argument('--max', type=positive_int, default=None, help='Maximum output word length.')
    parser.add_argument('-n','--num_words', type=positive_int, default=1, help='Number of words to combine.')
    parser.add_argument('-f', '--files', nargs='*', default=[], help='File(s) to load the words from.')
    parser.add_argument('-b', '--no_build_up', action='store_true',
        default=False, help='Don\'t build up number of word combinations. '
        'This means that if you provide the value 3 for the \'-n\' argument, '
        'only words which are a combination of 3 words will be genrated, '
        'otherwise all words from combination of 1 to 3 words will be.')
    args = parser.parse_args()

    thechronic = TheChronic(files=args.files)
    build_up = not args.no_build_up
    res = thechronic.combine(num_words=args.num_words, build_up=build_up,
    min_length=args.min, max_length=args.max)

    ### TODO:
    ### If outputting to file, simpy do sys.stdout = open('file') and keep the
    ### print statement.

    for i in res:
        print(i)
