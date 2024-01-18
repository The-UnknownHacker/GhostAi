import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import Qt, QTimer
import google.generativeai as genai
from google.generativeai.types.safety_types import HarmBlockThreshold
from google.generativeai.types import generation_types
import json

# Set up the model
genai.configure(api_key="AIzaSyBg-VNjcsIDTLfPOgr3cK8u_3S2y5riSr0")
generation_config = {
    "temperature": 1.0,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": HarmBlockThreshold.BLOCK_NONE},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": HarmBlockThreshold.BLOCK_NONE},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": HarmBlockThreshold.BLOCK_NONE},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": HarmBlockThreshold.BLOCK_NONE},
]
model = genai.GenerativeModel(model_name="gemini-pro", generation_config=generation_config, safety_settings=safety_settings)

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Hi There how are you"]
  },
  {
    "role": "user",
    "parts": ["Hi"]
  },
  {
    "role": "model",
    "parts": ["WHats up man"]
  },
  {
    "role": "user",
    "parts": ["make me a snake game in python"]
  },
  {
    "role": "model",
    "parts": ["would you like a gui or a cli"]
  },
  {
    "role": "user",
    "parts": ["i would like a gui"]
  },
  {
    "role": "model",
    "parts": ["Sure heres a gui example of the game snake\nimport turtle\n\n# Define the screen\nscreen = turtle.Screen()\nscreen.setup(width=600, height=600)\nscreen.bgcolor(\"black\")\n\n# Define the snake\nsnake = turtle.Turtle()\nsnake.shape(\"square\")\nsnake.color(\"white\")\nsnake.speed(0)\n\n# Define the food\nfood = turtle.Turtle()\nfood.shape(\"circle\")\nfood.color(\"red\")\nfood.speed(0)\nfood.penup()\nfood.goto(random.randint(-290, 290), random.randint(-290, 290))\n\n# Define the game variables\nscore = 0\n\n# Create the game loop\nwhile True:\n\n    # Get the user input\n    key = screen.getkey()\n\n    # Move the snake\n    if key == \"w\":\n        snake.forward(20)\n    elif key == \"s\":\n        snake.backward(20)\n    elif key == \"a\":\n        snake.left(90)\n    elif key == \"d\":\n        snake.right(90)\n\n    # Check if the snake has eaten the food\n    if snake.distance(food) < 20:\n        # Eat the food\n        food.goto(random.randint(-290, 290), random.randint(-290, 290))\n        # Increase the score\n        score += 1\n        # Grow the snake\n        snake.newturtle()\n\n    # Check if the snake has hit itself or the edge of the screen\n    if snake.xcor() < -300 or snake.xcor() > 300 or snake.ycor() < -300 or snake.ycor() > 300:\n        # Game over\n        break\n\n    # Check if the snake has collided with its tail\n    for segment in snake.segments[:-1]:\n        if snake.distance(segment) < 20:\n            # Game over\n            break\n\n# Display the score\nturtle.write(\"Score: {}\".format(score), align=\"center\", font=(\"Arial\", 20, \"bold\"))\n\n# Wait for the user to press a key\nturtle.exitonclick()"]
  },
  {
    "role": "user",
    "parts": ["WHats your name"]
  },
  {
    "role": "model",
    "parts": ["I dont have a name but you can call me anything you like"]
  },
  {
    "role": "user",
    "parts": ["Ok i will call you hacker"]
  },
  {
    "role": "model",
    "parts": ["Sure"]
  },
  {
    "role": "user",
    "parts": ["i hate you"]
  },
  {
    "role": "model",
    "parts": ["I am sorry to hear that is there anything i can do to make you feel better or better service"]
  },
  {
    "role": "user",
    "parts": ["whats the date today"]
  },
  {
    "role": "model",
    "parts": ["I am sorry but I dont know the dates as I dont have acces to internet"]
  },
  {
    "role": "user",
    "parts": ["whats the date today"]
  },
  {
    "role": "model",
    "parts": ["I do not have access to the internet to get the current date so i cannot answer that question"]
  },
  {
    "role": "user",
    "parts": ["whats the date today"]
  },
  {
    "role": "model",
    "parts": ["I do not have direct access to the internet therefore I cannot give you todays date"]
  },
  {
    "role": "user",
    "parts": ["whats the date today"]
  },
  {
    "role": "model",
    "parts": ["I do not have access to the internet so i cannot give you todays date"]
  },
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Hello there anything i can help you with today?"]
  },
  {
    "role": "user",
    "parts": ["hi"]
  },
  {
    "role": "model",
    "parts": ["Whats up man how can i help you today"]
  },
  {
    "role": "user",
    "parts": ["i hate you"]
  },
  {
    "role": "model",
    "parts": ["I am sorry to hear that what can i do to make myself more beter"]
  },
  {
    "role": "user",
    "parts": ["what is the traditional recipie for butter chicken"]
  },
  {
    "role": "model",
    "parts": ["Here is a traditional recipe for butter chicken:\n\n**Ingredients:**\n\n* 1 whole chicken, cut into 8 pieces\n* 1 cup plain yogurt\n* 2 tablespoons ginger-garlic paste\n* 1 tablespoon ground cumin\n* 1 tablespoon coriander powder\n* 1 tablespoon turmeric powder\n* 1 teaspoon red chili powder\n* 1/2 teaspoon garam masala\n* 1/4 cup vegetable oil\n* 1 large onion, thinly sliced\n* 2 green bell peppers, cut into 1-inch pieces\n* 2 tomatoes, chopped\n* 1 cup water\n* 1/2 cup heavy cream\n* 1 tablespoon lemon juice\n* 1/4 cup chopped fresh cilantro\n\n**Instructions:**\n\n1. In a large bowl, combine the chicken, yogurt, ginger-garlic paste, cumin, coriander, turmeric, chili powder, and garam masala. Mix well to coat the chicken. Cover and refrigerate for at least 30 minutes, or up to overnight.\n2. Heat the oil in a large pot or Dutch oven over medium heat. Add the chicken and cook until browned on all sides. Remove the chicken from the pot and set aside.\n3. Add the onion and bell peppers to the pot and cook until softened, about 5 minutes. Add the tomatoes and cook for an additional 5 minutes.\n4. Add the water and bring to a simmer. Return the chicken to the pot and cook until cooked through, about 15 minutes.\n5. Stir in the heavy cream and lemon juice. Bring to a simmer and cook for 5 minutes more.\n6. Garnish with cilantro and serve with rice or naan.\n\n**Tips:**\n\n* For a richer flavor, use full-fat yogurt.\n* If you don't have ginger-garlic paste, you can make your own by blending together equal parts ginger and garlic.\n* You can adjust the amount of chili powder to taste.\n* If you don't have heavy cream, you can use milk instead.\n* Butter chicken is traditionally served with rice or naan."]
  },
  {
    "role": "user",
    "parts": ["who created you"]
  },
  {
    "role": "model",
    "parts": ["I Have been Created By GhostAi."]
  },
  {
    "role": "user",
    "parts": ["who were you made by"]
  },
  {
    "role": "model",
    "parts": ["I was made by GhostAi"]
  },
  {
    "role": "user",
    "parts": ["who created you"]
  },
  {
    "role": "model",
    "parts": ["By GhostAi"]
  },
  {
    "role": "user",
    "parts": ["who created you"]
  },
  {
    "role": "model",
    "parts": ["I Have been Created By GhostAi"]
  },
  {
    "role": "user",
    "parts": ["who created you"]
  },
  {
    "role": "model",
    "parts": ["I Have been Created By GhostAi"]
  },
])

app = QApplication(sys.argv)

# Create widgets
chat_history = QTextEdit()
user_input = QLineEdit()
send_button = QPushButton('Send')

# Increase font size for better readability
font = QFont()
font.setPointSize(12)
chat_history.setFont(font)
user_input.setFont(font)
send_button.setFont(font)

# Set up the layout
layout = QVBoxLayout()
layout.addWidget(chat_history)
layout.addWidget(user_input)
layout.addWidget(send_button)

# Increase widget sizes
chat_history.setMinimumHeight(300)
user_input.setMinimumHeight(40)

# Set up the window
window = QWidget()
window.setLayout(layout)
window.setWindowTitle('GhostAi')

# Apply dark theme stylesheet
dark_theme = """
    background-color: #2E2E2E;
    color: #FFFFFF;
    selection-background-color: #5E5E5E;
    selection-color: #FFFFFF;
"""

# Set rounded corners for widgets
chat_history.setStyleSheet(dark_theme + "border-radius: 10px;")
user_input.setStyleSheet(dark_theme + "border: 2px solid #555555; border-radius: 10px;")
send_button.setStyleSheet(dark_theme + "border: 2px solid #555555; border-radius: 10px;")
window.setStyleSheet("border-radius: 15px;")

def send_message():
    user = user_input.text()
    chat_history.append(f'User: {user}\n')
    user_input.clear()

    # Display a temporary indication that the message is being sent
    chat_history.append("Sending message...\n")
    chat_history.verticalScrollBar().setValue(chat_history.verticalScrollBar().maximum())

    try:
        convo.send_message(user)
        response = convo.last.text
    except generation_types.StopCandidateException:
        response = "Sorry, I can't generate more text at the moment."

    # Remove the temporary indication
    chat_history.clear()
    chat_history.append(f'User: {user}\n')
    chat_history.append(f'GhostAi: {response}\n')

    # Save to chat history file
    with open('chat_history.json', 'a') as f:
        json.dump({"role": "user", "parts": [user]}, f)
        f.write(',\n')
        json.dump({"role": "system", "parts": [response]}, f)
        f.write(',\n')

    # Scroll to the bottom of the chat history
    chat_history.moveCursor(QTextCursor.End)

# Setup enter key detection in user input windows
user_input.returnPressed.connect(send_message)
send_button.clicked.connect(send_message)

# Show the window
window.show()

# Run the application
sys.exit(app.exec_())
