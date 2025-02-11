# AI Tutor

## Overview
AI Tutor is an interactive AI-powered learning assistant designed to help students (ages 6-18) understand various subjects in an engaging way. The AI tutor includes multiple agents specialized in study explanations, coding assistance, and quiz generation. This application is built using `phi.agent` for AI functionalities and `streamlit` for the user interface.

## Features
- **Study Agent**: Provides explanations of various topics in a student-friendly manner.
- **Coding Agent**: Assists students in learning programming concepts and coding exercises.
- **Quiz Agent**: Generates quizzes to reinforce learning.
- **AI Tutor**: A combined AI assistant that integrates all three agents for a seamless learning experience.
- **Interactive UI**: A user-friendly interface powered by Streamlit.

---

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required dependencies (install using the command below)

### Steps to Set Up and Run
1. Clone the repository:
   ```sh
   git clone https://github.com/AjayG1026/AI-Tutor.git
   cd ai-tutor
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the root directory and configure API keys (if required).
   ```sh
   touch .env
   ```
   - Add any necessary environment variables, such as API keys for `Groq` and `DuckDuckGo`.
4. Run the application:
   ```sh
   python -m streamlit run app.py
   ```

---

## Project Structure
```
ai-tutor/
│── main.py        # Defines AI Agents
│── app.py         # Streamlit-based UI for interaction
│── requirements.txt # Project dependencies
│── .env           # Environment variables (API keys)
└── README.md      # Project documentation
```

---

## Code Explanation

### `main.py`
Defines the AI Agents:
- `Study Agent`: Provides learning explanations.
- `Coding Agent`: Assists with coding exercises.
- `Quiz Agent`: Generates interactive quizzes.
- `AI Tutor`: Integrates all agents into a single AI assistant.

### `app.py`
Implements the user interface using Streamlit:
- Allows students to input questions.
- Displays AI-generated responses.
- Provides suggested topics for exploration.
- Uses a sidebar for question input and navigation.

---

## Usage
1. Open the Streamlit app.
2. Enter a topic or question in the sidebar.
3. Click "Get Answer" to receive an AI-generated response.
4. Explore suggested topics for quick learning.
5. Receive interactive explanations, coding guidance, or quiz questions.

---

## Future Enhancements
- Add more AI tools for subject-specific learning.
- Improve quiz interactivity with scoring features.
- Include voice-based interaction for younger students.

---

## Contributors
- Ajay Mudiraj G
- Contact: [ajaygudise03@gmail.com]

