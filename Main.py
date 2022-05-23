import speech_recognition as sr
import cv2
import time
import face_recognition
from gtts import gTTS
import playsound
import sys
import email
import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = "smtp.gmail.com"
sender_email = "SecurifyProtect@gmail.com"
receiver_email = "dripppypapi@gmail.com"
password = "Securify2120"

img_counter = 0


def speak(text):
    global img_counter
    tts = gTTS(text=text, lang="en")
    filename = "audio{}.mp3".format(img_counter)
    tts.save(filename)
    playsound.playsound(filename)
    img_counter += 1


r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Hello ! This is securify. May i know your name.")
    speak("Hello ! This is securify. May i know your name.")
    audio = r.listen(source, timeout=3)
try:
    print("" + r.recognize_google(audio))
except:
    speak("Sorry i couldn't hear you")
    print("Sorry i couldn't hear you")


with mic as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Did i guess your name right ?")
    speak("Did i guess your name right ?")
    reply = r.listen(source, timeout=3)
if "yes" in r.recognize_google(reply):
    speak("Okay thanks")
    print("Okay thanks")
else:
    speak("Type your name ")
    audio11 = input("Type your name ")

if "Vansh" in r.recognize_google(audio) or "Vansh" in audio11:
    speak("Hey Vansh")
    print("Hey Vansh")
elif "Akshay" in r.recognize_google(audio) or "Akshay" in audio11:
    speak("Hey Akshay")
    print("Hey Akshay")
else:
    print("Please look into the camera and press SPACE")
    speak("Please look into the camera and press SPACE")
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        cv2.imshow("SECURIFY", frame)

        k = cv2.waitKey(1)
        if k % 256 == 32:
            img_name = "unknown.jpg"
            cv2.imwrite(img_name, frame)
            print("Photo clicked.")
            break

    cam.release()
    cv2.destroyAllWindows()
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(
        MIMEText("This person tried to get into your house.", "plain"))

    filename = "unknown.jpg"
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
        print("Sorry you are unrecognized! Access denied")
    sys.exit()


print("Now can you please look into the camera. You can press space to click a picture")
speak("Now can you please look into the camera. You can press space to click a picture")
time.sleep(3)

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")
img_counter = 0
while True:
    ret, frame = cam.read()
    cv2.imshow("SECURIFY", frame)

    k = cv2.waitKey(1)
    if k % 256 == 32:
        img_name = "unknown.jpg"
        cv2.imwrite(img_name, frame)
        print("Photo clicked.")
        break

cam.release()
cv2.destroyAllWindows()

if "Vansh" in r.recognize_google(audio) or "Vansh" in audio11:
    picture_of_me = face_recognition.load_image_file("Vansh.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    unknown_picture = face_recognition.load_image_file("unknown.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results = face_recognition.compare_faces(
        [my_face_encoding], unknown_face_encoding)
    if results[0] == True:
        password = input("Please enter your unique PIN. ")
        if password == "1234":
            print("ACCESS GRANTED")
        else:
            print("Sorry you are unrecognized! Access denied")

            port = 465
            smtp_server = "smtp.gmail.com"
            sender_email = "SecurifyProtect@gmail.com"
            receiver_email = "lappykamail@gmail.com"
            password = "Securify2120"
            message = """\
            Subject: New Entry

                    Vansh just entered the house."""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

    else:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message.attach(
            MIMEText("This person tried to get into your house.", "plain"))

        filename = "unknown.jpg"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print("Sorry you are unrecognized! Access denied")
        sys.exit()

elif "Akshay" in r.recognize_google(audio) or "Akshay" in audio11:
    picture_of_me = face_recognition.load_image_file("Akshay.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]
    unknown_picture = face_recognition.load_image_file("unknown.jpg")
    unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
    results = face_recognition.compare_faces(
        [my_face_encoding], unknown_face_encoding)
    if results[0] == True:
        password = input("Please enter your unique PIN. ")
        if password == "42069":
            print("ACCESS GRANTED")
        else:
            print("Sorry you are unrecognized! Access denied")

            port = 465
            smtp_server = "smtp.gmail.com"
            sender_email = "SecurifyProtect@gmail.com"
            receiver_email = "lappykamail@gmail.com"
            password = "Securify2120"
            message = """\
            Subject: New Entry

                    Akshay just entered the house."""

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)

    else:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message.attach(
            MIMEText("This person tried to get into your house.", "plain"))

        filename = "unknown.jpg"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print("Sorry you are unrecognized! Access denied")
        sys.exit()

print("Thank you for using SECURIFY")
