# =========================================
# utils.py
# =========================================

import re


# =========================================
# ROLE SKILLS
# =========================================

ROLE_SKILLS = {

    "Python Developer": [
        "Python",
        "OOP",
        "SQL",
        "Git",
        "Pandas",
        "NumPy",
        "Machine Learning"
    ],

    "Java Developer": [
        "Java",
        "OOP",
        "SQL",
        "JDBC",
        "Spring",
        "Git",
        "Collections"
    ],

    "Data Analyst": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Excel",
        "Data Visualization",
        "Statistics"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "SQL",
        "Git",
        "Responsive Design"
    ]
}


# =========================================
# INTERVIEW DATA
# =========================================

INTERVIEW_DATA = {

    "Python Developer": [

        {
            "question": "What is Python?",
            "keywords": [
                "high level",
                "interpreted",
                "programming language",
                "object oriented",
                "dynamic"
            ],
            "ideal_answer":
            "Python is a high-level, interpreted programming language "
            "known for its simple syntax. It supports object-oriented, "
            "procedural and functional programming. Python is dynamically "
            "typed and is widely used in web development, data science, "
            "automation and artificial intelligence."
        },

        {
            "question": "What is OOP?",
            "keywords": [
                "object oriented",
                "class",
                "object",
                "inheritance",
                "polymorphism",
                "encapsulation",
                "abstraction"
            ],
            "ideal_answer":
            "OOP stands for Object-Oriented Programming. It organizes "
            "programs using classes and objects. The four main concepts "
            "are encapsulation, inheritance, polymorphism and abstraction."
        },

        {
            "question": "What is Exception Handling?",
            "keywords": [
                "exception",
                "error",
                "try",
                "except",
                "finally",
                "handle"
            ],
            "ideal_answer":
            "Exception handling is used to handle runtime errors without "
            "stopping the entire program. Python provides try, except, "
            "else and finally blocks to handle exceptions."
        },

        {
            "question": "Difference between List and Tuple?",
            "keywords": [
                "list",
                "tuple",
                "mutable",
                "immutable"
            ],
            "ideal_answer":
            "A list is mutable, meaning its elements can be changed after "
            "creation. A tuple is immutable, meaning its elements cannot "
            "be changed after creation. Lists use square brackets while "
            "tuples normally use parentheses."
        },

        {
            "question": "What is a Dictionary in Python?",
            "keywords": [
                "dictionary",
                "key",
                "value",
                "key value",
                "mutable"
            ],
            "ideal_answer":
            "A dictionary is a mutable Python data structure that stores "
            "data as key-value pairs. Keys are used to access corresponding "
            "values."
        }

    ],


    "Java Developer": [

        {
            "question": "What is JVM?",
            "keywords": [
                "java virtual machine",
                "bytecode",
                "execute",
                "java",
                "platform"
            ],
            "ideal_answer":
            "JVM stands for Java Virtual Machine. It executes Java bytecode "
            "and provides platform independence. Java source code is "
            "compiled into bytecode which can run on different JVMs."
        },

        {
            "question": "Difference between JDK and JRE?",
            "keywords": [
                "jdk",
                "jre",
                "development",
                "runtime",
                "compiler"
            ],
            "ideal_answer":
            "JDK stands for Java Development Kit and is used to develop "
            "Java applications. JRE stands for Java Runtime Environment "
            "and provides the environment required to run Java applications. "
            "JDK contains the JRE along with development tools such as "
            "the Java compiler."
        },

        {
            "question": "Explain OOP concepts.",
            "keywords": [
                "class",
                "object",
                "inheritance",
                "polymorphism",
                "encapsulation",
                "abstraction"
            ],
            "ideal_answer":
            "The main OOP concepts are encapsulation, inheritance, "
            "polymorphism and abstraction. Classes define objects, "
            "encapsulation protects data, inheritance enables reuse, "
            "polymorphism allows different behaviours and abstraction "
            "hides unnecessary implementation details."
        },

        {
            "question": "What is Multithreading?",
            "keywords": [
                "multiple",
                "thread",
                "concurrent",
                "execution",
                "process"
            ],
            "ideal_answer":
            "Multithreading is the execution of multiple threads within "
            "a process. It allows tasks to run concurrently and can improve "
            "application responsiveness and performance."
        },

        {
            "question": "What is Inheritance?",
            "keywords": [
                "inheritance",
                "parent",
                "child",
                "class",
                "reuse",
                "properties",
                "methods"
            ],
            "ideal_answer":
            "Inheritance allows a child class to acquire properties and "
            "methods of a parent class. It promotes code reuse and supports "
            "hierarchical relationships between classes."
        }

    ],


    "Data Analyst": [

        {
            "question": "What is Pandas?",
            "keywords": [
                "python",
                "library",
                "data",
                "dataframe",
                "analysis"
            ],
            "ideal_answer":
            "Pandas is a Python library used for data manipulation and "
            "analysis. It provides powerful structures such as Series "
            "and DataFrame for handling structured data."
        },

        {
            "question": "Explain NumPy.",
            "keywords": [
                "python",
                "library",
                "numerical",
                "array",
                "computation"
            ],
            "ideal_answer":
            "NumPy is a Python library for numerical computing. It provides "
            "efficient multidimensional arrays and functions for mathematical "
            "and scientific computations."
        },

        {
            "question": "What is Data Cleaning?",
            "keywords": [
                "data",
                "cleaning",
                "missing",
                "duplicate",
                "incorrect",
                "remove"
            ],
            "ideal_answer":
            "Data cleaning is the process of identifying and correcting "
            "incorrect, incomplete, duplicate or inconsistent data. "
            "It may involve handling missing values and removing duplicates."
        },

        {
            "question": "What is SQL?",
            "keywords": [
                "structured",
                "query",
                "language",
                "database",
                "data"
            ],
            "ideal_answer":
            "SQL stands for Structured Query Language. It is used to "
            "create, retrieve, update and manage data stored in relational "
            "databases."
        },

        {
            "question": "Explain Data Visualization.",
            "keywords": [
                "data",
                "visual",
                "chart",
                "graph",
                "pattern",
                "insight"
            ],
            "ideal_answer":
            "Data visualization represents data using charts, graphs and "
            "other visual methods. It helps identify patterns, trends and "
            "insights more easily."
        }

    ],


    "Web Developer": [

        {
            "question": "What is HTML?",
            "keywords": [
                "hypertext",
                "markup",
                "language",
                "web",
                "structure"
            ],
            "ideal_answer":
            "HTML stands for HyperText Markup Language. It is used to "
            "structure content on web pages using elements such as headings, "
            "paragraphs, links, images and forms."
        },

        {
            "question": "Difference between HTML and HTML5?",
            "keywords": [
                "html",
                "html5",
                "semantic",
                "audio",
                "video",
                "canvas"
            ],
            "ideal_answer":
            "HTML5 is the modern version of HTML. It introduces semantic "
            "elements and built-in support for audio, video and canvas. "
            "It also provides improved support for modern web applications."
        },

        {
            "question": "Explain CSS.",
            "keywords": [
                "cascading",
                "style",
                "sheet",
                "design",
                "layout",
                "web"
            ],
            "ideal_answer":
            "CSS stands for Cascading Style Sheets. It is used to control "
            "the appearance, layout, colours, fonts and responsive design "
            "of web pages."
        },

        {
            "question": "What is JavaScript?",
            "keywords": [
                "programming",
                "language",
                "web",
                "dynamic",
                "interactive"
            ],
            "ideal_answer":
            "JavaScript is a programming language widely used to make "
            "web pages dynamic and interactive. It can respond to user "
            "actions and manipulate webpage content."
        },

        {
            "question": "What is Responsive Design?",
            "keywords": [
                "responsive",
                "screen",
                "mobile",
                "desktop",
                "device",
                "layout"
            ],
            "ideal_answer":
            "Responsive design is an approach where a website automatically "
            "adjusts its layout and content according to different screen "
            "sizes and devices such as mobiles, tablets and desktops."
        }

    ]

}


# =========================================
# RESUME TEXT EXTRACTION
# =========================================

def extract_text_from_resume(pdf):

    text = ""

    for page in pdf.pages:

        content = page.extract_text()

        if content:
            text += content + "\n"

    return text


# =========================================
# SKILL DETECTION
# =========================================

def detect_skills(text, role):

    found = []

    text_lower = text.lower()

    for skill in ROLE_SKILLS[role]:

        if skill.lower() in text_lower:

            found.append(skill)

    return found


# =========================================
# ATS SCORE
# =========================================

def calculate_ats_score(
    found_skills,
    role,
    resume_text
):

    total = len(
        ROLE_SKILLS[role]
    )

    if total == 0:
        return 0

    skill_score = (
        len(found_skills) / total
    ) * 70

    keyword_score = 0

    important_words = [
        "experience",
        "project",
        "education",
        "skills",
        "internship",
        "certification",
        "github"
    ]

    text_lower = resume_text.lower()

    for word in important_words:

        if word in text_lower:

            keyword_score += 30 / len(
                important_words
            )

    score = round(
        skill_score + keyword_score
    )

    return min(score, 100)


# =========================================
# RESUME SUGGESTIONS
# =========================================

def get_resume_suggestions(
    score,
    found_skills,
    role
):

    suggestions = []

    if score >= 80:

        suggestions.append(
            "Excellent ATS compatibility. Keep your resume updated."
        )

        suggestions.append(
            "Add measurable achievements to your projects."
        )

    elif score >= 50:

        suggestions.append(
            "Add more technical skills related to the selected role."
        )

        suggestions.append(
            "Include more project and internship details."
        )

    else:

        suggestions.append(
            "Improve the technical skills section."
        )

        suggestions.append(
            "Add relevant projects and certifications."
        )

        suggestions.append(
            "Improve the professional summary."
        )

    return suggestions


# =========================================
# STRENGTHS
# =========================================

def get_strengths(found_skills):

    strengths = []

    if found_skills:

        strengths.append(
            f"{len(found_skills)} relevant technical skills detected."
        )

    if "Python" in found_skills:

        strengths.append(
            "Python programming knowledge."
        )

    if "Java" in found_skills:

        strengths.append(
            "Java programming knowledge."
        )

    if "SQL" in found_skills:

        strengths.append(
            "Database and SQL knowledge."
        )

    if "Machine Learning" in found_skills:

        strengths.append(
            "Machine Learning knowledge."
        )

    if "React" in found_skills:

        strengths.append(
            "Modern frontend development knowledge."
        )

    if not strengths:

        strengths.append(
            "Add more role-specific technical skills."
        )

    return strengths


# =========================================
# WEAKNESSES
# =========================================

def get_weaknesses(
    found_skills,
    role
):

    missing = [
        skill
        for skill in ROLE_SKILLS[role]
        if skill not in found_skills
    ]

    if not missing:

        return [
            "No major technical skill gaps detected."
        ]

    return [
        f"Consider improving knowledge of {skill}."
        for skill in missing[:5]
    ]


# =========================================
# ANSWER EVALUATION
# =========================================

def evaluate_answer(
    answer,
    question_data
):

    answer_lower = answer.lower()

    keywords = question_data["keywords"]

    matched = []

    for keyword in keywords:

        # Match phrases as well as words
        pattern = r"\b" + re.escape(
            keyword.lower()
        ) + r"\b"

        if re.search(
            pattern,
            answer_lower
        ):

            matched.append(keyword)

    total_keywords = len(keywords)

    if total_keywords == 0:

        score = 0

    else:

        ratio = len(matched) / total_keywords

        # Correctness matters more than length
        if ratio >= 0.80:
            score = 100
        elif ratio >= 0.60:
            score = 80
        elif ratio >= 0.40:
            score = 60
        elif ratio >= 0.20:
            score = 40
        else:
            score = 0

    if score == 100:

        level = "Excellent"

        feedback = (
            "Your answer contains most of the important technical "
            "concepts expected for this question."
        )

    elif score == 80:

        level = "Very Good"

        feedback = (
            "Your answer is mostly correct. Add the remaining "
            "important concepts for a complete answer."
        )

    elif score == 60:

        level = "Good"

        feedback = (
            "Your answer is partially correct. More technical "
            "explanation is required."
        )

    elif score == 40:

        level = "Needs Improvement"

        feedback = (
            "Only a few relevant concepts were identified. "
            "Try to explain the core definition and important points."
        )

    else:

        level = "Incorrect"

        feedback = (
            "The answer does not contain enough correct technical "
            "concepts for this question."
        )

    return {

        "score": score,

        "level": level,

        "feedback": feedback,

        "matched_keywords": matched,

        "ideal_answer":
            question_data["ideal_answer"]

    }