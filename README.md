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

## Python's complexity
A good reference for containers: https://wiki.python.org/moin/TimeComplexity
* `len(x)` for some list (or even set) `x` is in $\mathcal O(1)$