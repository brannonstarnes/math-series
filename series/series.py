def fibonacci(n):
    """
    fibonacci(n) -> return nth degree of the fibonacci sequence(0,1,1,2,3,5,8, etc)

    """

    if isinstance(n, int) == False:
      return "Invalid input"
    if n < 0:
      return "Invalid input"
    elif n <= 1:
      return n
    elif n > 1:
      return fibonacci(n-1) + fibonacci(n-2)
    else:
      return "Invalid input"
    pass


def lucas(n):

  """
  lucas -> same as fibonacci sequence, but starts with 2,1 (ie 2,1,3,4,7,11,etc)
  """
    if n == 0:
      return 2
    elif n == 1:
      return 1
    elif n > 1:
      return lucas(n-1) + lucas(n-2)
    else: 
      return "Invalid input"
    pass


def sum_series(n, position0= 0, position1= 1):
    """
    n = degree of recursion starting from 0, position0(optional) = starting number, position1(optional) = second number. (ie sum_series(3,4,6) -> returns 16 (see 4,6,10,16)
    """
    if position0 == 0 and position1 == 1:
      return fibonacci(n)
    elif position0 == 2 and position1 == 1:
      return lucas(n)
    else:
      if n == 0:
        return position0
      elif n == 1:
        return position1
      else:
        return sum_series(n-1, position0, position1) + sum_series(n-2, position0, position1)

