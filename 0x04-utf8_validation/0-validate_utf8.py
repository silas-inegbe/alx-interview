#!/usr/bin/python3

def validUTF8(data):
  index = 0
  while index < len(data):
    byte = data[index]
    
    # Check for 1 byte character
    if byte >> 7 == 0:
      index += 1 
      continue
    
    # Check for valid 2 byte character
    if index+1 >= len(data) or byte >> 5 != 0b110 or data[index+1] >> 6 != 0b10: 
      return False
    index += 2
    continue

    # Check for valid 3 byte character
    if index+2 >= len(data) or byte >> 4 != 0b1110 or data[index+1] >> 6 != 0b10 or data[index+2] >> 6 != 0b10:
      return False
    index += 3
    continue
    
    # Check for valid 4 byte character
    if index+3 >= len(data) or byte >> 3 != 0b11110 or data[index+1] >> 6 != 0b10 or data[index+2] >> 6 != 0b10 or data[index+3] >> 6 != 0b10:
      return False
    index += 4
    continue
    
  return True
