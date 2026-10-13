"""
import pyttsx3
pyttsx3.init().say("Student sssss")
engine = pyttsx3.init()
engine.say("Welcome To Python Programming. Hello Amrutaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa Mam , nice to meet youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu ")
engine.runAndWait()
"""


import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


questions_and_answers = [
    {
        "question": "What is the full form of KBC?",
        "options": [
            "Kaun Banega Crorepati",
            "Kya Aap Banega Crorepati",
            "Kuchh Bhi Banega Crorepati",
            "Kaun Banega Champion"
        ],
        "answer": "A"
    },
    {
        "question": "What is the capital of France?",
        "options": [
            "Berlin",
            "Madrid",
            "Paris",
            "Rome"
        ],
        "answer": "C"
    }
]

speak("Welcome to KBC Game. Let's start the game. Good luck!")

for qa in questions_and_answers:
    speak(qa["question"])

    for i, option in enumerate(qa["options"]):
        letter = chr(65 + i)
        speak(f"Option {letter}: {option}")

    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if answer == qa["answer"]:
        speak("Congratulations! Your answer is correct.")
    else:
        correct_index = ord(qa["answer"]) - 65
        correct_option = qa["options"][correct_index]

        speak(f"Sorry! Incorrect answer. The correct answer is {correct_option}.")
        break

speak("Thank you for playing KBC!")
