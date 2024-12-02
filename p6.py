from PIL import Image
from io import StringIO

image = Image.open("debug.png")
data = image.load()

ppm_file = bytearray()
ppm_file += bytearray("P6\n".encode("utf-8"))
ppm_file += bytearray((str(image.width) + " ").encode("utf-8"))
ppm_file += bytearray((str(image.height) + " ").encode("utf-8"))
ppm_file+= bytearray(("255\n").encode("utf-8"))

for y in range(image.height):
  for x in range(image.width):
    pixel = data[x,y]
    r = chr(pixel[0])
    g = chr(pixel[0])
    b = chr(pixel[0])
    ppm_file.append(pixel[0])
    ppm_file.append(pixel[1])
    ppm_file.append(pixel[2])



with open("out.ppm", "wb") as text_file:
  text_file.write(ppm_file)

quit()

ppm_values = ppm_file.getvalue().split()

index = 0

front = ppm_values[index]
index += 1
assert front == "P6"

width = int(ppm_values[index])
index += 1
height = int(ppm_values[index])
index += 1
_ = ppm_values[index]
index += 1

print(width)
print(height)

image_out = Image.new("RGB", (width, height))
data_out = image_out.load()

for y in range(height):
  for x in range(width):
    if x == 370 and y == 200:
      pass
    r = int(ppm_values[index])
    index += 1
    g = int(ppm_values[index])
    index += 1
    b = int(ppm_values[index])
    index += 1

    pixel = (r, g, b)
    data_out[x,y] = pixel

image_out.save("fish.png")
