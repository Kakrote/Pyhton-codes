import face_recognition
from PIL import Image, ImageDraw

# Load the image with faces
image_path = "test_img.jpg"
image = face_recognition.load_image_file(image_path)

print(type(image), image.shape, image.ndim)
# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

print("Found {} face(s) in this photograph.".format(len(face_locations)))

# Load the image into a PIL Image object
pil_image = Image.fromarray(image)
print(type(pil_image))

# # Create a PIL drawing object topractice/test_img.jpg draw rectangles around the faces
# draw = ImageDraw.Draw(pil_image)

# # Loop through each face found in the image
# for face_location in face_locations:
#     # Print the location of each face in this image
#     top, right, bottom, left = face_location
#     print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

#     # Draw a box around the face using the Pillow module
#     draw.rectangle((left, top, right, bottom), outline="red")

# # Display the image with faces boxed
# pil_image.show()
