#!/usr/bin/env python3
"""
ClippedEmpire - Twitch to TikTok Converter

This is the main file for the ClippedEmpire project.
It will automatically download Twitch clips and convert them to TikTok videos.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Twitch credentials
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_ACCESS_TOKEN = os.getenv('TWITCH_ACCESS_TOKEN')

def main():
    """
    Main function - this runs when you start the program
    """
    print("="*50)
    print("Welcome to ClippedEmpire!")
    print("="*50)
    print()
    
    # Check if credentials are set
    if not TWITCH_CLIENT_ID or not TWITCH_ACCESS_TOKEN:
        print("ERROR: Twitch credentials not found!")
        print("Please create a .env file with your credentials.")
        print("See README.md for instructions.")
        return
    
    print("✓ Twitch credentials loaded successfully!")
    print()
    print("Next steps:")
    print("1. Add code to fetch Twitch clips")
    print("2. Add code to download videos")
    print("3. Add code to reformat for TikTok")
    print("4. Add code to upload to TikTok")
    print()
    print("Good luck with your project!")

if __name__ == '__main__':
    main()
