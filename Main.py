import time
import argparse

def print_hi(str1, str2, str3, str4):
    print('Hi')
    print(f'str 1 = {str1}')
    print(f'str 2 = {str2}')
    print(f'str 3 = {str3}')
    print(f'str 4 = {str4}')

    time.sleep(10)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parse some arguments', prefix_chars='-+')
    parser.add_argument('arg_1', type=str, help='positional arguments')
    parser.add_argument('--arg_2', type=str, help='optional arguments')
    parser.add_argument('-+arg_3', type=str, help='optional arguments and prefix -+')
    parser.add_argument('--arg_4', type=str, default='arg_four', help='optional arguments and def="arg_four"')
    parser.print_help()

    args = parser.parse_args()
    print_hi(args.arg_1, args.arg_2, args.arg_3, args.arg_4)