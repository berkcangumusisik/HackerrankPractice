# Problem: https://www.hackerrank.com/challenges/whats-your-name/problem
def print_full_name(first, last):
    print("Hello {} {}! You just delved into python.".format(first,last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
