#!/usr/bin/env python3
"""
ClippedEmpire - Twitch to TikTok Converter

Automatically downloads top Twitch clips from any channel
and converts them for TikTok.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Only need Client ID for public clip fetching
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET = os.getenv('TWITCH_CLIENT_SECRET')

def main():
    print("="*50)
    print("Welcome to ClippedEmpire!")
    print("="*50)
    print()

    if not TWITCH_CLIENT_ID or not TWITCH_CLIENT_SECRET:
        print("ERROR: Twitch App credentials not found!")
        print("Please add TWITCH_CLIENT_ID and TWITCH_CLIENT_SECRET to your .env file")
        return

    print("✓ Credentials loaded!")

if __name__ == '__main__':
    main()
