#!/bin/sh
# Whole outputs (including the drawn grids) against tools/reference.py. The highway start is found there with a different
# definition: the earliest step after which EVERY later 104-step displacement is diagonal.
ok=0; bad=0
same() { if [ "$1" = "$2" ]; then ok=$((ok+1)); else bad=$((bad+1)); echo "DIFFERENT: $3"; fi; }
for n in 0 1 2 3 4 5 8 11 50 100 200 500 1000 2500 5000 9000 10000 11000 12345 20000 30000; do
  same "$($LZ run --steps=$n)" "$(python3 tools/reference.py run --steps=$n)" "run --steps=$n"
done
same "$($LZ run --steps=11000 --brief)" "$(python3 tools/reference.py run --steps=11000 --brief)" "run --brief"
same "$($LZ highway)" "$(python3 tools/reference.py highway)" "highway"
echo "$ok outputs identical to the reference, $bad different"
