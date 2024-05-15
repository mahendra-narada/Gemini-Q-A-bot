Q&A Demo with Streamlit and Gemini API

This repository provides a basic implementation of a Q&A application built with Streamlit and Google's Generative AI platform, specifically the Gemini API.

Features

Users can type their questions in a text input field.
Clicking a button triggers the application to generate a response using the Gemini model.
The generated response is displayed on the screen.
Requirements

Python 3.6 or later
Streamlit (pip install streamlit)
google-generativeai library (pip install google-generativeai)
Instructions

Clone this repository.
Create a file named .env in the root directory.
Add your Google Generative AI API key to the .env file in the following format:
GOOGLE_API_KEY="YOUR_API_KEY"
Replace "YOUR_API_KEY" with your actual API key (obtained from [Google Cloud Console](URL google cloud console)).
Run the application using streamlit run app.py.
Deployment (Optional)

While Streamlit allows you to run the app locally, you can deploy it to a cloud platform for wider accessibility. Streamlit offers deployment options, or you can explore cloud providers like Google Cloud Platform or Amazon Web Services.

How it Works

The application leverages the following functionalities:

Streamlit: Streamlit is used to create the web app interface, including the text input field, button, and response display area.
dotenv: This library helps load environment variables securely from the .env file, keeping your API key confidential.
google-generativeai: This library provides access to the Gemini API for generating responses to user queries.
Further Development

This is a basic example, and you can enhance it by:

Adding functionalities to handle different types of user queries.
Implementing error handling for a more robust user experience.
Customizing the user interface with Streamlit's theming capabilities.
Feel free to explore the code and experiment with these possibilities!
