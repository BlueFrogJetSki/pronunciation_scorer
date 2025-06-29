#!/usr/bin/env python3
# Prototype pronunciation scorer
# Requirements: pip install speechrecognition pronouncing python-Levenshtein pydub
import sys

from scorer import score

if __name__ == "__main__":  # usage: python scorer.py rabbit.wav "rabbit"
    s, tr = score(sys.argv[1], " ".join(sys.argv[2:]))
    print(f"Transcript: {tr}\nPronunciation score: {s:.2f}")
