

def hatchH(f):
  print("hatchH <=	'1' when (", file=f)
  print(f"\t\t\t\t\t\t(pixelVert > T_EDGE + BORDER_LINE_WIDTH + 295) and --Upper and lower bounds", file=f)
  print(f"\t\t\t\t\t\t(pixelVert < T_EDGE + BORDER_LINE_WIDTH + 305)", file=f)
  print(f"\t\t\t\t\t\t) and (", file=f)
  for i in range(1, 49):
    print(f"\t\t\t\t\t\t(pixelHorz = L_EDGE + BORDER_LINE_WIDTH + {20 * i}) or", file=f)
  print(f"\t\t\t\t\t\t(pixelHorz = L_EDGE + BORDER_LINE_WIDTH + 980) --Each individual hatch", file=f)
  print(f"\t\t\t\t\t\t)", file=f)
  print(f"\t\t\t\t\t\t else '0';", file=f)

def hatchV(f):
  print("hatchV <=	'1' when (", file=f)
  print(f"\t\t\t\t\t\t(pixelHorz > L_EDGE + BORDER_LINE_WIDTH + 495) and --Left and right bounds", file=f)
  print(f"\t\t\t\t\t\t(pixelHorz < L_EDGE + BORDER_LINE_WIDTH + 505)", file=f)
  print(f"\t\t\t\t\t\t) and (", file=f)
  for i in range(1, 49):
    print(f"\t\t\t\t\t\t(pixelVert = T_EDGE + BORDER_LINE_WIDTH + {12 * i}) or", file=f)
  print(f"\t\t\t\t\t\t(pixelVert = T_EDGE + BORDER_LINE_WIDTH + 588) --Each individual hatch", file=f)
  print(f"\t\t\t\t\t\t)", file=f)
  print(f"\t\t\t\t\t\t else '0';", file=f)
  
def gridH(f):

def gridV(f):

if __name__ == "__main__":
    with open("hatch.txt", "w") as f:
        hatchH(f)
        hatchV(f)

    with open("grid.txt", "w") as f:
        gridH(f)
        gridV(f)