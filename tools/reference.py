#!/usr/bin/env python3
"""Independent Python check of langton.lz: a set of black cells, complex-number headings.

    python3 tools/reference.py run [--steps=200 --brief]
    python3 tools/reference.py highway
"""
import sys


def walk(steps):
    black, pos, heading = set(), 0j, -1j            # y grows downwards, so "up" is -1j
    xs, ys = [0], [0]
    lo, hi = [0, 0], [0, 0]
    for _ in range(steps):
        if pos in black:
            heading *= -1j                                                                # left turn (y grows downwards)
            black.discard(pos)
        else:
            heading *= 1j                                                                 # right turn: up (-1j) becomes right (1)
            black.add(pos)
        pos += heading
        lo = [min(lo[0], int(pos.real)), min(lo[1], int(pos.imag))]
        hi = [max(hi[0], int(pos.real)), max(hi[1], int(pos.imag))]
    return pos, heading, black, lo, hi


NAMES = {-1j: "up", 1: "right", 1j: "down", -1: "left"}

if __name__ == "__main__":
    if sys.argv[1] == "run":
        steps, brief = 200, False
        for a in sys.argv[2:]:
            if a == "--brief":
                brief = True
            else:
                steps = int(a.split("=")[1])
        pos, heading, black, lo, hi = walk(steps)
        w, h = hi[0] - lo[0] + 1, hi[1] - lo[1] + 1
        print("%d steps: ant at (%d, %d) facing %s; %d black cells" % (steps, pos.real, pos.imag, NAMES[heading], len(black)))
        print("the ant has wandered over an area %d wide and %d high" % (w, h))
        if not brief and w <= 100 and h <= 60:
            print("")
            for y in range(lo[1], hi[1] + 1):
                print("".join("@" if complex(x, y) == pos else ("#" if complex(x, y) in black else ".") for x in range(lo[0], hi[0] + 1)))
    else:
        # A different definition of "the highway": simulate to 14000 and find the earliest step from which every later
        # 104-step displacement (to the end of the run) is (+-2, +-2).
        black, pos, heading, path = set(), 0j, -1j, []
        for _ in range(14000):
            path.append(pos)
            if pos in black:
                heading *= -1j
                black.discard(pos)
            else:
                heading *= 1j
                black.add(pos)
            pos += heading
        path.append(pos)
        ok = [abs((path[i + 104] - path[i]).real) == 2 and abs((path[i + 104] - path[i]).imag) == 2 for i in range(len(path) - 104)]
        start = len(ok)
        while start > 0 and ok[start - 1]:
            start -= 1
        d = path[start + 104] - path[start]
        print("the highway begins at step %d" % start)
        print("from there the ant repeats a 104-step cycle, moving (%d, %d) each time" % (d.real, d.imag))
