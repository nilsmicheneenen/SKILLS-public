# Full.py
import os, json, streamlit as st
from openai import OpenAI

def main():
    # instantiate your OpenAI client
    client = OpenAI(api_key=st.secrets["openai_api_key"])

    st.title("🎓 Club Finder")
    query = st.text_input("What kind of club are you looking for?")

    if st.button("Find Club") and query:
        with open("shsg.clubs.keywords.json") as f:
            clubs = json.load(f)

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                  "role": "system",
                  "content": (
                    "You are a student advisor. "
                    "Given a list of student clubs and a student's interest, "
                    "recommend the 3 most relevant club only the name don't include the keywords"
                  )
                },
                {
                  "role":"user",
                  "content":(
                    f"Student said: {query}\n\n"
                    f"Here are the clubs if no club fit in the list don't invent any:\n{json.dumps(clubs, indent=2)}"
                  )
                }
            ]
        )

        st.subheader("💡 Recommended Club")
        st.write(response.choices[0].message.content)


if __name__ == "__main__":
    main()
