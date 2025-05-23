import sys 

N, K = map(int, sys.stdin.readline().split()) # input() 보다 sys.stdin.readline()이 빠름
numbers = sys.stdin.readline().strip()

s = list()
count = K

for n in numbers:
    while len(s)!=0 and count != 0 and s[-1] < n:
        s.pop()
        count -= 1
    s.append(n)

print("".join(s[:N-K]))


''' <스택>
문제
N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

출력
입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다.
'''

# 숫자의 순서를 유지하면서 없앰
# N-K개의 숫자 // K만큼 빼면 됨
# 스택에 넣고 스택 값보다 크면 빼고 넣기