# PerceptionChallengeWA

![Answer Image](answer.png)

### Methodology
- **Objective**: The goal was to detect red cones in an image and fit two lines through the cones, one for each row of cones (left and right), and then save the output as `answer.png`.
  
- **Step-by-Step Process**:
  1. **Loading the Image**: The image `red.png` is read and processed using OpenCV's image processing functions.
  2. **Color Space Conversion**: The image is converted from the BGR color space to HSV (Hue, Saturation, Value). HSV is preferred for color detection as it separates the chromatic content (hue) from the intensity (value), making it easier to specify a range for the red cones.
  3. **Mask Creation for Red Detection**: Two masks are created to detect red cones, as red spans two ranges in the HSV color space. These masks are combined to capture all red objects in the image.
  4. **Contour Detection**: Contours of red objects are detected, which helps locate the cones by identifying the edges.
  5. **Filtering Contours**: Contours are filtered by size to eliminate noise and focus on the cones.
  6. **Centroid Calculation**: For each contour, the centroid is calculated. This is the average position of all the pixels inside the contour and is treated as the cone’s center.
  7. **Row Separation**: The centroids are separated into two rows based on their horizontal position (left or right) relative to the image’s center.
  8. **Line Fitting**: OpenCV’s `cv2.fitLine()` function is used to fit straight lines through the centroids of the left and right cones.
  9. **Line Drawing**: The fitted lines are extended and drawn on the image in red color.

### What Did You Try and Why Do You Think It Did Not Work
- **Initial Attempts**: 
  - I initially used `cv2.HoughLinesP` to detect lines, which worked but did not align well with the cones.
  - At first while lines appeared, HSV values changed the direction of the lines.
- **Current Approach**: 
  - The current method uses `cv2.fitLine()` to fit lines based on the cone centroids. While it generally works well, small adjustments were needed to accurately capture the alignment of cones, particularly on the left side.
  - **Tweaks Made**: The code was modified to adjust the parameters for contour area and line fitting to better align the drawn lines with the cone rows. I used trial and error to change HSV values that eventually led to the red lines aligning very closely with the red cones.

### 4. Libraries Used
- **OpenCV (`cv2`)**: Used for image loading, color space conversion, contour detection, line fitting, and drawing.
- **NumPy (`np`)**: Used for numerical operations like array manipulation and mathematical calculations, such as storing and processing cone centroids.
