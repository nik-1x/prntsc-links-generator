lets1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lets2 = lets1.lower()
ints = "01234567890"
pattern = lets2+ints
pattern_len = len(pattern)

print(pattern)
found = []

def genFromPattern(pat: str, xs: bytearray) -> str:
  f_str = ""
  for x in range(len(xs)):
    f_str += pat[xs[x]]
  return f_str


f = open("all_links.txt", "w")
for x1 in range(pattern_len):
  for x2 in range(pattern_len):
    for x3 in range(pattern_len):
      for x4 in range(pattern_len):
        for x5 in range(pattern_len):
          for x6 in range(pattern_len):
            generated = genFromPattern(pattern, [
              x1, x2, x3, x4, x5, x6
            ])
            print(generated)
            link = "prnt.sc/"+generated+"\r\n"
            f.write(link)
f.close()
