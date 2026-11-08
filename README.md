# Study Buddy — Time Management & Study Assistant 📚

**Study Buddy** is a Python-based chatbot designed to help students manage their time, organize their study schedules, and improve productivity.

It provides predefined daily and weekly timetables, study recommendations, and guidance on effective learning techniques through an interactive conversational interface.

The chatbot uses keyword-based question matching and a predefined knowledge base to identify user queries and provide relevant responses.

## Features

- **Weekly Timetable:** Display a complete seven-day study and activity schedule.
- **Daily Schedule:** View individual timetables for Monday through Sunday.
- **Today's Schedule:** Automatically display the current day's timetable.
- **Tomorrow's Schedule:** Retrieve the next day's planned activities.
- **Study Planning:** Get guidance on organizing study sessions and academic responsibilities.
- **Time Management:** Learn prioritization, time blocking, and effective scheduling.
- **Productivity Guidance:** Get advice on concentration, motivation, and avoiding procrastination.
- **Pomodoro Technique:** Understand focused study sessions and scheduled breaks.
- **Exam Preparation:** Receive guidance on revision, assignments, and exam planning.
- **Machine Learning Study:** Access general guidance on learning Machine Learning.
- **Interactive Chat Interface:** Communicate with Study Buddy through a Gradio-powered interface.
- **Fallback Responses:** Handles questions that do not match its predefined knowledge base.

## Topics Covered

- Daily and Weekly Planning
- Time Management
- Study Timetables
- Pomodoro Technique
- SMART Goals
- Active Recall
- Spaced Repetition
- Exam Preparation
- Assignment Management
- Concentration and Focus
- Avoiding Procrastination
- Stress Management
- Sleep and Exercise
- Programming Practice
- Machine Learning Study
- Productivity and Habit Building

## Technologies Used

- **Python 3:** Core programming language.
- **Regular Expressions (re):** Text normalization and processing.
- **Gradio:** Interactive chatbot interface.

## How It Works

1. The user enters a question or request.
2. Study Buddy normalizes the input text.
3. The keyword-matching system compares the question against predefined keywords.
4. A scoring mechanism identifies the most relevant knowledge category.
5. The chatbot generates a response based on the matched information.
6. Special conditions allow users to retrieve daily, weekly, today's, and tomorrow's timetables.

## Project Structure

```text
StudyBuddy/
│
├── study_buddy.py
└── README.md
```

## Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
```

**2. Navigate to the project directory**

```bash
cd StudyBuddy
```

**3. Install the required dependency**

```bash
pip install gradio
```

**4. Run the application**

```bash
python study_buddy.py
```

The application will launch in your default web browser.

## Learning Objectives

- Practice Python programming and problem-solving.
- Understand text preprocessing using regular expressions.
- Implement keyword-based question matching.
- Work with Python lists, dictionaries, loops, and functions.
- Learn to organize information using a predefined knowledge base.
- Build an interactive chatbot using Gradio.
- Apply programming concepts to a practical student productivity application.

## Limitations

- The chatbot uses predefined information rather than a trained AI or Machine Learning model.
- Responses depend on the keywords stored in its knowledge base.
- It does not dynamically modify or personalize the timetable.
- It does not automatically learn from previous conversations.
- It may not recognize questions that do not match its predefined keywords.

## Future Improvements

- Introduce more advanced NLP techniques.
- Implement semantic question understanding.
- Allow users to create and customize their own timetables.
- Add task tracking and reminders.
- Integrate persistent data storage.
- Introduce machine learning-based intent classification.

## Author

**Muhammad Saim**

GitHub: [saimkabirdev-svg](https://github.com/saimkabirdev-svg)

---

*Study Buddy is an educational Python project developed to demonstrate rule-based chatbot development, text processing, and interactive application development using Gradio.*