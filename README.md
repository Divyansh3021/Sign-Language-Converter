# Sign Language Converter

The Sign Language Converter is an application that aims to bridge the communication gap between individuals who use sign language and those who don't understand it. This application leverages computer vision and machine learning techniques to detect and interpret sign language gestures, converting them into text or spoken language.

## Features

- **Real-time Gesture Detection:** The application uses a webcam or camera input to capture live sign language gestures in real time.
- **Gesture Recognition:** Utilizing computer vision algorithms, the application analyzes the captured gestures and recognizes the corresponding sign language signs.
- **Translation:** The recognized sign language signs are converted into text or spoken language, allowing communication with non-sign language users.
- **Multi-language Support:** The converter supports various sign languages, enabling users to communicate using their preferred sign language.
- **User-friendly Interface:** The application provides an intuitive and easy-to-use interface for capturing, recognizing, and translating sign language gestures.

## System Requirements

- **Operating System:** The Sign Language Converter is compatible with Windows, macOS, and Linux.
- **Hardware Requirements:** The application requires a computer with a webcam or a camera connected for capturing sign language gestures.
- **Software Dependencies:** The following software dependencies must be installed on the system:
  - Python 3.x
  - OpenCV
  - TensorFlow
  - Keras
  - Other necessary libraries (requirements will be provided in the project documentation)

## Installation

To install and set up the Sign Language Converter, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/Divyansh3021/Sign-Language-Converter.git
   ```

2. Navigate to the project directory:

   ```shell
   cd sign-language-converter
   ```

3. Install the required dependencies. It is recommended to use a virtual environment:

   ```shell
   pip install -r requirements.txt
   ```

4. Run the application:

   ```shell
   python model.py
   ```

   Make sure your webcam or camera is connected and accessible.

## Usage

1. Launch the Sign Language Converter application by running `converter.py`.
2. Position yourself in front of the camera, ensuring that your hand gestures are clearly visible.
3. The application will start capturing the live video stream from the camera and display it on the screen.
4. Perform sign language gestures within the camera's field of view.
5. The application will detect and recognize the gestures, displaying the corresponding translated text on the screen.
6. If the application is configured to support spoken language output, it may also speak the translated text aloud.
7. Continue performing gestures to have them recognized and translated in real time.

## Contributing

Contributions to the Sign Language Converter project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch from the `main` branch.
3. Make your changes and enhancements in the new branch.
4. Test your changes thoroughly.
5. Create a pull request against the original repository's `main` branch.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code as per the license terms.

If you have any questions or need further assistance, please contact [your-name] at [your-email].
