from PIL import Image
from io import StringIO

image = Image.open("fish.jpg")
data = image.load()

ppm_file = StringIO()
ppm_file.write("P3\n")
ppm_file.write(str(image.width) + " ")
ppm_file.write(str(image.height) + "\n")
ppm_file.write("255\n")

for y in range(image.height):
  for x in range(image.width):
    pixel = data[x,y]
    ppm_file.write(f"{pixel[0]} {pixel[1]} {pixel[2]} ")
  ppm_file.write("\n")



with open("out.ppm", "w") as text_file:
  text_file.write(ppm_file.getvalue())

ppm_values = ppm_file.getvalue().split()

index = 0

front = ppm_values[index]
index += 1
assert front == "P3"

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
