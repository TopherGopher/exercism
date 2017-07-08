def is_leap_year(the_year):
  #on every year that is evenly divisible by 4
  if the_year % 4 == 0:
    #except every year that is evenly divisible by 100
    if the_year % 100 == 0:
      #unless the year is also evenly divisible by 400
      if the_year % 400 == 0:
        return True
      return False
    return True

  return False
