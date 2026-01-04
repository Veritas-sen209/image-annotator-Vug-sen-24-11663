import cv2
import math
from tkinter import Tk, filedialog, simpledialog

Tk().withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.png *.jpeg")]
)

image = cv2.imread(image_path)
points = []
mode = "line" 

def mouse_click(event, x, y, flags, param):
    global points, image, mode

    if event == cv2.EVENT_LBUTTONDOWN:

        # TEXT MODE
        if mode == "text":
            text = simpledialog.askstring("Input", "Enter text:")
            if text:
                cv2.putText(
                    image,
                    text,
                    (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 255),
                    2
                )

        else:
            points.append((x, y))
            cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

            # LINE (MEASURE)
            if mode == "line" and len(points) == 2:
                cv2.line(image, points[0], points[1], (255, 0, 0), 2)

                x1, y1 = points[0]
                x2, y2 = points[1]
                dist = int(math.sqrt((x2-x1)**2 + (y2-y1)**2))

                cv2.putText(
                    image,
                    f"{dist}px",
                    ((x1+x2)//2, (y1+y2)//2),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 0, 255),
                    2
                )
                points = []

            # RECTANGLE
            elif mode == "rect" and len(points) == 2:
                cv2.rectangle(image, points[0], points[1], (0, 0, 0), 2)
                points = []

            # CIRCLE
            elif mode == "circle" and len(points) == 2:
                center = points[0]
                edge = points[1]
                radius = int(math.sqrt((edge[0]-center[0])**2 + (edge[1]-center[1])**2))
                cv2.circle(image, center, radius, (255, 255, 0), 2)
                points = []

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_click)

print("""
Controls:
L - Line / Measure
R - Rectangle
C - Circle
T - Text
S - Save Image
ESC - Exit
""")

while True:
    cv2.imshow("Image", image)
    key = cv2.waitKey(1) & 0xFF

    if key == 27:
        break
    elif key == ord('l'):
        mode = "line"
        print("Mode: Line / Measure")
    elif key == ord('r'):
        mode = "rect"
        print("Mode: Rectangle")
    elif key == ord('c'):
        mode = "circle"
        print("Mode: Circle")
    elif key == ord('t'):
        mode = "text"
        print("Mode: Text")
    elif key == ord('s'):
        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
        )
        if save_path:
            cv2.imwrite(save_path, image)
            print("Image saved successfully!")

cv2.destroyAllWindows()
