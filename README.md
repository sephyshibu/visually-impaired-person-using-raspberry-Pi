# visually-impaired-person-using-raspberry-Pi
Our proposed solution is defined as a portable device which is aiming at assisting visually
impaired people. The proposing system uses Raspberry pi, it is a small processing device.
The system is intended to provide artificial vision, object detection, face recognition, text
reading, real time assistance via making use of Raspberry Pi. Here we used Raspbian Op-
erating System within Raspberry Pi and have written code in Python language. The system
uses speech to text and text to speech for communicating with users. The embedded system
consists of camera module, GSM, headset, virtual assistant and contain various modules.

The proposed system consists of two parts:
• Virtual Assistant
• OpenCV
Virtual Assistant
Virtual Assistant can create interaction environment amonguser it seems natural, the user
communicates using theirvoice,and the virtual assistant responds in the same way.Thishelps
user to do daily activities independently. Virtual Assis-tant system basically means a system
where voice is taken asan input or understands the meaning of that input, processesit and
generates an appropriate audio output. Here we use two speak engines for converting speech
to text and text to speech.
• Speech Recognition
• gTTS
When the user wants to recognize object,face,text or do someonline search, it can be done
simply by speaking throughmicrophone.And the result is fed back to user in the form of
audio. It contain various modules like Wikipedia module, Wolfram Alpha module, Open-
Weathermap API.
OpenCV
This is the backend of our proposed system.This section will deals with
• Object Recognition
• Face Recognition and Detection
• Text Reading

Object Recognition
Visually impaired people need not to recognize objects.Thisdeals with identifying and ver-
ifying objects infront of the userthrough camera in real time.The camera capture the image
ofthe object and tells to the user in the form of audio.The objectis detected only if it is in
the local data set. The algorithm usedfor object detection in this paper is faster r-cnn (faster
regional-convolutional network).This algorithm finds all objects in animage with the help of
RPN (Region Proportion Network)
Face Recognition and Detection
A face recognition system is a computer application forautomatically identifying or verify-
ing a person from a digitalimage or a video frame.This module uses the camera to capturethe
images of the face of the person in front of the user.Thisis stored in the SD card within
Raspberry Pi.The capturedimage of the person is crosschecked with the previously stored-
faces,if a match is found, the name of the person is readout.If no match is found, a trainer
program is triggered andthe person’s face images are trained in real time.This is alsostored
in the SD card. All image capture and processing isdone with the help of OpenCV soft-
ware.HOG(Histogram ofOriented Gradients) and facial land mark estimation algorithmis
used in face recognition.
Text Reading
A technique used to detect the textual information availablein an image or any printed docu-
ments.It involves text recogni-tion and text detection.In text detection regions of image con-
taining text is detected and these text information is retrievedin the recognition stage.These
retrieved text is converted toaudio, which is fed to blind person via headset.This helps themto
know what text is in the image.The best tool for text recog-nition is OCR(Optical character
recognition).Python-tesseractor pytesseract is an OCR tool.It allows to recognise and read-
textual content in an image.When an image containing text isshown to camera, textual re-
gions coming under bounding boxis recognized by tesseract library.When asked, the OCR
andTTS engine act as a reader machine and read out it to the user.

System Requirements
Hardware Implementation
Hardware components used for this system are Raspberry pi, camera mounted on spec-
tacle, a power bank, GSM, headset. The camera on spectacle captures the image from the
frame. The captured images are sent to Raspberry Pi and all the image processing was done.
The voice output is via through headset.
1. Raspberry Pi 3 B+
Raspberry Pi 3 B+ is used, which is the latest variant of Raspberry Pi 3 model.It is a
mini computer which is credit card sized single board serves as foundation for various
core implementation of different projects.It is most suitable for every application such
as Voice assistant, Deep learning etc. The specification is Broadcom BCM2837 SoC
with a 1.2 GHz 64-bit quad-core ARM Cortex-A53 processor, with 512 KiB shared L2
cach.After all, Raspbian OS is installed, which contains basic programs and services
that helps the Raspberry Pi run.
2. Camera
Camera helps to feed real time video to Raspberry Pi where Open Source Computer
Vision analyzes the data.Camera is mount to the spectacle for image capturing
3. Power bank and headset
Power bank is used to make the system more compact and flexible.The headset serve as
a communication channel between user and Virtual assistant.It is interfaced with rasp-
berry pi.The query input from user is fed through the mic and the output is delivered
via headset.
4. Spectacle
The camera is mounted on spectacle for capturing the images .

Software Implementation
1. Raspbian Operating System
Raspbian being a free operating system based on Debian developed for the Raspberry
Pi module.Raspberry Pi OS (previously called Raspbian) is our official supported op-
erating system. The operating system is a set of basic programs and services that helps
the Raspberry Pi run. Many versions of Raspbian are available like Raspbian Stretch
and Raspbian Jessie. Raspberry Pi OS comes with over 35,000 packages: precompiled
software bundled in a nice format for easy installation on your Raspberry Pi.
2. Python Language
Python is a high-level programming language for general-purpose. It has been de-
signed in such a way that emphasizes code readability, notably using signicant whites-
pace. Python is an interpreted, high level, multi paradigm programming language,
object oriented programming and structured programming are fully supported. It pro-
vides a platform to constructs a clear programming stage on both small and large
scales. Python uses dynamic typing, and a combination of reference counting and
a cycle detecting garbage collector for memory management. It is meant to be an eas-
ily readable language. Its formatting is visually uncluttered, and it often uses English
keywords where other languages use punctuation.
3. OpenCV
OpenCV is an open source library for programs and functions mainly aimed at real-
time computer vision. It’s free for the users and the library is cross platform.The
has more than 2500 optimized algorithms, which includes a comprehensive set of both
classic and state-of-the-art computer vision and machine learning algorithms. OpenCV
supports the deep learning frameworks TensorFlow, OCR, face recognition,object de-
tection etc.

System Architecture
The implementation of system is explained, which will be useful for visually impaired
people and people with disability. The speech is used for communication for users, the
virtual assistant helps to search anything for users, read text with OCR tool, identify objects
and person near to user with help of object recognition module, face recognition module
respectively.
3.3.1 Text Detection
Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will
recognize and “read” the text embedded in images. OCR is a task that consists of extracting
text from images, hardcopy or scanned document. With the help of a digital camera the text
is recognized by Tesseract library. The text coming under bounding box will be recognized.
When we combine OCR and text to speech convertor when user ask to read then it act
function as reader machine of the document that we present in front of the camera.

Face Detection and Recognition
A facial recognition system helps in identifying and verifying a person in real time. The
face detection and recognition module uses the camera to capture the images of the face of
the person in front of the user. If the image of that person will crosschecked with dataset
provided, if match if found the corresponding name of the person is read out else a trainer
prograam will get triggered. This will help to train new image and added to the dataset.
3.3.3 Object Recognition
An object detection system helps to identify the objects in the real time.The camera
capture the image of the object and tells about to the user.The object is only identified if it
is in the data set.And if not,a trainer program is added,to train the object which is not in the
dataset.Once trained,it is saved and again if that object is captured by camera,it will easily
identified.
3.3.4 Virtual Assistant
It performs task given by voice command by users and give corresponding response to
the users via headset. Users can navigate the websites through voice commands. It also
provides the feature of providing answers to a particular question from a user using different
modules like:
1. Wikipedia module
The Wikipedia feature is invoked when the user responds to the speech recognition
with the word “Wikipedia”. The system redirects to a page which listens to the user
input through the voice. Once the system receives the input, it processes the user’s
query and fetches the information from Wikipedia and speak out via headset.
2. Wolfram Alpha module
Wolfram Alpha is a computational search engine that tends to evaluate what the user
asks. User’s input will be passed to Wolfram Alpha through voice commands for processing. If a result is obtained, the result will be speak out to the user.
3. OpenWeathermap API
The OpenWeathermap feature is invoked when the user responds to the speech recog-
nition with the word “Weather”. The system redirects to a page which listens to the
user input through the voice. Once the system receives the input, it processes the user’s
query and provides global weather data, including current weather data, forecasts, and
speak out via headset.
3.3.5 Speech Recognition Module
Normal speech to text conversion is done using speech recognition module which is a
STT system. This involves recording the user’s voice, capturing the words from the recording
(cancelling any noise), and then convert the recording to a text string.
3.3.6 gTTS Module
Here we use gTTS(Google Text to Speech) to convert text to audio format.The inputs
were given in text format. The output had clear voice.
Department of Computer Science and Engineering,AJCE 15

