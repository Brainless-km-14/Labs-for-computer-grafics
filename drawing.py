from PIL import Image, ImageDraw
 
im = Image.new('RGB', (960, 540), (255, 255, 255))
draw = ImageDraw.Draw(im)
f = open('DS9.txt','r')
x=[]
y=[]
for line in f:
    line = line.split(" ")
    for i in range(len(line)):
        if i ==0:
            x.append(line[i])
        if i ==1:
            y.append(line[i])
for i in range(len(x)):
    draw.point(xy=(int(y[i]),int(x[i])), fill='black')
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show()
