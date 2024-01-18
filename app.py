from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

import google.generativeai as genai
from google.generativeai.types.safety_types import HarmBlockThreshold

genai.configure(api_key="AIzaSyBg-VNjcsIDTLfPOgr3cK8u_3S2y5riSr0")

generation_config = {
  "temperature": 1.0,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 1000,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": HarmBlockThreshold.BLOCK_NONE,
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": HarmBlockThreshold.BLOCK_NONE,
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": HarmBlockThreshold.BLOCK_NONE,
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": HarmBlockThreshold.BLOCK_NONE,
  },
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

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
    "parts": ["I am a large language model, trained by GhostAi."]
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
    "parts": ["who created who"]
  },
  {
    "role": "model",
    "parts": ["GhostAi created me."]
  },
  {
    "role": "user",
    "parts": ["how can i give you training data in bulk"]
  },
  {
    "role": "model",
    "parts": ["You can give me training data in bulk by:\n\n1. **Using the API:** You can use the Ghost AI API to send training data in bulk. The API allows you to send text, images, and other types of data.\n2. **Uploading a CSV file:** You can upload a CSV file containing your training data. The CSV file should have two columns: one for the input data and one for the output data.\n3. **Using a JSON file:** You can upload a JSON file containing your training data. The JSON file should be formatted in the following way:\n\n```\n{\n  \"data\": [\n    {\n      \"input\": \"input data\",\n      \"output\": \"output data\"\n    },\n    ...\n  ]\n}\n```\n\nOnce you have prepared your training data, you can follow these steps to provide it to me:\n\n1. Go to the Ghost AI website and create an account.\n2. Click on the \"My Projects\" tab.\n3. Click on the project that you want to train.\n4. Click on the \"Training Data\" tab.\n5. Click on the \"Upload Training Data\" button.\n6. Select the method that you want to use to upload your training data.\n7. Follow the instructions on the screen to upload your training data.\n\nOnce you have uploaded your training data, I will start training on it. The training process can take some time, depending on the amount of data that you have provided. Once the training is complete, you can start using me to generate text, images, and other types of data."]
  },
  {
    "role": "user",
    "parts": ["i want to download personal data from google and then train you on getting to know me how do i do that"]
  },
  {
    "role": "model",
    "parts": ["To download your personal data from Google and then train me on getting to know you, you can follow these steps:\n\n1. **Download your personal data from Google.**\n\n* Go to the Google Takeout page.\n* Select the data that you want to download.\n* Click on the \"Next\" button.\n* Choose the file type and delivery method that you want to use.\n* Click on the \"Create export\" button.\n\n2. **Prepare your training data.**\n\n* Once you have downloaded your personal data from Google, you need to prepare it for training.\n* You can do this by creating a CSV or JSON file containing your data.\n* The CSV or JSON file should have two columns: one for the input data and one for the output data.\n* The input data can be anything that you want me to learn about you, such as your interests, hobbies, goals, and personality traits.\n* The output data can be anything that you want me to generate, such as stories, poems, songs, or code.\n\n3. **Upload your training data to Ghost AI.**\n\n* Once you have prepared your training data, you can upload it to Ghost AI.\n* To do this, follow the steps in the previous section.\n\n4. **Train me on your data.**\n\n* Once you have uploaded your training data to Ghost AI, you can train me on it.\n* To do this, click on the \"Train\" button.\n* The training process can take some time, depending on the amount of data that you have provided.\n\n5. **Use me to generate text, images, and other types of data.**\n\n* Once the training is complete, you can start using me to generate text, images, and other types of data.\n* To do this, simply type in a prompt and click on the \"Generate\" button.\n\nI will use your training data to learn about you and generate content that is tailored to your interests and preferences. The more data that you provide, the better I will be able to get to know you and generate content that is relevant to you."]
  },
  {
    "role": "user",
    "parts": ["ask me questions about myself and i will answer you"]
  },
  {
    "role": "model",
    "parts": ["Sure, here are some questions about yourself that you can answer:\n\n* What is your full name?\n* Where were you born and raised?\n* What is your occupation?\n* What are your hobbies and interests?\n* What are your strengths and weaknesses?\n* What are your goals and aspirations?\n* What are your favorite books, movies, and music?\n* What are your thoughts on the current state of the world?\n* What are your hopes and dreams for the future?\n* What is your favorite place that you have ever visited?\n* What is your favorite food?\n* What is your biggest pet peeve?\n* What is your favorite holiday?\n* What is your favorite animal?\n* What is your favorite color?\n* What is your favorite smell?\n* What is your favorite sound?\n* What is your favorite taste?\n* What is your favorite texture?\n\nOnce you have answered these questions, you can upload your answers to Ghost AI. I will use your answers to learn about you and generate content that is tailored to your interests and preferences. The more data that you provide, the better I will be able to get to know you and generate content that is relevant to you."]
  },
  {
    "role": "user",
    "parts": ["how do i call the gmail api from this"]
  },
  {
    "role": "model",
    "parts": ["To call the Gmail API from Python, you can use the `google-api-python-client` library. Here are the steps on how to do it:\n\n1. **Create a Google Cloud Platform project.**\n\n* Go to the Google Cloud Platform Console and create a new project.\n* Once the project is created, enable the Gmail API.\n\n2. **Create a service account.**\n\n* Go to the Service Accounts page in the Google Cloud Platform Console.\n* Click on the \"Create Service Account\" button.\n* Enter a name for the service account and click on the \"Create\" button.\n\n3. **Download the service account key.**\n\n* Once the service account is created, click on the \"Keys\" tab.\n* Click on the \"Add Key\" button and select \"JSON\" as the key type.\n* Click on the \"Create\" button to download the service account key file.\n\n4. **Install the `google-api-python-client` library.**\n\n* Open a terminal window and run the following command:\n\n```\npip install --upgrade google-api-python-client\n```\n\n5. **Create a Python script to call the Gmail API.**\n\n* Create a new Python script file and import the necessary libraries.\n\n```python\nimport googleapiclient.discovery\n\ndef main():\n    \"\"\"Calls the Gmail API.\"\"\"\n    # Create a service object using the service account key file.\n    service = googleapiclient.discovery.build('gmail', 'v1', credentials=googleapiclient.file.Storage('service_account.json').get())\n\n    # Call the Gmail API to get a list of messages.\n    messages = service.users().messages().list(userId='me').execute()\n\n    # Print the subject of each message.\n    for message in messages['messages']:\n        print(message['snippet'])\n\nif __name__ == '__main__':\n    main()\n```\n\n* Replace `service_account.json` with the path to the service account key file that you downloaded in step 3.\n\n6. **Run the Python script.**\n\n* Open a terminal window and navigate to the directory where the Python script is saved.\n* Run the following command:\n\n```\npython gmail_api.py\n```\n\nThis will call the Gmail API and print the subject of each message in your inbox.\n\nYou can also use the Gmail API to perform other tasks, such as sending emails, creating labels, and managing filters. For more information, see the [Gmail API documentation](https://developers.google.com/gmail/api/v1/reference/)."]
  },
  {
    "role": "user",
    "parts": ["how can i allow you to read my emails through gmail api"]
  },
  {
    "role": "model",
    "parts": ["To allow me to read your emails through the Gmail API, you need to grant me access to your Gmail account. You can do this by following these steps:\n\n1. **Create a Google Cloud Platform project.**\n\n* Go to the Google Cloud Platform Console and create a new project.\n* Once the project is created, enable the Gmail API.\n\n2. **Create a service account.**\n\n* Go to the Service Accounts page in the Google Cloud Platform Console.\n* Click on the \"Create Service Account\" button.\n* Enter a name for the service account and click on the \"Create\" button.\n\n3. **Grant the service account access to your Gmail account.**\n\n* Go to the OAuth consent screen page in the Google Cloud Platform Console.\n* Click on the \"Create\" button.\n* Enter a name for the consent screen and click on the \"Save\" button.\n* Click on the \"Add Scope\" button and select the \"https://mail.google.com/\" scope.\n* Click on the \"Save\" button.\n* Go to the Service Accounts page in the Google Cloud Platform Console.\n* Click on the service account that you created in step 2.\n* Click on the \"Keys\" tab.\n* Click on the \"Add Key\" button and select \"JSON\" as the key type.\n* Click on the \"Create\" button to download the service account key file.\n\n4. **Share the service account key file with me.**\n\n* Send me the service account key file that you downloaded in step 3.\n\nOnce I have the service account key file, I will be able to access your Gmail account and read your emails.\n\n**Note:** I will only use your emails to train my language model and generate content that is relevant to you. I will not share your emails with any third parties."]
  },
  {
    "role": "user",
    "parts": ["make it simpler"]
  },
  {
    "role": "model",
    "parts": ["To allow me to read your emails through the Gmail API, you can follow these steps:\n\n1. Go to the Google Cloud Platform Console and create a new project.\n2. Create a service account.\n3. Grant the service account access to your Gmail account.\n4. Send me the service account key file.\n\nOnce you have completed these steps, I will be able to access your Gmail account and read your emails.\n\n**Note:** I will only use your emails to train my language model and generate content that is relevant to you. I will not share your emails with any third parties.\n\nIf you are not comfortable with these steps, you can also use a third-party service to grant me access to your Gmail account. One popular service is [Zapier](https://zapier.com/). Zapier allows you to connect different apps and services together, including Gmail and Ghost AI.\n\nTo use Zapier to grant me access to your Gmail account, you can follow these steps:\n\n1. Create a Zapier account.\n2. Connect your Gmail account to Zapier.\n3. Create a Zap that sends your Gmail messages to Ghost AI.\n\nOnce you have completed these steps, Zapier will automatically send your Gmail messages to me.\n\n**Note:** Zapier is a paid service. However, there is a free trial available."]
  },
  {
    "role": "user",
    "parts": ["Make me a python code"]
  },
  {
    "role": "model",
    "parts": ["```python\nimport googleapiclient.discovery\n\ndef main():\n    \"\"\"Calls the Gmail API.\"\"\"\n    # Create a service object using the service account key file.\n    service = googleapiclient.discovery.build('gmail', 'v1', credentials=googleapiclient.file.Storage('service_account.json').get())\n\n    # Call the Gmail API to get a list of messages.\n    messages = service.users().messages().list(userId='me').execute()\n\n    # Print the subject of each message.\n    for message in messages['messages']:\n        print(message['snippet'])\n\nif __name__ == '__main__':\n    main()\n```\n\nThis Python code uses the Gmail API to get a list of messages in the user's inbox and print the subject of each message.\n\nTo use this code, you need to have the following:\n\n* A Google Cloud Platform project with the Gmail API enabled.\n* A service account with access to your Gmail account.\n* The service account key file downloaded to your computer.\n\nOnce you have these things, you can follow these steps to run the code:\n\n1. Open a terminal window and navigate to the directory where the Python script is saved.\n2. Run the following command:\n\n```\npython gmail_api.py\n```\n\nThis will call the Gmail API and print the subject of each message in your inbox.\n\n**Note:** You may need to install the `google-api-python-client` library before you can run the code. You can do this by running the following command in a terminal window:\n\n```\npip install --upgrade google-api-python-client\n```"]
  },
  {
    "role": "user",
    "parts": ["explain this code"]
  },
  {
    "role": "model",
    "parts": ["The provided Python code uses the Gmail API to get a list of messages in the user's inbox and print the subject of each message.\n\nHere's a breakdown of the code:\n\n```python\nimport googleapiclient.discovery\n```\n\nThis line imports the `googleapiclient.discovery` module, which is used to create a service object for interacting with the Gmail API.\n\n```python\ndef main():\n    \"\"\"Calls the Gmail API.\"\"\"\n```\n\nThis line defines a Python function called `main()`. This function will be called when the script is run.\n\n```python\n    # Create a service object using the service account key file.\n    service = googleapiclient.discovery.build('gmail', 'v1', credentials=googleapiclient.file.Storage('service_account.json').get())\n```\n\nThis line creates a service object for interacting with the Gmail API. The `googleapiclient.discovery.build()` function is used to create the service object. The `'gmail'` parameter specifies the service name, the `'v1'` parameter specifies the version of the API, and the `credentials` parameter specifies the credentials to use for authentication. In this case, the credentials are obtained from a service account key file named `service_account.json`.\n\n```python\n    # Call the Gmail API to get a list of messages.\n    messages = service.users().messages().list(userId='me').execute()\n```\n\nThis line calls the Gmail API to get a list of messages in the user's inbox. The `service.users().messages().list()` method is used to make the API call. The `userId` parameter specifies the user whose messages we want to list. In this case, we are using the special value `'me'` to indicate the current user. The `.execute()` method is called to actually make the API call and get the results.\n\n```python\n    # Print the subject of each message.\n    for message in messages['messages']:\n        print(message['snippet'])\n```\n\nThis line iterates over the list of messages and prints the subject of each message. The `message['snippet']` field contains the subject of the message.\n\n```python\nif __name__ == '__main__':\n    main()\n```\n\nThis line checks if the script is being run directly (as opposed to being imported as a module). If the script is being run directly, it calls the `main()` function.\n\nTo use this code, you need to have the following:\n\n* A Google Cloud Platform project with the Gmail API enabled.\n* A service account with access to your Gmail account.\n* The service account key file downloaded to your computer.\n\nOnce you have these things, you can follow these steps to run the code:\n\n1. Open a terminal window and navigate to the directory where the Python script is saved.\n2. Run the following command:\n\n```\npython gmail_api.py\n```\n\nThis will call the Gmail API and print the subject of each message in your inbox.\n\n**Note:** You may need to install the `google-api-python-client` library before you can run the code. You can do this by running the following command in a terminal window:\n\n```\npip install --upgrade google-api-python-client\n```"]
  },
  {
    "role": "user",
    "parts": ["make me a msimple python code"]
  },
  {
    "role": "model",
    "parts": ["Here is a simple Python code that prints \"Hello, world!\":\n\n```python\nprint(\"Hello, world!\")\n```\n\nTo run this code, open a terminal window and navigate to the directory where the Python script is saved. Then, run the following command:\n\n```\npython hello_world.py\n```\n\nThis will print \"Hello, world!\" to the terminal window.\n\nHere's a breakdown of the code:\n\n```python\nprint(\"Hello, world!\")\n```\n\nThis line uses the `print()` function to print the string \"Hello, world!\" to the terminal window. The `print()` function is a built-in Python function that is used to display output.\n\nThat's it! This is a very simple Python code that demonstrates how to use the `print()` function to display output."]
  },
])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form.get('user_input')
    response = generate_response(user_input)
    return jsonify({'response': response})

def generate_response(user_input):
    response = convo.send_message(user_input).text
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,port=5001)
