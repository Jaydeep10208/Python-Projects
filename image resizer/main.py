import cv2

# Read the image
src = cv2.imread("hero_image.jpg", cv2.IMREAD_UNCHANGED)

# Display the original image
# cv2.imshow("title", src)

# Percent by which the image is resized
scale_percent = 50

# Calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# Resize image
output = cv2.resize(src, dsize)

# Save the resized image
cv2.imwrite('newimage.png', output)

# Wait for a key press and close the window
cv2.waitKey(0)

