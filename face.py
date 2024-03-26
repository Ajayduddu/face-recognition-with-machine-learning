import cv2
import os
import math
import time

# Function to calculate Euclidean distance between two images
def euclidean_distance(img1, img2):
    distance = 0
    min_height = min(img1.shape[0], img2.shape[0])
    min_width = min(img1.shape[1], img2.shape[1])

    for i in range(min_height):
        for j in range(min_width):
            distance += (img1[i][j]/255.0 - img2[i][j]/255.0)**2
    return math.sqrt(distance)

# Read the input image
input_img_path = "C:/Users/DELL/man_21.jpg"
input_img = cv2.imread(input_img_path, cv2.IMREAD_GRAYSCALE)

# Check if the input image was read successfully
if input_img is None:
    print("Error: Unable to read the input image.")
    exit(1)

# Create a list to store the images in the folder
images = []

# Read all the images in the folder
folder = "C:/Users/DELL/faces/"
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
    if img is not None:
        images.append(img)

# Normalize the pixel values of the input image
input_img = input_img / 255.0

# Calculate the Euclidean distance between the input image and each image in the folder
distances = []
for img in images:
    img = img / 255.0
    distance = euclidean_distance(input_img, img)
    distances.append(distance)

# Find the index of the closest match
index = distances.index(min(distances))

# Display the closest match
if index < len(images):
    start_time = time.time()
    cv2.imshow("Closest match", images[index])
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    end_time = time.time()

    
else:
    print("Error: No closest match found.")

# Calculate and print the time taken to iterate through the folder
start_time = time.time()
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename), cv2.IMREAD_GRAYSCALE)
    # Your image processing or comparison code here
end_time = time.time()

print("Time taken to iterate through folder:", end_time - start_time, "seconds")
