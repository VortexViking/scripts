#!/bin/bash

# Ask for the recording name
echo "Enter the recording name (without extension):"
read RECORDING_NAME

# Check if the user provided a name
if [ -z "$RECORDING_NAME" ]; then
  echo "You must provide a name for the recording!"
  exit 1
fi

# Run ffmpeg to record screen, desktop audio, and mic
ffmpeg -f x11grab -i :0.0 -f alsa -i hw:0 -f alsa -i hw:2 -acodec aac -vcodec libx264 -preset fast -crf 23 -y "$RECORDING_NAME.mkv"

echo "Recording saved as $RECORDING_NAME.mkv"
