from string import ascii_lowercase

def is_isogram(word):
    temp_arr = []
    for c in word:
      if c.lower() in ascii_lowercase:
        if c.lower() in temp_arr:
          return False
        temp_arr.append(c.lower())

    return True