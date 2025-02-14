#!/bin/bash

mpv /dev/video0
mpv ~/Music/angryhiphop.m4a

# Ask for the output file name
echo "Enter the name for your recording (without extension): "
read FILENAME

# Define the output file path
OUTPUT_FILE="$HOME/Videos/recordings/$FILENAME.mp4"

# Create the recordings directory if it doesn't exist
mkdir -p "$HOME/Videos/recordings"

# Start recording with wf-recorder
# Capture both desktop and Elgato Wave Neo microphone
wf-recorder -f "$OUTPUT_FILE" \
            --audio-file="$HOME/Videos/recordings/$FILENAME-audio.wav" \
            --device "alsa_input.usb-Elgato_Wave_Neo-00.analog-stereo"

