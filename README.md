# Advent of Code 2022

Notation for time complexity: In general, $n$ denotes the number of input lines and, when needed, $\ell$ the length of the longest input. Usually, I just assume $\ell$ to be sensibly bounded, so that it can be ignored. Any other notation that's needed will be introduced for each day separately. At the very bottom are some useful things I've learned about Python by doing these complexity analyses.

## Day 01
This was just a basic problem. No special knowledge or algorithm was required.

**Time complexity:** $\mathcal O(n)$ for part 1 and $\mathcal O(n + k \log k)$ for part 2, where $k$ denotes the number of elves (i.e. input blocks separated by an empty line).

## Day 02
Another basic problem with a twist in the second part. Dictionaries come in handy here.

**Time complexity:** $\mathcal O(n)$ for both parts.

## Day 03
In principle a simple problem, but I ran into some problems and misunderstood something in the second part. I thought you were meant to also find the groups, i.e. look through all triples of Elves and see which of them have exactly one item in common. But it turned out that the groups were already given by the order of the input lines. This cost me a bunch of time.

**Time complexity:** $\mathcal O(n \cdot \ell^2)$ for both parts.
In the average case, this could actually be improved to $\mathcal O(n \cdot \ell)$ by using intersections to find the common items. (Note: I tried this, but the result is in fact slower for the inputs provided by the puzzle. This makes sense, as `intersection` probably has a larger overhead. When multiplying the lengths of the strings by 20, `intersection` starts becoming faster.)

## Day 04
Very simple problem that has you think about how to determine if sets of integers intersect without actually computing the intersection. Part 2 shouldn't have taken me as long as it did - while trying to avoid double counting, I accidentally counted too few overlaps! Part 1 went well, I even got rank 250, which is quite good, given my usual placing of 2000 and upwards.

**Time complexity:** $\mathcal O(n)$ for both parts.

## Day 05
A stack problem - although the stack part was quite simple compared to the input reading. It took me an embarrassing 10 minutes to parse the crate stacks correctly. I ended up transposing the first part of the input, in order to have each stack on one line. Then, a rogue `strip()` in the first line messed up the test input, causing me to be very confused and wasting even more time. Fun problem, though.

**Time complexity:** Let $s$ be the number of stacks, $h$ the height of the tallest stack in the beginning and $m$ the maximum amount of crates that are moved at once in any move. By the convention above, $n$ is the number of moves. Then, the time complexity for both parts is $\mathcal O(s \cdot h + n \cdot m)$. The $s\cdot h$ part comes from transposing the input. Fixing the number of stacks, assuming a somewhat even distribution of crates as well as number of crates moved at once, we can say that the algorithm is linear in the number of moves.

## Day 06
I was slightly disappointed by today's part 2. In terms of implementation, it was the exact same as part 1, except that you had to exchange a number. I barely made the leaderboard on part 1 and unfortunately didn't make it on part 2.

**Time complexity:** This time, there is no number of lines, so let $n$ be the length of the signal. Then the time complexity for both parts is $\mathcal O(n)$. If we let the scope (i.e. the value that was 4 respectively 14 in today's puzzle) be a variable as well, call it $s$, the complexity is $\mathcal O((n-s) \cdot s)$, implying that it should be slowest when $s \approx \frac{n}{2}$.

## Day 10
I didn't catch that the addx instruction takes two ticks instead of one. This cost me a bit of time. Overall though, my placement was quite good.

**Time complexity:** Nothing special, $\mathcal O(n)$.

## Python's complexity
A good reference for containers: https://wiki.python.org/moin/TimeComplexity
* `len(x)` for some list (or even set) `x` is in $\mathcal O(1)$