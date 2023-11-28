# Hand Tracking Project

This project utilizes OpenCV and Mediapipe to perform real-time hand tracking using a webcam. It detects hand landmarks, extracts their positions, and displays them on the screen.

## Description

The program captures video from the webcam and processes it to identify hand landmarks. It converts the image to RGB format, runs it through the Mediapipe hands model, and draws landmarks on the screen. Additionally, it calculates and displays the frames per second (FPS) of the video stream.

## Usage

1. Clone this repository.
2. Install the necessary dependencies: OpenCV and Mediapipe.
3. Run the Python script `hand_tracking.py`.
4. Ensure that your webcam is properly connected and visible to the script.

## Features

- Real-time hand tracking from webcam feed.
- Detection and visualization of hand landmarks.
- Display of frames per second (FPS) for the video stream.

## Requirements

- Python 3.11.5
- OpenCV
- Mediapipe

## How to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make changes or enhancements.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.

## Credits

This project utilizes OpenCV and Mediapipe libraries for hand tracking.

## License

This project is licensed under the [MIT License](LICENSE).
