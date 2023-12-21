from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def generate_new_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    answer = num1 * num2
    return num1, num2, answer

def get_current_question():
    if 'current_question' not in session:
        session['current_question'] = generate_new_question()
    return session['current_question']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    session.setdefault('score', {'correct': 0, 'incorrect': 0})
    session.setdefault('submitted_answer', False)

    num1, num2, answer = get_current_question()
    is_correct, user_answer = None, None

    if request.method == 'POST':
        try:
            user_answer = int(request.form['user_answer'])
            actual_answer = int(request.form['actual_answer'])
            is_correct = user_answer == actual_answer
        except (KeyError, ValueError):
            is_correct = False

        if session['submitted_answer']:
            if is_correct:
                session['score']['correct'] += 1
            else:
                session['score']['incorrect'] += 1

        session['submitted_answer'] = True

    return render_template('quiz.html', num1=num1, num2=num2, answer=answer, is_correct=is_correct, user_answer=user_answer, score=session['score'], submitted_answer=session['submitted_answer'])

@app.route('/next', methods=['GET', 'POST'])
def next_question():
    session['current_question'] = generate_new_question()
    session['submitted_answer'] = False
    num1, num2, answer = get_current_question()
    return render_template('quiz.html', num1=num1, num2=num2, answer=answer, score=session['score'], submitted_answer=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
