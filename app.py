import streamlit as st
import openai
import os

openai.api_key = 'API_KEY'

def main():
    st.title("Python Code Review Application")
    st.subheader("Submit your Python code for review")

    code = st.text_area("Enter your Python code here")

    if st.button("Submit"):
        if not code:
            st.write("Please enter your Python code.")
        else:
            st.write("Analyzing your code...")
            response = analyze_code(code)
            st.write("Feedback:")
            st.write(response["feedback"])
            st.write("Fixed code:")
            st.write(response["fixed_code"])

@st.cache
def analyze_code(code):
    response = openai.Completion.create(
        model="code-davinci-001",
        prompt=f"Review the following Python code and provide feedback on potential bugs and errors, along with fixed code snippets:\n\n{code}\n\nFeedback:\n",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response.choices[0].text

if __name__ == "__main__":
    main()
