def solve(x):
    N = 1000_000_000

    found = None
    for y in range(1, N):
        if int(str(x) + str(y)) % (x + y) == 0:
            found = y
            break
    
    print(found)

if __name__ == '__main__':
    t = int(input())

    for i in range(1, t+1):
        n = int(input())
        solve(n)

"""
Had no idea on how to solve this one after analyzing the math.
I figured out that new number will be -
x*10^d + y, where d is number of digits in y.
And this number must be divisible by x + y.

But after this my math skills kind of betrayed me
and I was not able to do proceed.

Instead I rationilized the fraction by multiplying 
numerator and denominator with x - y and ended up getting nothing :)

Need more experience in solving divibility problems and related maths.
"""