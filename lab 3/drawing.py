from PIL import Image, ImageDraw

def rotate(A,B,C):
  return (B[0]-A[0])*(C[1]-B[1])-(B[1]-A[1])*(C[0]-B[0])

def Endrew(A):
    U, L = [], []

    for point in A:
      while (len(L) > 1 and rotate(point, L[-2], L[-1]) <= 0):
        L.pop()
      L += [point]

    for point in A[::-1]:
      while (len(U) > 1 and rotate(point, U[-2], U[-1]) <= 0):
        U.pop()
      U += [point]

    return L+U

def lst():
  f = open('DS9.txt','r')
  points=[]
  k=0
  for line in f:
    line = line.split(" ")
    points.append([])
    for i in range(len(line)):
      points[k].append(int(line[i]))
    k+=1
  f.close()
  return points

def convex_shell(B):
  x,y =[],[]
  for i in range(len(B)):
    x.append(B[i][0])
    y.append(B[i][1])
  return x,y

def points():
  f = open('DS9.txt','r')
  x,y =[],[]
  for line in f:
    line = line.split(" ")
    for i in range(len(line)):
        if i ==0:
            x.append(int(line[i]))
        if i ==1:
            y.append(int(line[i]))  
  f.close()
  return x,y

im = Image.new('RGB', (960, 540), (255, 255, 255))
draw = ImageDraw.Draw(im)

A = lst()
B = Endrew(A)
m,n =convex_shell(B)

x,y =points()

for i in range(len(x)):
    draw.point(xy=(y[i],x[i]), fill='black')

for i in range(len(n)-1):
    x = n[i:i+2]
    y = m[i:i+2]
    draw.line(xy=((x[0],y[0]),(x[1],y[1])), fill='blue',width =3)
    
im = im.transpose(Image.FLIP_TOP_BOTTOM)

im.show()
