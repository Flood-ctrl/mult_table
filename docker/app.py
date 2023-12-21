from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def index():
    # Reset session variables when returning to the index page.
    session.pop('first_question', None)
    session.pop('score', None)
    session.pop('submitted_answer', None)

    # Render the index.html template when the root URL is accessed.
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Initialize session variables if not present.
    session.setdefault('first_question', True)
    session.setdefault('score', {'correct': 0, 'incorrect': 0})
    session.setdefault('submitted_answer', False)

    num1, num2, answer, is_correct, user_answer = None, None, None, None, None

    if request.method == 'POST':
        try:
            # Retrieve the user's answer and the correct answer from the form data.
            user_answer = int(request.form['user_answer'])
            actual_answer = int(request.form['actual_answer'])
            # Check if the user's answer is correct.
            is_correct = user_answer == actual_answer
        except (KeyError, ValueError):
            # Handle the case when 'user_answer' or 'actual_answer' is not present or not an integer.
            is_correct = False

        # Update score based on correctness only if an answer was submitted.
        if session['submitted_answer']:
            if is_correct:
                session['score']['correct'] += 1
            else:
                session['score']['incorrect'] += 1

        # Mark that the user has submitted an answer.
        session['submitted_answer'] = True

    # Generate new random numbers if the page is just opened or the answer is incorrect.
    if not session['first_question'] or (session['submitted_answer'] and (is_correct is None or not is_correct)):
        if session['first_question'] is True:
            is_correct = 'first_time_run'
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 * num2

    # Mark that the first question has been asked.
    session['first_question'] = False

    # Render the quiz.html template with the appropriate variables.
    return render_template('quiz.html', num1=num1, num2=num2, answer=answer, is_correct=is_correct, user_answer=user_answer, score=session['score'], submitted_answer=session['submitted_answer'])

if __name__ == "__main__":
    # Run the Flask app on the specified host and port for local testing.
    app.run(host="0.0.0.0", port=8080, debug=True)
