import random
def programa2():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #last = len(quotes) - 1
  last=13
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  programa2()
