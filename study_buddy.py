
import re
import gradio as gr

BOT_NAME = "Study Buddy"

TIMETABLE = {
    "Monday": [
        ("6:00 AM - 6:30 AM", "Wake up and morning routine"),
        ("6:30 AM - 7:00 AM", "Exercise and freshen up"),
        ("7:00 AM - 8:00 AM", "Breakfast and preparation"),
        ("8:00 AM - 2:00 PM", "University / Academic Classes"),
        ("2:00 PM - 3:00 PM", "Lunch and rest"),
        ("3:00 PM - 4:00 PM", "Review university lectures"),
        ("4:00 PM - 5:00 PM", "Python programming practice"),
        ("5:00 PM - 5:30 PM", "Break"),
        ("5:30 PM - 6:30 PM", "Machine Learning study"),
        ("6:30 PM - 7:30 PM", "Personal time and dinner"),
        ("7:30 PM - 8:30 PM", "Assignments and homework"),
        ("8:30 PM - 9:00 PM", "Revision"),
        ("9:00 PM - 10:00 PM", "Relaxation and hobbies"),
        ("10:00 PM - 10:30 PM", "Prepare for tomorrow"),
        ("10:30 PM", "Sleep"),
    ],

    "Tuesday": [
        ("6:00 AM - 7:00 AM", "Morning routine and exercise"),
        ("7:00 AM - 8:00 AM", "Breakfast and preparation"),
        ("8:00 AM - 2:00 PM", "University / Academic Classes"),
        ("2:00 PM - 3:00 PM", "Lunch and rest"),
        ("3:00 PM - 4:00 PM", "University lecture revision"),
        ("4:00 PM - 5:00 PM", "C++ programming practice"),
        ("5:00 PM - 5:30 PM", "Break"),
        ("5:30 PM - 6:30 PM", "Machine Learning concepts"),
        ("6:30 PM - 7:30 PM", "Dinner and personal time"),
        ("7:30 PM - 8:30 PM", "Assignment work"),
        ("8:30 PM - 9:30 PM", "Practice problems"),
        ("9:30 PM - 10:30 PM", "Relax and prepare for tomorrow"),
        ("10:30 PM", "Sleep"),
    ],

    "Wednesday": [
        ("6:00 AM - 7:00 AM", "Morning routine and exercise"),
        ("7:00 AM - 8:00 AM", "Breakfast and preparation"),
        ("8:00 AM - 2:00 PM", "University / Academic Classes"),
        ("2:00 PM - 3:00 PM", "Lunch and rest"),
        ("3:00 PM - 4:00 PM", "Lecture revision and notes"),
        ("4:00 PM - 5:00 PM", "Python libraries: NumPy and Pandas"),
        ("5:00 PM - 5:30 PM", "Break"),
        ("5:30 PM - 6:30 PM", "Machine Learning practice"),
        ("6:30 PM - 7:30 PM", "Dinner and personal time"),
        ("7:30 PM - 8:30 PM", "University assignments"),
        ("8:30 PM - 9:30 PM", "Weekly topic revision"),
        ("9:30 PM - 10:30 PM", "Relaxation"),
        ("10:30 PM", "Sleep"),
    ],

    "Thursday": [
        ("6:00 AM - 7:00 AM", "Morning routine and exercise"),
        ("7:00 AM - 8:00 AM", "Breakfast and preparation"),
        ("8:00 AM - 2:00 PM", "University / Academic Classes"),
        ("2:00 PM - 3:00 PM", "Lunch and rest"),
        ("3:00 PM - 4:00 PM", "University lecture revision"),
        ("4:00 PM - 5:00 PM", "C++ and Data Structures practice"),
        ("5:00 PM - 5:30 PM", "Break"),
        ("5:30 PM - 6:30 PM", "Machine Learning theory"),
        ("6:30 PM - 7:30 PM", "Dinner and personal time"),
        ("7:30 PM - 8:30 PM", "Assignment completion"),
        ("8:30 PM - 9:30 PM", "Coding practice"),
        ("9:30 PM - 10:30 PM", "Relaxation and preparation"),
        ("10:30 PM", "Sleep"),
    ],

    "Friday": [
        ("6:00 AM - 7:00 AM", "Morning routine"),
        ("7:00 AM - 8:00 AM", "Breakfast and preparation"),
        ("8:00 AM - 2:00 PM", "University / Academic Classes"),
        ("2:00 PM - 3:00 PM", "Lunch and rest"),
        ("3:00 PM - 4:00 PM", "Weekly academic revision"),
        ("4:00 PM - 5:00 PM", "Python project development"),
        ("5:00 PM - 5:30 PM", "Break"),
        ("5:30 PM - 6:30 PM", "Machine Learning practice"),
        ("6:30 PM - 7:30 PM", "Dinner and personal time"),
        ("7:30 PM - 8:30 PM", "Complete pending assignments"),
        ("8:30 PM - 9:30 PM", "Weekly progress review"),
        ("9:30 PM - 10:30 PM", "Relaxation"),
        ("10:30 PM", "Sleep"),
    ],

    "Saturday": [
        ("7:00 AM - 8:00 AM", "Wake up and morning routine"),
        ("8:00 AM - 9:00 AM", "Breakfast"),
        ("9:00 AM - 11:00 AM", "Deep study session"),
        ("11:00 AM - 11:30 AM", "Break"),
        ("11:30 AM - 1:00 PM", "Python / ML project development"),
        ("1:00 PM - 2:00 PM", "Lunch and rest"),
        ("2:00 PM - 3:30 PM", "University assignments"),
        ("3:30 PM - 4:30 PM", "Exercise and outdoor activities"),
        ("4:30 PM - 5:30 PM", "Break and personal time"),
        ("5:30 PM - 7:00 PM", "Machine Learning course"),
        ("7:00 PM - 8:00 PM", "Dinner"),
        ("8:00 PM - 9:00 PM", "Weekly revision"),
        ("9:00 PM - 10:30 PM", "Entertainment and relaxation"),
        ("10:30 PM", "Sleep"),
    ],

    "Sunday": [
        ("7:30 AM - 8:30 AM", "Wake up and morning routine"),
        ("8:30 AM - 9:30 AM", "Breakfast"),
        ("9:30 AM - 11:00 AM", "Review difficult topics"),
        ("11:00 AM - 12:00 PM", "Personal development / Reading"),
        ("12:00 PM - 2:00 PM", "Family time and lunch"),
        ("2:00 PM - 3:00 PM", "Rest"),
        ("3:00 PM - 4:00 PM", "Prepare for upcoming week"),
        ("4:00 PM - 5:00 PM", "Organize notes and assignments"),
        ("5:00 PM - 6:00 PM", "Exercise and outdoor activities"),
        ("6:00 PM - 7:00 PM", "Free time"),
        ("7:00 PM - 8:00 PM", "Dinner"),
        ("8:00 PM - 9:00 PM", "Plan weekly goals"),
        ("9:00 PM - 10:00 PM", "Relaxation"),
        ("10:00 PM", "Sleep"),
    ]
}

def format_timetable(day):
    entries = TIMETABLE[day]

    result = f"## {day} Timetable\n\n"
    result += "| Time | Activity |\n|---|---|\n"

    for time, activity in entries:
        result += f"| {time} | {activity} |\n"

    return result


def format_weekly_timetable():
    result = "# Complete Weekly Timetable\n\n"

    for day in TIMETABLE:
        result += format_timetable(day) + "\n\n"

    return result

# KNOWLEDGE BASE
RULES = [

    {
        "topic": "Daily Routine",
        "keywords": ["daily routine", "daily schedule", "organize my day"],
        "answer": (
            "A productive daily routine should include sufficient sleep, "
            "morning preparation, academic responsibilities, focused study, "
            "exercise, meals, relaxation, and time for personal development. "
            "Follow a consistent routine while allowing flexibility."
        )
    },

    {
        "topic": "Weekly Timetable",
        "keywords": ["weekly timetable", "weekly schedule", "whole week plan"],
        "answer": (
            "Study Buddy has a predefined seven-day timetable covering "
            "Monday through Sunday. It balances university classes, "
            "programming, Machine Learning, assignments, revision, "
            "exercise, and personal activities. Ask 'Show my weekly timetable'."
        )
    },

    {
        "topic": "Study Timetable",
        "keywords": ["study timetable", "study schedule", "study plan"],
        "answer": (
            "A good study timetable divides your subjects into manageable "
            "sessions. Prioritize difficult topics when your concentration "
            "is highest. Include revision, practice, and breaks. "
            "Avoid scheduling every minute of your day."
        )
    },

    {
        "topic": "Morning Routine",
        "keywords": ["morning routine", "wake up early", "start my day"],
        "answer": (
            "Start your day with a consistent wake-up time. Freshen up, "
            "exercise, eat breakfast, review your daily priorities, "
            "and prepare for academic responsibilities. "
            "Avoid immediately checking social media."
        )
    },

    {
        "topic": "Evening Routine",
        "keywords": ["evening routine", "night routine", "before sleeping"],
        "answer": (
            "Use your evening to complete assignments, revise important "
            "topics, prepare for the next day, and relax. Reduce screen "
            "exposure before bedtime and maintain a consistent sleep schedule."
        )
    },

    {
        "topic": "Time Management",
        "keywords": ["time management", "manage my time", "save time"],
        "answer": (
            "Time management means planning and controlling how you spend "
            "your time. Set priorities, create a timetable, divide large "
            "tasks into smaller steps, avoid distractions, and review "
            "your progress regularly."
        )
    },

    {
        "topic": "Prioritization",
        "keywords": ["set priorities", "important tasks", "urgent tasks"],
        "answer": (
            "Prioritize tasks according to importance and urgency. "
            "Complete important deadlines first, then work on long-term "
            "goals. Avoid spending too much time on low-value activities."
        )
    },

    {
        "topic": "Pomodoro Technique",
        "keywords": ["pomodoro", "25 minute technique", "study timer"],
        "answer": (
            "The Pomodoro Technique involves studying for 25 minutes "
            "with complete focus, followed by a 5-minute break. "
            "After four sessions, take a longer break of 15–30 minutes. "
            "You can adjust the duration according to your concentration."
        )
    },

    {
        "topic": "Time Blocking",
        "keywords": ["time blocking", "block my time", "fixed study hours"],
        "answer": (
            "Time blocking means assigning specific time periods to "
            "different activities. For example, 4 PM to 5 PM can be "
            "reserved for programming and 5:30 PM to 6:30 PM for ML."
        )
    },

    {
        "topic": "SMART Goals", 
        "keywords": ["smart goals", "set goals", "goal setting"],
        "answer": (
            "SMART goals are Specific, Measurable, Achievable, Relevant, "
            "and Time-bound. Instead of saying 'learn Python', set a goal "
            "such as 'complete five Python exercises by Friday'."
        )
    },

    {
        "topic": "Avoiding Procrastination",
        "keywords": ["procrastination", "procrastinate", "delay work"],
        "answer": (
            "To overcome procrastination, start with a small task, "
            "remove distractions, set a short deadline, and use the "
            "5-minute rule. Focus on starting rather than completing "
            "everything immediately."
        )
    },

    {
        "topic": "Concentration",
        "keywords": ["concentration", "improve focus", "stay focused"],
        "answer": (
            "Improve concentration by studying in a quiet environment, "
            "keeping your phone away, setting one clear objective, "
            "taking short breaks, and avoiding multitasking."
        )
    },

    {
        "topic": "Distractions",
        "keywords": ["avoid distractions", "social media", "phone distraction"],
        "answer": (
            "Turn off unnecessary notifications, keep your phone away "
            "during study sessions, use website blockers if necessary, "
            "and reserve social media for scheduled breaks."
        )
    },

    {
        "topic": "Effective Learning",
        "keywords": ["study effectively", "effective learning", "learn faster"],
        "answer": (
            "Use active recall, spaced repetition, practice questions, "
            "and practical exercises. Try explaining a concept in your "
            "own words instead of repeatedly reading the same material."
        )
    },

    {
        "topic": "Active Recall",
        "keywords": ["active recall", "test myself", "remember concepts"],
        "answer": (
            "Active recall is a learning technique in which you try to "
            "remember information without looking at your notes. "
            "Use flashcards, practice questions, and self-testing."
        )
    },

    {
        "topic": "Spaced Repetition",
        "keywords": ["spaced repetition", "revision intervals", "memory retention"],
        "answer": (
            "Spaced repetition means reviewing information at increasing "
            "intervals. For example, revise a topic on the same day, "
            "the next day, after three days, and again after one week."
        )
    },

    {
        "topic": "Note Taking",
        "keywords": ["note taking", "make notes", "organize notes"],
        "answer": (
            "Create short, structured notes using headings, bullet points, "
            "examples, and diagrams. Highlight important concepts rather "
            "than copying entire textbooks."
        )
    },

    {
        "topic": "Exam Preparation",
        "keywords": ["exam preparation", "prepare for exams", "study for exams"],
        "answer": (
            "Start exam preparation early. Identify the syllabus, "
            "prioritize difficult subjects, create a revision timetable, "
            "solve past papers, and practice under timed conditions. "
            "Leave time for final revision."
        )
    },

    {
        "topic": "Assignment Management",
        "keywords": ["assignments", "complete homework", "assignment deadline"],
        "answer": (
            "Break assignments into research, planning, implementation, "
            "review, and submission. Start before the deadline and "
            "reserve time to check your work."
        )
    },

    {
        "topic": "Handling Multiple Tasks",
        "keywords": ["multiple tasks", "too much work", "many responsibilities"],
        "answer": (
            "List all pending tasks, identify their deadlines, "
            "prioritize important work, and complete one task at a time. "
            "Break large responsibilities into smaller achievable steps."
        )
    },

    {
        "topic": "Taking Breaks",
        "keywords": ["take breaks", "study breaks", "rest between studies"],
        "answer": (
            "Short breaks help maintain concentration and reduce mental "
            "fatigue. Take a 5-minute break after a focused 25-minute "
            "session, or use longer breaks after extended study periods."
        )
    },

    {
        "topic": "Sleep Management",
        "keywords": ["sleep schedule", "sleep hours", "manage sleep"],
        "answer": (
            "Most adults need at least 7 hours of sleep each night. "
            "Maintain consistent sleeping and waking times. Avoid "
            "sacrificing sleep regularly to complete academic tasks."
        )
    },

    {
        "topic": "Exercise and Health",
        "keywords": ["exercise", "physical activity", "stay healthy"],
        "answer": (
            "Include physical activity in your routine. Walking, "
            "stretching, or exercising can support physical health, "
            "energy, and general well-being. Avoid sitting continuously "
            "for long study sessions."
        )
    },

    {
        "topic": "Stress Management",
        "keywords": ["stress management", "study stress", "feeling stressed"],
        "answer": (
            "Manage academic stress by planning ahead, taking breaks, "
            "getting enough sleep, exercising, and discussing difficulties "
            "with someone you trust. Focus on progress rather than perfection."
        )
    },

    {
        "topic": "Motivation",
        "keywords": ["motivation", "stay motivated", "lack of motivation"],
        "answer": (
            "Maintain motivation by setting realistic goals, tracking "
            "small achievements, celebrating progress, and reminding "
            "yourself why you started. Build consistent habits instead "
            "of relying only on motivation."
        )
    },

    {
        "topic": "Building Habits",
        "keywords": ["build habits", "good habits", "consistent routine"],
        "answer": (
            "Build habits gradually. Start with small actions, attach "
            "new habits to existing routines, repeat them consistently, "
            "and track your progress. Consistency is more important "
            "than perfection."
        )
    },

    {
        "topic": "Weekly Review",
        "keywords": ["weekly review", "review my week", "weekly progress"],
        "answer": (
            "At the end of each week, review completed tasks, identify "
            "unfinished work, evaluate your study progress, and set "
            "priorities for the upcoming week. Sunday is reserved for "
            "this activity in the Study Buddy timetable."
        )
    },

    {
        "topic": "Weekend Planning",
        "keywords": ["weekend planning", "saturday sunday", "weekend routine"],
        "answer": (
            "Use Saturday for deeper study, programming projects, and "
            "assignments. Use Sunday for revision, personal development, "
            "weekly planning, and relaxation."
        )
    },

    {
        "topic": "Buffer Time",
        "keywords": ["buffer time", "unexpected tasks", "extra time"],
        "answer": (
            "Buffer time is extra time reserved for unexpected work, "
            "delays, or unfinished activities. Avoid scheduling your "
            "entire day without flexibility."
        )
    },

    {
        "topic": "Missed Tasks",
        "keywords": ["missed task", "missed my schedule", "could not finish"],
        "answer": (
            "If you miss a scheduled task, do not panic. Review its "
            "importance, move it to an available time slot, and adjust "
            "your remaining priorities. Avoid sacrificing essential sleep."
        )
    },

    {
        "topic": "Digital Productivity",
        "keywords": ["productivity apps", "digital tools", "organize tasks"],
        "answer": (
            "Digital calendars, task managers, reminders, and note-taking "
            "applications can help organize your responsibilities. "
            "Choose a simple system and use it consistently."
        )
    },

    {
        "topic": "Balancing Study and Personal Life",
        "keywords": ["study life balance", "personal life", "balance studies"],
        "answer": (
            "A balanced routine includes academic work, personal interests, "
            "family, exercise, social activities, and sufficient rest. "
            "Productivity is not about studying every minute."
        )
    },

    {
        "topic": "Programming Practice",
        "keywords": ["programming practice", "learn coding", "coding schedule"],
        "answer": (
            "Practice programming regularly. Focus on Python fundamentals, "
            "C++, problem-solving, data structures, and small projects. "
            "Write code yourself instead of only watching tutorials."
        )
    },

    {
        "topic": "Machine Learning Study",
        "keywords": ["machine learning", "learn ml", "ml study"],
        "answer": (
            "For Machine Learning, gradually study Python, NumPy, Pandas, "
            "Matplotlib, statistics, data preprocessing, supervised "
            "learning, classification, regression, and model evaluation. "
            "Practice concepts with small datasets."
        )
    },

    {
        "topic": "University Studies",
        "keywords": ["university studies", "academic classes", "lecture revision"],
        "answer": (
            "Attend classes, take useful notes, review lectures on the "
            "same day, complete assignments before deadlines, and "
            "regularly revise difficult topics."
        )
    },

    {
        "topic": "Time Management Mistakes",
        "keywords": ["time management mistakes", "bad study habits", "waste time"],
        "answer": (
            "Common mistakes include multitasking, procrastination, "
            "unrealistic schedules, ignoring breaks, poor sleep, "
            "and failing to prioritize tasks. Create realistic goals "
            "and review your routine regularly."
        )
    },

    {
        "topic": "Creating a Timetable",
        "keywords": ["create timetable", "make a timetable", "design schedule"],
        "answer": (
            "To create a timetable, list your fixed commitments, "
            "identify your study goals, assign time blocks, include "
            "meals and breaks, reserve buffer time, and review the "
            "schedule weekly."
        )
    },

    {
        "topic": "Productive Environment",
        "keywords": ["study environment", "study room", "study desk"],
        "answer": (
            "Choose a clean, quiet, and comfortable study environment. "
            "Keep your books and equipment organized, maintain good "
            "lighting, and remove unnecessary distractions."
        )
    },

    {
        "topic": "Goal Tracking",
        "keywords": ["track goals", "track progress", "daily goals"],
        "answer": (
            "Track your goals using a checklist or planner. Record "
            "completed tasks, pending activities, and progress toward "
            "long-term objectives. Review your results every week."
        )
    },

    {
        "topic": "Burnout Prevention",
        "keywords": ["burnout", "mental exhaustion", "too tired to study"],
        "answer": (
            "Prevent burnout by maintaining reasonable study hours, "
            "taking breaks, getting enough sleep, staying physically "
            "active, and making time for enjoyable activities. "
            "Reduce your workload when necessary."
        )
    },

    {
        "topic": "Learning from Mistakes",
        "keywords": ["learn from mistakes", "poor performance", "study improvement"],
        "answer": (
            "Identify what went wrong, understand the reason, and "
            "make a practical adjustment. Review difficult questions "
            "and use mistakes as feedback for future improvement."
        )
    },

    {
        "topic": "Productivity Tips",
        "keywords": ["productivity tips", "be productive", "increase productivity"],
        "answer": (
            "Plan your day in advance, start with important tasks, "
            "work in focused sessions, minimize distractions, "
            "take breaks, and track your achievements."
        )
    },

]

# QUESTION NORMALIZATION AND MATCHING
def normalize(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s'-]", " ", text)
    return re.sub(r"\s+", " ", text)


def find_best_rule(question):
    q = normalize(question)

    best_rule = None
    best_score = 0

    for rule in RULES:
        score = 0

        for keyword in rule["keywords"]:
            k = normalize(keyword)

            if k and k in q:
                score += 3 if " " in k else 1

        if score > best_score:
            best_score = score
            best_rule = rule

    if best_score == 0:
        return None

    return best_rule

# CHATBOT RESPONSE
def study_buddy_response(message, history):

    if not message or not message.strip():
        return "Please ask me something about time management or studying."

    q = normalize(message)

    # GREETINGS

    if q in {"hi", "hello", "hey", "salam", "assalam o alaikum"}:
        return (
            "Hello! I'm Study Buddy 📚\n\n"
            "Your personal time management assistant. "
            "I can help you with study schedules, productivity, "
            "time management, exam preparation, and daily routines.\n\n"
            "What would you like to know?"
        )

    # THANKS

    if q in {"thanks", "thank you", "thankyou"}:
        return "You're welcome! Keep learning and stay productive. 📚"

    # GOODBYE

    if q in {"bye", "goodbye", "exit"}:
        return "Goodbye! Stay organized and make every day productive. 🌟"

    # SHOW COMPLETE TIMETABLE

    if any(x in q for x in [
        "weekly timetable",
        "weekly schedule",
        "whole week timetable",
        "show my week",
        "entire week"
    ]):
        return format_weekly_timetable()

    # SHOW A PARTICULAR DAY'S TIMETABLE

    day_names = {
        "monday": "Monday",
        "tuesday": "Tuesday",
        "wednesday": "Wednesday",
        "thursday": "Thursday",
        "friday": "Friday",
        "saturday": "Saturday",
        "sunday": "Sunday"
    }

    for day_key, day_name in day_names.items():
        if day_key in q and any(word in q for word in [
            "schedule", "timetable", "plan", "routine"
        ]):
            return format_timetable(day_name)

    # SHOW TODAY'S TIMETABLE

    if any(x in q for x in ["today's schedule", "today timetable", "my schedule today"]):
        from datetime import datetime
        today = datetime.now().strftime("%A")

        if today in TIMETABLE:
            return format_timetable(today)

    # SHOW TOMORROW'S TIMETABLE

    if any(x in q for x in ["tomorrow schedule", "tomorrow timetable", "my schedule tomorrow"]):
        from datetime import datetime, timedelta
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%A")

        if tomorrow in TIMETABLE:
            return format_timetable(tomorrow)

    # LIST KNOWLEDGE BASE TOPICS

    if any(x in q for x in [
        "what can you do",
        "your topics",
        "knowledge base",
        "available topics",
        "what do you know"
    ]):
        topics = "\n".join(
            f"- {rule['topic']}" for rule in RULES
        )

        return (
            "## My Knowledge Base 📚\n\n"
            "I currently contain information about:\n\n"
            f"{topics}\n\n"
            "You can ask me questions about any of these topics."
        )

    # NUMBER OF KNOWLEDGE BASE ENTRIES

    if "how many topics" in q or "how many rules" in q:
        return (
            f"My knowledge base currently contains "
            f"{len(RULES)} predefined topics."
        )

    # MATCH STORED KNOWLEDGE

    rule = find_best_rule(message)

    if rule is None:
        return (
            "I'm sorry, I couldn't find a relevant answer in my "
            "stored knowledge base.\n\n"
            "Try asking about:\n"
            "- Time management\n"
            "- Study timetables\n"
            "- Pomodoro technique\n"
            "- Exam preparation\n"
            "- Machine Learning study\n"
            "- Productivity\n"
            "- Procrastination\n\n"
            "You can also ask: 'What topics do you know?'"
        )

    return (
        f"## {rule['topic']} 📚\n\n"
        f"{rule['answer']}\n\n"
        "*Stay consistent. Small improvements every day lead to "
        "great results!*"
    )


# ============================================================
# PROFESSIONAL GRADIO FRONTEND
# ============================================================

CUSTOM_CSS = """
:root {
    --study-accent: #2563eb;
}

.gradio-container {
    max-width: 1100px !important;
    margin: 0 auto !important;
}

#study-header {
    text-align: center;
    padding: 22px 10px 8px;
}

#study-header h1 {
    font-size: 2.4rem;
    font-weight: 750;
    letter-spacing: -0.04em;
    margin-bottom: 6px;
}

#study-header p {
    font-size: 1rem;
    opacity: .78;
}

#study-note {
    text-align: center;
    opacity: .65;
    font-size: .82rem;
    margin-top: 10px;
}
"""


# ============================================================
# LAUNCH APPLICATION
# ============================================================

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        neutral_hue="slate",
        radius_size="lg"
    ),
    css=CUSTOM_CSS,
    title="Study Buddy — Time Management Assistant"
) as demo:

    gr.HTML(
        """
        <div id="study-header">
            <h1>📚 Study Buddy</h1>
            <p>Your Personal Time Management & Study Assistant</p>
        </div>
        """
    )

    gr.ChatInterface(
        fn=study_buddy_response,

        chatbot=gr.Chatbot(
            height=520,
            placeholder=(
                "<div style='text-align:center; opacity:.7'>"
                "<strong>Welcome to Study Buddy!</strong><br>"
                "Ask me anything about time management, studying, "
                "and productivity."
                "</div>"
            )
        ),

        textbox=gr.Textbox(
            placeholder="Message Study Buddy...",
            container=False,
            scale=7
        ),

        examples=[
            "Show my weekly timetable",
            "What should I study on Monday?",
            "Explain the Pomodoro technique",
            "How can I avoid procrastination?",
            "How should I prepare for exams?",
            "How can I improve my concentration?",
            "Give me some productivity tips",
            "What topics do you know?"
        ],

        title=None,
        description=None,
        submit_btn="Send"
    )

    gr.Markdown(
        """
        <div id='study-note'>
            Study Buddy | A Knowledge-Based Time Management Chatbot
            <br>
            Helping students organize their time and improve productivity.
        </div>
        """
    )


if __name__ == "__main__":
    demo.launch(
        inbrowser=True,
        share=False
    )
