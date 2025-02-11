
import streamlit as st
from main import ai_tutor

def main():
    st.set_page_config(page_title="AI Tutor", layout="wide")
    st.title("📚 AI Tutor")
    st.write("An interactive AI-powered tutor for students!")
    
    # Sidebar for user input
    with st.sidebar:
        st.header("Ask a Question")
        user_query = st.text_area("Enter your question:", "What is Python?")
        submit_button = st.button("Get Answer")
    
    # Display AI response
    if submit_button and user_query:
        with st.spinner("Thinking..."):
            response = ai_tutor.run(message=user_query)

        # Handle function call cases
        if isinstance(response, str):  # If response is a direct string
            st.subheader("Answer:")
            st.markdown(response)
        elif hasattr(response, "content") and isinstance(response.content, str):  # If response contains structured content
            st.subheader("Answer:")
            st.markdown(response.content)
        elif hasattr(response, "tool_calls") and response.tool_calls:
            # Extract the first tool call result, assuming it's the correct response
            tool_response = response.tool_calls[0].get("result", "")
            if tool_response:
                st.subheader("Answer:")
                st.markdown(tool_response)
            else:
                st.error("Sorry, I couldn't generate a structured response.")
        else:
            st.error("Sorry, I couldn't understand the response.")

    # Suggested topics
    st.sidebar.header("Suggested Topics")
    topics = ["Newton's Laws", "Basics of Python", "HTML Structure", "Simple Coding Projects"]
    for topic in topics:
        if st.button(topic):
            with st.spinner("Thinking..."):
                response = ai_tutor.run(message=topic)
            if isinstance(response, str):
                st.subheader(f"{topic}:")
                st.markdown(response)
            elif hasattr(response, "content") and isinstance(response.content, str):
                st.subheader(f"{topic}:")
                st.markdown(response.content)
            else:
                st.error("Sorry, I couldn't generate a structured response.")
    
if __name__ == "__main__":
    main()
