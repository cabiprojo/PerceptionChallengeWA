# import cv2 (OpenCV library) and numpy, a Python library for arrays and matricies
import cv2
import numpy as np

# load and read the image red.png
image = cv2.imread('red.png')

# convert the image to HSV (Hue, Saturation, Value) for better color detection
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define the color range for red 
lower_red1 = np.array([0, 100, 190])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 150, 100])
upper_red2 = np.array([100, 205, 255])

# create a mask to detect red color 
mask1 = cv2.inRange(hsv, lower_red1, upper_red1) # first red range
mask2 = cv2.inRange(hsv, lower_red2, upper_red2) # second red range
mask = cv2.bitwise_or(mask1, mask2) # combines the masks to detect all red areas

# find contours of the red cones
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# list to store the centroids of the cones
cone_centers = []

# filter contours and find the centroids of the red cones
for contour in contours:
    if cv2.contourArea(contour) > 100:  # filter out small noise
        # calculate the centroid of the contour
        M = cv2.moments(contour)
        if M["m00"] != 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])
            cone_centers.append([center_x, center_y])

# convert to numpy array for easier manipulation
cone_centers = np.array(cone_centers)

# dynamically calculate the horizontal midpoint of the image
image_center_x = image.shape[1] // 2

# separate the cones into two rows (left and right) based on their x-coordinate relative to the image center
left_cones = [pt for pt in cone_centers if pt[0] < image_center_x]
right_cones = [pt for pt in cone_centers if pt[0] >= image_center_x]

# fit a line for each row of cones (left and right)
def fit_and_draw_line(image, points, color):
    if len(points) > 1:
        # fit a line using cv2.fitLine
        line = cv2.fitLine(np.array(points), cv2.DIST_L2, 0, 0.01, 0.01)
        vx, vy, x0, y0 = line[0], line[1], line[2], line[3]

        # calculate two points to extend the line
        pt1 = (int(x0 - vx * 1000), int(y0 - vy * 1000))
        pt2 = (int(x0 + vx * 1000), int(y0 + vy * 1000))

        # draw the line on the image
        cv2.line(image, pt1, pt2, color, 3)

# draw the left and right lines (using red color for both)
fit_and_draw_line(image, left_cones, (0, 0, 255))  # left line in red
fit_and_draw_line(image, right_cones, (0, 0, 255))  # right line in red

# save the result with the two lines drawn
cv2.imwrite('answer.png', image)
