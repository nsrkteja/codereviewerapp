import streamlit as st
import openai

# Set up OpenAI API
openai.api_key = "API_KEY"

def review_code(user_code):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=f"Review the following Python code and identify any potential bugs, errors, or areas of improvement. Provide fixed code snippets where applicable.\n\n{user_code}\n\n# Review:\n",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    st.write("## Review")
    st.write(response.choices[0].text)

def main():
    st.title("Python Code Review")
    user_code = st.text_area("Enter your Python code here:")
    if st.button("Submit for Review"):
        review_code(user_code)

if __name__ == "__main__":
    main()
