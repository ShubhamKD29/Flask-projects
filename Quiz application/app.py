from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy quiz questions
questions = [
    {"question": "What is the capital of France?", 
     "options": ["Paris", "London", "Rome", "Berlin"], 
     "answer": "Paris"},

    {"question": "Which language is used for web apps?", 
     "options": ["Python", "C++", "Java", "HTML"], 
     "answer": "Python"},

    {"question": "Who developed C language?", 
     "options": ["Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum", "James Gosling"], 
     "answer": "Dennis Ritchie"},

    {"question": "What is the capital of India?", 
     "options": ["New Delhi", "Mumbai", "Kolkata", "Chennai"], 
     "answer": "New Delhi"},

    {"question": "Which company developed Java?", 
     "options": ["Microsoft", "Sun Microsystems", "IBM", "Google"], 
     "answer": "Sun Microsystems"},

    {"question": "HTML stands for?", 
     "options": ["Hyper Text Markup Language", "High Transfer Machine Language", "Hyperlink Transfer Markup Language", "None of these"], 
     "answer": "Hyper Text Markup Language"},

    {"question": "What is 2 + 2 * 2?", 
     "options": ["6", "8", "4", "2"], 
     "answer": "6"},

    {"question": "Which planet is known as the Red Planet?", 
     "options": ["Mars", "Jupiter", "Venus", "Saturn"], 
     "answer": "Mars"},

    {"question": "In Python, which keyword is used to define a function?", 
     "options": ["func", "define", "def", "function"], 
     "answer": "def"},

    {"question": "Which data structure uses FIFO (First In First Out)?", 
     "options": ["Stack", "Queue", "Array", "Tree"], 
     "answer": "Queue"}
]


# Home page
@app.route("/")
def home():
    return render_template("home.html")

# Quiz page
@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# Result page
@app.route("/result", methods=['POST'])
def result():
    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f"q{i}")
        if user_answer == q["answer"]:
            score += 1
    return render_template("result.html", score=score, total=len(questions))
