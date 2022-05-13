"""
>>> com([1,2,3])
[1, (1, 2), (1, 3)]
"""

def combine(e, l):
  c = []
  for a in l:
    c.append((e, a))
  return c


def com(l):
  if len(l) <= 1: return l
  else: return l[:1] + combine(l[0], l[1:])

