inp = input()
try:
  inp = int(inp)
expect:
  pass
if type(inp) is str:
  print('Invalid Input')
else:
  if inp > 0:
    print('Positive')
  elif inp<0:
    print('Negative')
  else:
    print('Zero')
