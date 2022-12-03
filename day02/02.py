input = open("02.in").read().split('\n')

def part1():
    same = [('A','X'),('B','Y'),('C','Z')]
    
    win = {
        'A':'Y',
        'B':'Z',
        'C':'X'
    }

    score = 0
    for line in input:
        opp,me = line.split()
        score += ord(me) - ord('X') + 1
        if (opp,me) in same: # draw
            score += 3
        elif me == win[opp]:
            score += 6
    print("Part 1:", score)

def part2():
    win = {
        'A':'B',
        'B':'C',
        'C':'A'
    }

    lose = {
        'A':'C',
        'B':'A',
        'C':'B'
    }

    score = 0
    for line in input:
        opp,outcome = line.split()
        if outcome == 'X': # lose
            me = lose[opp]
        elif outcome == 'Y': # draw
            me = opp
            score += 3
        elif outcome == 'Z': # win
            me = win[opp]
            score += 6
        score += ord(me) - ord('A') + 1 # move score
    print("Part 2:", score)

part1()
part2()