# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n is None:
        return False
    if n == 42:
        return True
    if n < 42:
        return False
    if n % 2 == 0 and bears(n/2):
        return True
    if n % 3 == 0 or n % 4 == 0:
        c = str(int(n))
        d = int(c[-2:-1]) * int(c[-1:])
        if d != 0 and bears(n - d):
            return True
    if n % 5 == 0 and bears(n-42):
        return True
    return False
