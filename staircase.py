def staircase(n):
    for _ in range(1, n + 1):
       print(' ' * (n - _) + '#' * _)
n = int(input())
staircase(n)
