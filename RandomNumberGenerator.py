"""
This Python program generates a random 6-digit passcode.

Author: Jose Ortiz
Date: 2024-10-03
"""

import random

def generate_passcode():
  """Generates a random 6-digit passcode."""
  return str(random.randint(0, 999999)).zfill(6)

# Generate and print a random passcode
passcode = generate_passcode()
print("Your random passcode is:", passcode)