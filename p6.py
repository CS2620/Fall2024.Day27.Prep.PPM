from PIL import Image

image = Image.open("cookies.jpg")
data = image.load()

ppm_file = bytearray()
ppm_file += bytearray(b"P6\n")
ppm_file += bytearray(str(image.width).encode())
ppm_file += b" "
ppm_file += bytearray(str(image.height).encode())
ppm_file += b" "
ppm_file+= bytearray(b"255\n")

for y in range(image.height):
  for x in range(image.width):
    pixel = data[x,y]
    ppm_file.append(pixel[0])
    ppm_file.append(pixel[1])
    ppm_file.append(pixel[2])

with open("out.ppm", "wb") as text_file:
  text_file.write(ppm_file)


index = 0
assert chr(ppm_file[index]) == "P"
index += 1
assert chr(ppm_file[index]) == "6"
index +=1 
assert chr(ppm_file[index]).isspace()
index += 1

#Get width
buffer = []
while  chr(ppm_file[index]).isspace() is False:
  buffer += chr(ppm_file[index])
  index += 1

width = int("".join(buffer))
print(width)

# Move forward one since we found whitespace
index+=1

#Get height
buffer = []
while chr(ppm_file[index]).isspace() is False:
  buffer += chr(ppm_file[index])
  index += 1
height = int("".join(buffer))
print(height)

# Move forward one since we found whitespace
index+=1

#Get size
buffer = []
while chr(ppm_file[index]).isspace() is False:
  buffer += chr(ppm_file[index])
  index += 1
size = int("".join(buffer))
print(size)

# Move forward one since we found whitespace
index+=1

# Now read each byte
image_out = Image.new("RGB", (width, height))
data_out = image_out.load()


for y in range(height):
  for x in range(width):
    r = int(ppm_file[index])
    g = int(ppm_file[index+1])
    b = int(ppm_file[index+2])
    index += 3
    data_out[x,y] = (r,g,b)

image_out.save("done.png")

