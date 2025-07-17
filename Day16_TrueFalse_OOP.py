#this program is a small quiz game, to show oop concepts, where the user is asked True False questions
# and the score is displayed at the end

# list of dictionaries containing questions and answers
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]

# define question class
class Question:
    # initialize question with text and answer, working as a constructor
    def __init__(self, q_text, q_answer):
        """initialize a question object with text and answer"""
        self.text = q_text  # question text
        self.answer = q_answer  # correct answer


# create an empty list to store question objects
question_bank = []
# loop through question data and create question objects
for q in question_data:
    # append each question object to question_bank
    question_bank.append(Question(q["text"], q["answer"]))

# define quizBrain class to handle quiz logic
class QuizBrain:
    # initialize quiz with a list of questions working as a constructor
    def __init__(self, questions_list):
        """initialize the quizbrain with a question list and score tracking"""
        self.score = 0  # initial score
        self.qno = 0  # current question number
        self.questions = questions_list  # list of question objects

    # check if there are still questions left
    def still_has_questions(self):
        """returns true if there are still questions left in the quiz"""
        #this line basically returns true or false based on the condition
        return self.qno < len(self.questions)

    # display the next question and get user input
    def next_question(self):
        """shows the next question and asks user for their answer"""
        self.qno += 1  # increment question number
        correct = self.questions[self.qno - 1].answer  # get correct answer
        ans = input(f"Q{self.qno}: {self.questions[self.qno - 1].text} (True/False): ").lower()  # get user input
        self.check_answer(ans, correct)  # check the user's answer

    # check if the user's answer is correct
    def check_answer(self, answer, correct_answer):
        """checks if the user's answer matches the correct answer"""
        if answer == correct_answer.lower():
            print("your answer is correct.")  # user answered correctly
            self.score += 1  # increment score
        else:
            print("your answer is incorrect.")  # user answered incorrectly


# create a quizBrain object with the question bank
obj = QuizBrain(question_bank)

# run the quiz while there are questions left
while obj.still_has_questions():
    obj.next_question()

# display the user's final score
print(f"your score is: {obj.score}/11")
