#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 input.flac output.wav"
  echo "Saves output to /audio/"
  exit 1
fi

input="$1"
output="./audio/$2"

ffmpeg -i "$input" -acodec pcm_s16le -ac 1 -ar 16000 "$output"
