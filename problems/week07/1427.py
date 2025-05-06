import sys

numbers = sys.stdin.readline().strip()

sorted_data = sorted(numbers, reverse=True)

print(''.join(sorted_data))