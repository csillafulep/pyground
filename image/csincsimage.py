from skimage import data, io, filters, feature, color
import matplotlib.pyplot as plt

image = io.imread('image/lena.jpg')
grayImage = color.rgb2gray(image)
plt.figure(1)
edgesCanny = feature.canny(grayImage)
io.imshow(edgesCanny)

plt.figure(2)
edgesSobel = filters.sobel(grayImage)
io.imshow(edgesSobel)

io.show()