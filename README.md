# Real-time-Face-Detection-and-Recognition-System
The "Real-time Face Detection and Recognition System" is a project that combines computer vision techniques to detect and recognize faces in real-time. The system utilizes the OpenCV library for image processing, face detection, and face recognition tasks.

The project consists of several components. First, there is a script called "prise.py" that captures images from a camera feed. It uses the Haar cascade classifier, implemented in OpenCV, to detect faces in the captured images. Then, it applies face recognition using a pre-trained model.

The "detector.py" script is responsible for real-time face detection. It continuously captures frames from the camera, applies the Haar cascade classifier to detect faces, and performs face recognition using a pre-trained model loaded from "trainingData.yml". Detected faces are highlighted with bounding boxes, and their identities are displayed on the screen.

The "apprentissage.py" script is used for training the face recognition model. It reads a dataset of labeled face images, extracts the faces using Haar cascade detection, assigns unique identifiers to each face, and trains the LBPH (Local Binary Patterns Histograms) face recognizer. The trained model is then saved to "trainingData.yml" for later use in face recognition.

Overall, this project provides a real-time face detection and recognition system that can be used for various applications, such as access control, surveillance, and personalized user experiences. It leverages computer vision techniques and the OpenCV library to achieve accurate and efficient face detection and recognition capabilities.
