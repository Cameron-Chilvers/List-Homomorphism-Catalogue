import functools

def foldl(func, acc, xs):
  return functools.reduce(func, xs, acc)

# Right fold implementation using recursion as we use many elements
def foldr(func, acc, xs):
    if not xs:
        return acc
    return func(xs[0], foldr(func, acc, xs[1:]))