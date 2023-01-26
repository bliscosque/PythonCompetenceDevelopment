import math

def isOn(S, j):
    return (S & (1<<j))

def setBit(S, j):
    return (S | (1<<j))

def clearBit(S, j):
    return (S & (~(1<<j)))

def toggleBit(S, j):
    return (S ^ (1<<j))

def lowBit(S):
    return (S&(-S))

def setAll(n):
    return ((1<<n)-1)

def modulo(S, N): # returns S % N, where N is a power of 2
    return ((S) & (N-1))

def isPowerOfTwo(S):
    return (not(S & (S - 1))) # 16&15=0 (10000 & 01111 = 00000)

def nearestPowerOfTwo(S):
    return 1<<round(math.log2(S))

def turnOffLastBit(S):
    return (S & (S - 1)) # 9&8 = 1001 & 1000 = 1000

def turnOnLastZero(S):
    return ((S) | (S + 1))

def turnOffLastConsecutiveBits(S):
    return ((S) & (S + 1))

def turnOnLastConsecutiveZeroes(S):
    return ((S) | (S-1))


def printSet(vS):           # in binary representation
    print(f"S = {vS} = {vS:b}")

def fastExpo(i,n):
    ans=1
    while n>0:
        last_bit=n&1
        if last_bit: ans*=i
        i*=i
        n=n>>1
    return ans


def main():
    print("0. Most basic - AND/OR/XOR")
    print(f"5&7: {5 & 7}") # 0101 & 0111 = 0101
    print(f"5|8: {5 | 8}") # 0101 | 1000 = 1101
    print(f"5^7: {5 ^ 7}") # 0101 ^ 0111 = 0010 (XOR)
    print(f"~0: {~0}") # ~0 = -1 (a inversao de um numero é ~num+1 = complemento de 2)
    print()
    
    print("1. Representation (all indexing are 0-based and counted from right)")
    S = 34
    printSet(S)
    print()

    print("2. Multiply S by 2, then divide S by 4 (2x2), then by 2")
    S = 34
    printSet(S)
    S = S << 1
    printSet(S)
    S = S >> 2
    printSet(S)
    S = S >> 1
    printSet(S)
    print()


    print("3. Set/turn on the 3-rd item of the set")
    S = 34
    printSet(S)
    S = setBit(S, 3)
    printSet(S)
    print()

    print("4. Check if the 3-rd and then 2-nd item of the set is on?")
    S = 42
    printSet(S)
    T = isOn(S, 3)
    print(f"T = {T}, {'ON' if T else 'OFF'}")
    T = isOn(S, 2)
    print(f"T = {T}, {'ON' if T else 'OFF'}")
    print()

    print("5. Clear/turn off the 1-st item of the set")
    S = 42
    printSet(S)
    S = clearBit(S, 1)
    printSet(S)
    print()

    print("6. Toggle the 2-nd item and then 3-rd item of the set")
    S = 40
    printSet(S)
    S = toggleBit(S, 2)
    printSet(S)
    S = toggleBit(S, 3)
    printSet(S)
    print()

    print("7. Check the first bit from right that is on")
    S = 40
    printSet(S)
    T = lowBit(S)
    print(f"T = {T} (this is always a power of 2)")
    S = 52
    printSet(S)
    T = lowBit(S)
    print(f"T = {T} (this is always a power of 2)")
    print();

    print("8. Turn on all bits in a set of size n = 6")
    S = setAll(6)
    printSet(S)
    print()

    print("9. Other tricks (not shown in the book)")
    print("8 % 4 = {}".format(modulo(8, 4)))
    print("7 % 4 = {}".format(modulo(7, 4)))
    print("6 % 4 = {}".format(modulo(6, 4)))
    print("5 % 4 = {}".format(modulo(5, 4)))
    print(f"is {9} power of two? {isPowerOfTwo(9)}")
    print(f"is {8} power of two? {isPowerOfTwo(8)}")
    print(f"is {7} power of two? {isPowerOfTwo(7)}")
    for i in range(1, 17):
        print("Nearest power of two of {} is {}".format(i, nearestPowerOfTwo(i)))
    print("S = {}, turn off last bit in S, S = {}".format(40, turnOffLastBit(40)))
    print("S = {}, turn on last zero in S, S = {}".format(41, turnOnLastZero(41)))
    print("S = {}, turn off last consecutive bits in S, S = {}".format(39, turnOffLastConsecutiveBits(39)))
    print("S = {}, turn on last consecutive zeroes in S, S = {}".format(36, turnOnLastConsecutiveZeroes(36)))
    print()

    print("10. Fast exponentiation")
    print(f"fastExpo(3,5): {fastExpo(3,5)}")

    print("11. Count bits in python")
    n=11
    print(f"{n} has {n.bit_count()} bits on")


main()