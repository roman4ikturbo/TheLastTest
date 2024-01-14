import tkinter as tk

# Question data
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "answer_choices": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": 0
    },
    {
        "question": "Who is the author of \"Harry Potter\"?",
        "answer_choices": ["J.K. Rowling", "Stephen King", "J.R.R. Tolkien", "George R.R. Martin"],
        "correct_answer": 0
    },
    {
        "question": "What is the Earth's approximate diameter?",
        "answer_choices": ["10,000 kilometers", "1 million kilometers", "100 million kilometers", "1 billion kilometers"],
        "correct_answer": 1
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "answer_choices": ["Venus", "Mars", "Jupiter", "Saturn"],
        "correct_answer": 1
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer_choices": ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"],
        "correct_answer": 1
    },
    {
        "question": "What is the largest animal in the world?",
        "answer_choices": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": 2
    },
    {
        "question": "In which year did World War I begin?",
        "answer_choices": ["1910", "1914", "1918", "1922"],
        "correct_answer": 1
    }
]

# Global variables
current_question_index = 0
score = 0
restart_button = None
next_button = None

# Create the main window
window = tk.Tk()
window.title("Trivia Quiz")
window.geometry("400x400")

# Create the feedback label
feedback_label = tk.Label(text="", font=("Arial", 16))
feedback_label.pack(pady=20)

# Create the question label
question_label = tk.Label(text="", font=("Arial", 20))
question_label.pack(pady=10)

# Create a list to store answer buttons
answer_buttons = []

# Function to create answer buttons based on the number of choices
def create_answer_buttons(choices):
    for i, choice in enumerate(choices):
        button = tk.Button(text=f"Answer {i + 1}: {choice}", command=lambda i=i: answer_selected(i))
        button.pack(pady=5)
        answer_buttons.append(button)

# Function to create the check button
def create_check_button():
    global check_button
    check_button = tk.Button(text="Check", command=check_answer, state="disabled")
    check_button.pack(pady=5)

# Function to check user answer and display feedback
def check_answer():
    global score, current_question_index

    selected_answer = var.get()

    # Check if there are more questions
    if current_question_index < len(quiz_questions):
        correct_answer = quiz_questions[current_question_index]["correct_answer"]

        # Handle invalid answer inputs
        if selected_answer == -1:
            feedback_label.config(text="Please select an answer.")
            return

        if selected_answer == correct_answer:
            feedback_label.config(text=f"Correct! The answer is {quiz_questions[current_question_index]['answer_choices'][correct_answer]}")
            score += 1
        else:
            feedback_label.config(text=f"Incorrect. The correct answer is {quiz_questions[current_question_index]['answer_choices'][correct_answer]}")

        # Enable the next question button
        next_button.config(state="normal")
    else:
        # End of the quiz
        end_quiz()

# Function to start the quiz
def start_quiz():
    global current_question_index, score

    # Check for empty questions or answer choices
    if not quiz_questions:
        feedback_label.config(text="Quiz is empty. Please add questions and answer choices.")
        return

    # Reset variables
    current_question_index = 0
    score = 0

    # Display the first question
    show_question()

def show_question():
    global current_question_index, next_button

    # Check if there are more questions
    if current_question_index < len(quiz_questions):
        current_question = quiz_questions[current_question_index]

        # Update the question label
        question_label.config(text=f"Question {current_question_index + 1}: {current_question['question']}")

        # Destroy previous answer buttons
        for button in answer_buttons:
            button.destroy()

        # Create new answer buttons based on the number of choices
        create_answer_buttons(current_question["answer_choices"])

        # Clear previous selection
        var.set(-1)

        # Disable the check button
        check_button.config(state="disabled")

        # Disable the next button
        if next_button:
            next_button.config(state="disabled")
    else:
        # End of the quiz
        end_quiz()

# Variable to store selected answer
var = tk.IntVar()
var.set(-1)

# Create check button
create_check_button()

# Function to handle answer selection
def answer_selected(selected_index):
    var.set(selected_index)
    check_button.config(state="normal")

# Function to show the next question
def show_next_question():
    global current_question_index, next_button

    # Move to the next question
    current_question_index += 1

    # Display the next question if available
    if current_question_index < len(quiz_questions):
        # Display the next question
        show_question()

        # Disable the next button
        if next_button:
            next_button.config(state="disabled")
    else:
        # End of the quiz
        end_quiz()

# Function to end the quiz
# Function to end the quiz
def end_quiz():
    global score, restart_button, next_button

    # Disable answer buttons
    for button in answer_buttons:
        if button.winfo_exists():
            button.config(state="disabled")

    # Display the final score and congratulatory message
    feedback_label.config(text=f"Quiz Over. Your Final Score: {score}/{len(quiz_questions)}\nCongratulations!")

    # Create restart button if it doesn't exist
    if not restart_button:
        restart_button = tk.Button(text="Restart Quiz", command=start_quiz)
        restart_button.pack(pady=5)

    # Disable the next button if it exists
    if next_button:
        next_button.config(state="disabled")

# ... (rest of your code)


# Create next button
next_button = tk.Button(text="Next Question", command=show_next_question, state="disabled")
next_button.pack(pady=5)

# Start the quiz
start_quiz()

# Run the main loop
window.mainloop()

