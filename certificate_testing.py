import cv2
import os

# Parameters
point = (100, 595)
font_scale = 1.6
color = (255, 255, 255)
thickness = 2

# Load the original image
img_path = "participation.png"
img = cv2.imread(img_path)

# Ensure the output directory exists
output_dir = "certificate_sample"
os.makedirs(output_dir, exist_ok=True)

# Draw text with different fonts and save images
fonts = [
    (cv2.FONT_HERSHEY_SIMPLEX, "hershey_simplex.png"),
    (cv2.FONT_HERSHEY_PLAIN, "hershey_plain.png"),
    (cv2.FONT_HERSHEY_DUPLEX, "hershey_duplex.png"),
    (cv2.FONT_HERSHEY_COMPLEX, "hershey_complex.png"),
    (cv2.FONT_HERSHEY_TRIPLEX, "hershey_triplex.png"),
    (cv2.FONT_HERSHEY_COMPLEX_SMALL, "hershey_complex_small.png"),
    (cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, "hershey_script_simplex.png"),
    (cv2.FONT_HERSHEY_SCRIPT_COMPLEX, "hershey_script_complex.png"),
    (cv2.FONT_HERSHEY_SIMPLEX | cv2.FONT_ITALIC, "hershey_simplex_italics.png")
]

for font, filename in fonts:
    img_copy = img.copy()  # Copy the original image
    cv2.putText(img_copy, 'Srujan rai', point, font, font_scale, color, thickness, cv2.LINE_AA)
    cv2.imwrite(os.path.join(output_dir, filename), img_copy)

cv2.destroyAllWindows()
