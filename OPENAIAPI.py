# This file connects to the OpenAI API in order to make AI based HSG- clubs recommendation 
# Import necessary libraries
import os  # Commonly imported when working with file paths
import json  # To read and parse the JSON file containing club data
import streamlit as st  # For building the web interface
from openai import OpenAI  # OpenAI client to access GPT-3.5-turbo API

def main():
    # Step 1: Instantiate the OpenAI client using your secret API key from Streamlit's secure storage
    client = OpenAI(api_key=st.secrets["openai_api_key"])

    # Step 2: Set the page title for the Streamlit app
    st.title("🎓 Club Finder")

    # Step 3: Ask the user what kind of club they are interested in
    query = st.text_input("What kind of club are you looking for?")

    # Step 4: Only proceed if the user clicks the button AND provided some input
    if st.button("Find Club") and query:

        # Step 5: Load the list of clubs from a JSON file that includes keywords describing each club
        with open("shsg.clubs.keywords.json") as f:
            clubs = json.load(f)

        # Step 6: Send a request to OpenAI's chat model to find relevant clubs
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Use a lightweight yet powerful model for fast results
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a student advisor. "
                        "Given a list of student clubs and a student's interest, "
                        "recommend the 3 most relevant club only the name don't include the keywords" #explain the task to the model for successful completion
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Student said: {query}\n\n"
                        f"Here are the clubs if no club fit in the list don't invent any:\n{json.dumps(clubs, indent=2)}" #ensure no club is invented and only club included in the list are recommended
                    )
                }
            ]
        )

        # Step 7: Display the AI's response (list of recommended clubs)
        st.subheader("💡 Recommended Club")
        st.write(response.choices[0].message.content) #processing of the response of the api

# Step 8: Standard Python practice — ensure `main()` only runs when the script is executed directly
if __name__ == "__main__":
    main()


