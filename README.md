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

## Day 12
I read the problem statement, and thought to my self, "Ah, Dijkstra!". Well, I was wrong. While Dijkstra worked perfectly for part 1, it failed me on part 2. Python does not have a priority queue available, so the implementation was not as efficient as it could have been. I searched for all-source algorithms and implemented Floyd-Warshall, which was again stupid, because it runs in cubic time.
What is the correct algorithm then? Breadth-first search. It only needs linear (or quadratic in a strongly connected graph) time. The reason it works is simply that the edges don't have weights. Using Dijkstra or Floyd-Warshall to find all-source shortest paths in an *unweighted* graph is like using a sledgehammer to crack a nut!

**Time complexity:** $\mathcal O((RC)^2)$, where $R$ and $C$ are the number of rows and columns, respectively.

## Day 13
Quite a wild ride. Gave up on this puzzle after an hour or so, because it would run fine on the test input but the answer for the actual input was still wrong. Turned out that simply writing `a = [a]` in the compare function was not such a good idea, because this actually changes the list in the puzzle input as well, i.e. later computations will be wrong.

Also, surprisingly, my part 2 answer was correct, even though the code contained two mistakes. The algorithm was wrong but it happened to work on my input (not the test input, though).

## Day 24
Nice problem. I've never solved a graph traversal problem with a changing graph. My first instinct was to use DP, which worked for the test input, but was too slow for the actual input. BFS works much better: the key observation is that the player's behaviour has no impact on the structure of the graph, only time. Hence, one can just "expand" the graph to a time dimension, i.e. the nodes are of the form $(r,c,t)$ and there is an edge $(r,c,t) \to (r',c',t')$ if, and only if, $t' = t+1$ and $(r',c')$ is a passable neighbor of $(r,c)$ at time $t+1$.

The other observation is that the evolution of the blizzards is periodic with period less than or equal to the grid size (ignoring walls)*, so that the graph described above is finite. It has $((R-2)\cdot(C-2))^2 = \mathcal O((RC)^2)$ vertices with each one having at most $5$ outgoing edges (4 directions + wait). Hence, the overall time complexity is $\mathcal O(|V| + |E|) = \mathcal O((RC)^2)$.

\*The period is in fact $lcm(R-2,C-2)$.

## Learned lessons
* BFS is far more applicable than I thought
* algorithm choice heuristics for shortest path problems
    * if the edges are unweighted and you have only ONE start or ONE goal, use BFS ($n^2$); same scenario with (non-negative) weighted edges: Dijkstra ($n^2$); otherwise: Floyd-Warshall ($n^3$)
    * whenever you care about the FASTEST or FIRST way of reaching some goal, BFS is better than DFS, as you won't have to traverse all nodes
    * if the behavior of the player alters the environment, use DP
* DP is just a (variant of) DFS over the state graph
    * BFS would also work in theory, but the recursive nature of DFS is much nicer to comprehend and implement
* write helper functions for grids, as well as a ``memoize`` function (see ``utils.py``)
* implement a priority queue or Fibonacci heap for Dijkstra's algorithm

## Python's complexity
A good reference for containers: https://wiki.python.org/moin/TimeComplexity
* `len(x)` for some list (or even set) `x` is in $\mathcal O(1)$