from string import ascii_lowercase

def is_pangram(sentence):
    tmp_list = {}
    for c in sentence:
      if c.lower() in ascii_lowercase:
        if c not in tmp_list.keys():
          tmp_list[c] = 1
        else:
          tmp_list[c] += 1
    if len(tmp_list) == 26:
      return True
    else:
      return False

