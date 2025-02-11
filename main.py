
import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo

# Load API key from Streamlit secrets
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Study Agent: Helps with general learning and explanations
study_agent = Agent(
    name="Study Agent",
    role="Interactive tutor for students",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Explain concepts in simple, engaging ways suitable for students aged 6-18.",
        "Provide real-world examples where possible.",
        "Encourage curiosity and interactive learning."
    ],
    markdown=True,
)

# Coding Agent: Helps students with programming concepts and coding exercises
coding_agent = Agent(
    name="Coding Agent",
    role="Helps students learn coding",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=[
        "Provide beginner-friendly explanations for programming concepts.",
        "Give coding examples in Python, HTML, and Scratch.",
        "Encourage students to try small projects and coding challenges."
    ],
    markdown=True,
)

# Quiz Agent: Generates quizzes to reinforce learning
quiz_agent = Agent(
    name="Quiz Agent",
    role="Creates interactive quizzes",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=[
        "Generate multiple-choice and short-answer quizzes based on a topic.",
        "Ensure questions are suitable for different age groups.",
        "Provide feedback on answers with explanations."
    ],
    markdown=True,
)

# AI Team: Combines study, coding, and quiz agents into one AI assistant
ai_tutor = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[study_agent, coding_agent, quiz_agent],
    instructions=[
        "Be interactive and engaging.",
        "Guide students step-by-step when explaining topics.",
        "Encourage learning through questions, discussions, and projects."
    ],
    markdown=True,
)
# ai_tutor.get_response("What is Python?")