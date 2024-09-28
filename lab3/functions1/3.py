numheads = int(input())
numlegs = int(input())

def solve(numheads, numlegs):
    for ch in range(numheads + 1):
        rab = numheads - ch
        if ch * 2 + rab * 4 == numlegs:
            print(f"number of chicken is {ch}, number of rabbits is {rab}")
        
    return "No solution"

solve(numheads, numlegs)
