import streamlit as st
from PyPDF2 import PdfReader

from utils import (
    ROLE_SKILLS,
    extract_text_from_resume,
    detect_skills,
    calculate_ats_score,
    get_resume_suggestions,
    get_strengths,
    get_weaknesses,
    INTERVIEW_DATA,
    evaluate_answer
)

from report import create_pdf_report


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Interview Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE
# =========================================================

if "interview_results" not in st.session_state:
    st.session_state.interview_results = []

if "resume_data" not in st.session_state:
    st.session_state.resume_data = None


# =========================================================
# EXISTING ORANGE / YELLOW THEME
# =========================================================

st.markdown("""
<style>

/* =========================================
   MAIN BACKGROUND
========================================= */

.stApp {
    background:
    linear-gradient(
        135deg,
        #ff512f 0%,
        #ff7a18 35%,
        #f09819 70%,
        #ffd166 100%
    );

    background-attachment: fixed;
}


/* =========================================
   MAIN CONTAINER
========================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* =========================================
   HEADINGS
========================================= */

h1 {
    color: white !important;
    text-align: center !important;
    font-size: 3rem !important;
    font-weight: 900 !important;
    text-shadow:
        0 5px 15px rgba(0,0,0,0.25);
}

h2 {
    color: white !important;
    text-shadow:
        0 3px 10px rgba(0,0,0,0.18);
}

h3 {
    color: white !important;
}


/* =========================================
   NORMAL TEXT
========================================= */

.stMarkdown > div > p,
.stMarkdown > div > ul,
.stMarkdown > div > ol,
.stCaption {
    color: white !important;
}


/* =========================================
   LABELS
========================================= */

label {
    color: white !important;
    font-weight: 600 !important;
}


/* =========================================
   SIDEBAR
========================================= */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #ff512f,
        #f09819
    );

    border-right:
        2px solid rgba(255,255,255,0.35);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] h1 {
    text-align: left !important;
    font-size: 1.8rem !important;
}


/* =========================================
   HERO CARD
========================================= */

.hero {

    background: white;

    border-radius: 28px;

    padding: 65px 30px;

    text-align: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.20);

    margin-bottom: 35px;
}

.hero p {

    color: #444444 !important;

    font-size: 1.1rem;

    max-width: 750px;

    margin: auto;
}


/* =========================================
   METRIC CARDS
========================================= */

div[data-testid="stMetric"] {

    background: white !important;

    padding: 22px;

    border-radius: 18px;

    border-top:
        5px solid #ff6b35;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.15);

    transition: 0.3s ease;
}

div[data-testid="stMetric"]:hover {
    transform: translateY(-5px);
}

div[data-testid="stMetric"] * {
    color: #222222 !important;
}


/* =========================================
   WHITE CONTAINERS
========================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {

    background: white !important;

    border-radius: 18px !important;

    border: none !important;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.15);
}

div[data-testid="stVerticalBlockBorderWrapper"] * {
    color: #222222 !important;
}


/* =========================================
   INTERVIEW CARD
========================================= */

.interview-card {

    background: white;

    color: #222222 !important;

    border-left:
        7px solid #ff7a00;

    border-radius: 18px;

    padding: 28px;

    box-shadow:
        0 10px 25px rgba(0,0,0,0.15);

    margin: 20px 0;
}

.interview-card h3 {
    color: #ff512f !important;
}

.interview-card p {
    color: #222222 !important;
}


/* =========================================
   BUTTONS
========================================= */

.stButton > button {

    width: 100% !important;

    background:
    linear-gradient(
        135deg,
        #ff512f,
        #ff9800
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding:
        0.75rem 1rem !important;

    font-size: 1rem !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 20px
        rgba(255,81,47,0.35);

    transition: 0.3s !important;
}

.stButton > button:hover {

    transform:
        translateY(-3px);

    box-shadow:
        0 14px 30px
        rgba(255,81,47,0.45);
}


/* =========================================
   DOWNLOAD BUTTON
========================================= */

.stDownloadButton > button {

    width: 100% !important;

    background:
    linear-gradient(
        135deg,
        #ff512f,
        #ff9800
    ) !important;

    color: white !important;

    border: none !important;

    border-radius: 12px !important;

    padding:
        0.8rem 1rem !important;

    font-weight: 800 !important;

    box-shadow:
        0 8px 20px
        rgba(255,81,47,0.35);
}


/* =========================================
   TEXT INPUT
========================================= */

.stTextInput input,
.stTextArea textarea {

    background: white !important;

    color: #222222 !important;

    border:
        2px solid #ffb347 !important;

    border-radius: 12px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus {

    border:
        2px solid #ff512f !important;

    box-shadow:
        0 0 8px
        rgba(255,81,47,0.25) !important;
}


/* =========================================
   SELECT BOX
========================================= */

div[data-baseweb="select"] > div {

    background: white !important;

    color: #222222 !important;

    border:
        2px solid #ffb347 !important;

    border-radius: 12px !important;
}


/* =========================================
   FILE UPLOADER
========================================= */

section[data-testid="stFileUploaderDropzone"] {

    background: white !important;

    border:
        2px dashed #ff7a00 !important;

    border-radius: 18px !important;

    padding: 30px !important;
}

section[data-testid="stFileUploaderDropzone"] * {
    color: #222222 !important;
}


/* =========================================
   PROGRESS
========================================= */

div[data-testid="stProgress"] > div > div {

    background:
    linear-gradient(
        90deg,
        #ff512f,
        #ff9800,
        #ffd166
    ) !important;
}


/* =========================================
   ALERTS
========================================= */

div[data-testid="stAlert"] {

    background:
        rgba(255,255,255,0.95) !important;

    border-radius: 12px !important;
}

div[data-testid="stAlert"] * {
    color: #222222 !important;
}


/* =========================================
   EXPANDERS
========================================= */

details {

    background: white !important;

    border: none !important;

    border-radius: 15px !important;

    box-shadow:
        0 5px 15px rgba(0,0,0,0.12);

    padding: 8px 12px;
}

details * {
    color: #222222 !important;
}


/* =========================================
   DIVIDER
========================================= */

hr {
    border-color:
        rgba(255,255,255,0.45) !important;
}


/* =========================================
   FOOTER
========================================= */

.footer {

    margin-top: 60px;

    padding: 25px;

    text-align: center;

    color: white !important;

    font-weight: 700;

    text-shadow:
        0 3px 8px rgba(0,0,0,0.18);
}


/* =========================================
   MOBILE
========================================= */

@media (max-width: 768px) {

    .block-container {

        padding-left: 1rem;

        padding-right: 1rem;
    }

    h1 {

        font-size:
            2.2rem !important;
    }

    .hero {

        padding:
            45px 20px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title(
    "🤖 AI Interview Analyzer"
)

st.sidebar.caption(
    "Smart Resume & Interview Evaluation"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📄 Resume Analyzer",
        "🎯 Interview Practice",
        "📊 Performance Dashboard",
        "ℹ️ About"
    ]
)


# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    # NO HTML HERE
    st.title("🤖 AI Interview Analyzer")

    st.write(
        "Analyze your resume, discover your skills, "
        "practice interview questions and improve "
        "your career readiness with intelligent feedback."
    )

    st.subheader(
        "🚀 Smart Career Preparation"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 Resume Analysis",
            "Smart"
        )

        st.write(
            "Analyze ATS score, skills, strengths "
            "and areas for improvement."
        )

    with col2:

        st.metric(
            "🎯 Interview Evaluation",
            "Concept Based"
        )

        st.write(
            "Your answer is evaluated based on "
            "correct technical concepts."
        )

    with col3:

        st.metric(
            "📄 Final Report",
            "PDF"
        )

        st.write(
            "Download your complete resume and "
            "interview performance report."
        )

    st.divider()

    st.subheader(
        "⚡ How It Works"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "STEP 01",
            "Upload"
        )

        st.caption(
            "Upload your resume"
        )

    with col2:

        st.metric(
            "STEP 02",
            "Analyze"
        )

        st.caption(
            "Detect skills and ATS score"
        )

    with col3:

        st.metric(
            "STEP 03",
            "Practice"
        )

        st.caption(
            "Answer interview questions"
        )

    with col4:

        st.metric(
            "STEP 04",
            "Improve"
        )

        st.caption(
            "Get feedback and report"
        )


# =========================================================
# RESUME ANALYZER
# =========================================================

elif page == "📄 Resume Analyzer":

    st.title(
        "📄 Resume Analyzer"
    )

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input(
            "👤 Candidate Name"
        )

    with col2:

        role = st.selectbox(
            "💼 Target Job Role",
            list(ROLE_SKILLS.keys())
        )

    resume = st.file_uploader(
        "📤 Upload Resume (PDF)",
        type=["pdf"]
    )

    if resume:

        try:

            pdf = PdfReader(resume)

            resume_text = extract_text_from_resume(
                pdf
            )

            found_skills = detect_skills(
                resume_text,
                role
            )

            missing_skills = [
                skill
                for skill in ROLE_SKILLS[role]
                if skill not in found_skills
            ]

            ats_score = calculate_ats_score(
                found_skills,
                role,
                resume_text
            )

            strengths = get_strengths(
                found_skills
            )

            weaknesses = get_weaknesses(
                found_skills,
                role
            )

            suggestions = get_resume_suggestions(
                ats_score,
                found_skills,
                role
            )

            st.session_state.resume_data = {
                "name":
                    name or "Candidate",
                "role":
                    role,
                "ats_score":
                    ats_score,
                "found_skills":
                    found_skills,
                "missing_skills":
                    missing_skills,
                "strengths":
                    strengths,
                "weaknesses":
                    weaknesses,
                "suggestions":
                    suggestions
            }

            st.success(
                "✅ Resume analyzed successfully!"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "ATS Score",
                    f"{ats_score}%"
                )

            with col2:

                st.metric(
                    "Skills Found",
                    len(found_skills)
                )

            with col3:

                st.metric(
                    "Missing Skills",
                    len(missing_skills)
                )

            st.progress(
                ats_score / 100
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader(
                    "✅ Skills Detected"
                )

                if found_skills:

                    for skill in found_skills:

                        st.success(
                            f"✓ {skill}"
                        )

                else:

                    st.warning(
                        "No role-specific skills detected."
                    )

            with col2:

                st.subheader(
                    "⚠ Missing Skills"
                )

                if missing_skills:

                    for skill in missing_skills:

                        st.warning(
                            f"• {skill}"
                        )

                else:

                    st.success(
                        "No major skills missing!"
                    )

            st.subheader(
                "💪 Strengths"
            )

            for item in strengths:

                st.success(
                    item
                )

            st.subheader(
                "⚠ Areas for Improvement"
            )

            for item in weaknesses:

                st.error(
                    item
                )

            st.subheader(
                "💡 Smart Suggestions"
            )

            for item in suggestions:

                st.info(
                    item
                )

            with st.expander(
                "📄 View Resume Content"
            ):

                st.text(
                    resume_text[:5000]
                )

        except Exception as e:

            st.error(
                f"Unable to analyze the PDF: {e}"
            )


# =========================================================
# INTERVIEW PRACTICE
# =========================================================

elif page == "🎯 Interview Practice":

    st.title(
        "🎯 AI Interview Practice"
    )

    st.write(
        "Answer scoring is based on relevant technical "
        "concepts, not answer length."
    )

    role = st.selectbox(
        "Select Interview Role",
        list(INTERVIEW_DATA.keys())
    )

    questions = INTERVIEW_DATA[role]

    question_map = {
        item["question"]: item
        for item in questions
    }

    selected_question = st.selectbox(
        "Choose an Interview Question",
        list(question_map.keys())
    )

    question_data = question_map[
        selected_question
    ]

    # NORMAL STREAMLIT DISPLAY
    st.info(
        f"💬 Interview Question\n\n{selected_question}"
    )

    answer = st.text_area(
        "✍️ Write Your Answer",
        height=220,
        placeholder=
        "Explain your answer using relevant technical concepts..."
    )

    if st.button(
        "🧠 Evaluate My Answer"
    ):

        if not answer.strip():

            st.warning(
                "Please enter your answer first."
            )

        else:

            result = evaluate_answer(
                answer,
                question_data
            )

            st.success(
                "✅ Answer evaluated successfully!"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Interview Score",
                    f"{result['score']}%"
                )

            with col2:

                st.metric(
                    "Evaluation",
                    result["level"]
                )

            st.progress(
                result["score"] / 100
            )

            st.subheader(
                "💬 Feedback"
            )

            st.info(
                result["feedback"]
            )

            st.subheader(
                "🔑 Concepts Detected"
            )

            if result["matched_keywords"]:

                st.success(
                    ", ".join(
                        result["matched_keywords"]
                    )
                )

            else:

                st.error(
                    "No important expected concepts were detected."
                )

            st.subheader(
                "✨ Suggested Better Answer"
            )

            st.write(
                result["ideal_answer"]
            )

            interview_record = {
                "question":
                    selected_question,
                "answer":
                    answer,
                "score":
                    result["score"],
                "feedback":
                    result["feedback"],
                "ideal_answer":
                    result["ideal_answer"]
            }

            already_exists = any(
                item["question"]
                == selected_question
                and item["answer"]
                == answer
                for item
                in st.session_state.interview_results
            )

            if not already_exists:

                st.session_state.interview_results.append(
                    interview_record
                )


# =========================================================
# PERFORMANCE DASHBOARD
# =========================================================

elif page == "📊 Performance Dashboard":

    st.title(
        "📊 Performance Dashboard"
    )

    resume_data = (
        st.session_state.resume_data
    )

    interview_results = (
        st.session_state.interview_results
    )

    if not resume_data and not interview_results:

        st.warning(
            "Please complete Resume Analysis "
            "or Interview Practice first."
        )

    else:

        if resume_data:

            st.subheader(
                "📄 Resume Performance"
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "ATS Score",
                    f"{resume_data['ats_score']}%"
                )

            with col2:

                st.metric(
                    "Skills Found",
                    len(
                        resume_data[
                            "found_skills"
                        ]
                    )
                )

            with col3:

                st.metric(
                    "Missing Skills",
                    len(
                        resume_data[
                            "missing_skills"
                        ]
                    )
                )

        if interview_results:

            scores = [
                item["score"]
                for item in interview_results
            ]

            average_score = round(
                sum(scores) /
                len(scores)
            )

            st.subheader(
                "🎯 Interview Performance"
            )

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Questions Attempted",
                    len(interview_results)
                )

            with col2:

                st.metric(
                    "Average Score",
                    f"{average_score}%"
                )

            st.progress(
                average_score / 100
            )

            st.subheader(
                "📝 Interview History"
            )

            for index, result in enumerate(
                interview_results,
                start=1
            ):

                with st.expander(
                    f"Question {index} | Score {result['score']}%"
                ):

                    st.write(
                        "**Question:**",
                        result["question"]
                    )

                    st.write(
                        "**Your Answer:**",
                        result["answer"]
                    )

                    st.write(
                        "**Feedback:**",
                        result["feedback"]
                    )

        if resume_data:

            st.divider()

            st.subheader(
                "📄 Download Complete PDF Report"
            )

            try:

                pdf_report = create_pdf_report(
                    name=resume_data["name"],
                    role=resume_data["role"],
                    ats_score=resume_data["ats_score"],
                    found_skills=resume_data["found_skills"],
                    missing_skills=resume_data["missing_skills"],
                    strengths=resume_data["strengths"],
                    weaknesses=resume_data["weaknesses"],
                    suggestions=resume_data["suggestions"],
                    interview_results=interview_results
                )

                st.download_button(
                    label=
                    "⬇️ Download AI Interview Report (PDF)",

                    data=pdf_report,

                    file_name=
                    "AI_Interview_Analyzer_Report.pdf",

                    mime="application/pdf",

                    key="download_pdf_report"
                )

            except Exception as e:

                st.error(
                    f"PDF generation error: {e}"
                )


# =========================================================
# ABOUT
# =========================================================

elif page == "ℹ️ About":

    st.title(
        "ℹ️ About AI Interview Analyzer"
    )

    st.write(
        "A smart career preparation platform that helps "
        "candidates analyze resumes, practice interviews "
        "and improve performance."
    )

    st.subheader(
        "🚀 Our Intelligent Platform"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "📄 RESUME",
            "ANALYSIS"
        )

        st.write(
            "Upload your resume and receive ATS score, "
            "skills and improvement areas."
        )

    with col2:

        st.metric(
            "🧠 ANSWER",
            "EVALUATION"
        )

        st.write(
            "Your answer is evaluated based on correct "
            "technical concepts."
        )

    with col3:

        st.metric(
            "📊 CAREER",
            "INSIGHTS"
        )

        st.write(
            "Understand strengths, weaknesses and "
            "interview performance."
        )

    st.divider()

    st.subheader(
        "⚡ Core Features"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.success(
            "🤖 Intelligent Resume Analysis"
        )

        st.success(
            "📊 Role-Based ATS Scoring"
        )

        st.success(
            "🛠️ Technical Skill Detection"
        )

        st.success(
            "💪 Strength & Weakness Analysis"
        )

        st.success(
            "💡 Smart Resume Suggestions"
        )

    with col2:

        st.info(
            "🎯 Role-Based Interview Questions"
        )

        st.info(
            "🧠 Concept-Based Answer Evaluation"
        )

        st.info(
            "💬 Intelligent Feedback"
        )

        st.info(
            "✨ Suggested Better Answers"
        )

        st.info(
            "📄 Professional PDF Report"
        )

    st.divider()

    st.subheader(
        "🔄 How AI Interview Analyzer Works"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "STEP 01",
            "UPLOAD"
        )

        st.caption(
            "Upload your resume"
        )

    with col2:

        st.metric(
            "STEP 02",
            "ANALYZE"
        )

        st.caption(
            "Skills and ATS analysis"
        )

    with col3:

        st.metric(
            "STEP 03",
            "PRACTICE"
        )

        st.caption(
            "Answer interview questions"
        )

    with col4:

        st.metric(
            "STEP 04",
            "IMPROVE"
        )

        st.caption(
            "Get feedback and PDF report"
        )

    st.divider()

    st.subheader(
        "🛠️ Technology Stack"
    )

    st.info(
        "🐍 Python  |  🎈 Streamlit  |  "
        "📄 PyPDF2  |  📊 ReportLab"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    🤖 AI Interview Analyzer
    <br>
    Analyze • Practice • Improve • Succeed
</div>
""", unsafe_allow_html=True)