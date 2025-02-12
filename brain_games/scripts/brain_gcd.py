#!/usr/bin/env python

from brain_games import engine
from brain_games.scripts.games import gcd


def main():
    engine.run(gcd)


if __name__ == "__main__":
    main()