# Face Detection and Filter Application (OpenCV)

This project is a real-time webcam-based face detection and filtering application built using Python and OpenCV. It demonstrates how classic computer vision techniques can be used for interactive media applications.

---

## Features

- Real-time webcam feed processing
- Face detection using Haar cascade classifiers
- Multiple visual filters:
  - Grayscale
  - Gaussian Blur
  - Canny Edge Detection
  - Cartoon Effect
- Screenshot saving with applied filters
- Keyboard shortcuts for quick filter toggling

---

## Technologies Used

- Python 3.x
- OpenCV 4.x
- Haar cascade classifiers

---

## Project Structure


---

## How to Run

1. Install dependencies:

    ```bash
    pip install opencv-python
    ```

2. Run the script:

    ```bash
    python3 try.py
    ```

---

## Controls

| Key  | Action                      |
|------|-----------------------------|
| `g`  | Apply grayscale filter      |
| `b`  | Apply Gaussian blur filter  |
| `e`  | Apply edge detection filter |
| `c`  | Apply cartoon effect        |
| `n`  | Remove filter (normal view) |
| `s`  | Save screenshot             |
| `q`  | Quit application            |

---

## How It Works

### Face Detection

Face detection is performed using OpenCV’s pre-trained Haar cascade classifier `haarcascade_frontalface_default.xml`. Detected faces are marked with green rectangles in the video feed.

---

### Filters

- **Grayscale**: Converts the frame to black and white using `cv2.cvtColor()`.
- **Gaussian Blur**: Smooths the image using a Gaussian kernel with `cv2.GaussianBlur()`.
- **Edge Detection**: Applies the Canny edge detector (`cv2.Canny()`) to highlight strong gradients (edges).
- **Cartoon Effect**:
  1. Converts the image to grayscale.
  2. Applies a median blur to reduce noise.
  3. Detects edges using adaptive thresholding.
  4. Applies bilateral filtering to smooth colors while preserving edges.
  5. Combines color regions with detected edges to create a cartoon-like appearance.

---

## Why These Methods Were Chosen

| Task           | Method Used             | Why This Method?                                      | Alternatives                                  |
|----------------|--------------------------|--------------------------------------------------------|-----------------------------------------------|
| Face Detection | Haar Cascades            | Fast, easy to use, no GPU required                     | DNN-based detectors, YOLO, MTCNN              |
| Blur Filter    | Gaussian Blur            | Smooths quickly with less edge distortion              | Median Blur (preserves edges better, slower)  |
| Edge Detection | Canny                    | Effective and efficient edge detection                 | Sobel, Laplacian                              |
| Cartoon Effect | Adaptive Threshold + Bilateral Filter | Combines simplicity and performance          | Deep learning-based style transfer            |

---

## Expected Output

- The application opens a window titled `Filtered FaceCam`.
- Your webcam feed is displayed.
- Detected faces are outlined in green rectangles.
- Filters can be toggled in real time using the keyboard.
- Pressing `s` saves the current frame with the applied filter as `screenshot.png`.

---

## Extension Ideas

- Replace Haar cascade with DNN-based face detectors for better accuracy.
- Add age, gender, or emotion detection using pre-trained models.
- Implement a GUI for filter selection using PyQt or Tkinter.
- Add real-time style transfer using neural networks (e.g., Fast Neural Style Transfer).
- Allow custom filter creation using sliders for parameters like blur intensity, edge thresholds, etc.

---

## License

This project is open-source and available under the MIT [License](LICENSE).

---

## Author

**quasar-011**  
