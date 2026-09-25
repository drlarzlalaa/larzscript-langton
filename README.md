# larzscript-langton

Langton's ant, written entirely in [Larzscript](https://larzos.com/larzos-linux/). An ant walks on an infinite grid of white cells. On a white cell it turns right, flips the cell to black and steps forward; on a black cell it turns left, flips it to white and steps forward. That is the whole rule.

```
larzscript langton.lz run [--steps=200 --brief]
larzscript langton.lz highway
```

`#` is black, `.` white, `@` the ant. After 500 steps it looks like a symmetric-ish blob:

```
500 steps: ant at (6, -4) facing down; 62 black cells
the ant has wandered over an area 13 wide and 13 high

..##....##...
.#..#....####
###.....###.@
#.####.#.#.#.
......#...#..
...##.#.###..
..#..##...#..
..#..#..##...
....##.......
.#.....####.#
.#.##.....###
..##....#..#.
...##....##..
```

For about 10,000 steps the pattern looks like chaos. Then the ant suddenly builds a diagonal **highway**, repeating a 104-step cycle for ever (it has not been proved that this always happens, but it does from an empty grid):

```
the highway begins at step 9976
from there the ant repeats a 104-step cycle, moving (-2, 2) each time
```

```
11000 steps: ant at (-34, 14) facing down; 834 black cells
the ant has wandered over an area 67 wide and 45 high
30000 steps: ant at (-402, 380) facing down; 3026 black cells
the ant has wandered over an area 433 wide and 403 high
```

## How it was checked

`tools/reference.py` is an independent Python implementation (a set of black cells and complex-number headings). `tests/crosscheck.sh` compares 23 whole outputs from 0 to 30000 steps, including every drawn picture; all identical. The highway start is found there with a *different definition* (the earliest step after which every later 104-step displacement is diagonal, to the end of a 14000-step run) and both give step 9976, matching the well-known figure of roughly 10,000 steps. (The very first comparison, on step 1, exposed a mirrored turn direction in my first draft of the reference; the Larzscript program was right.) `sh tests/run_tests.sh` needs Python 3 for that check. Zero dependencies apart from Larzscript's `cli` and `args` packages. MIT licensed.
