# =========================================
# report.py
# =========================================

from io import BytesIO

from reportlab.lib import colors

from reportlab.lib.pagesizes import A4

from reportlab.lib.styles import getSampleStyleSheet

from reportlab.lib.enums import TA_CENTER

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)


# =========================================
# CREATE PDF REPORT
# =========================================

def create_pdf_report(
    name,
    role,
    ats_score,
    found_skills,
    missing_skills,
    strengths,
    weaknesses,
    suggestions,
    interview_results
):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]

    title_style.alignment = TA_CENTER

    title_style.textColor = colors.HexColor(
        "#ff512f"
    )

    heading_style = styles["Heading2"]

    heading_style.textColor = colors.HexColor(
        "#ff512f"
    )

    normal_style = styles["BodyText"]

    normal_style.leading = 16

    story = []

    # =========================================
    # TITLE
    # =========================================

    story.append(
        Paragraph(
            "AI INTERVIEW ANALYZER",
            title_style
        )
    )

    story.append(
        Spacer(1, 10)
    )

    story.append(
        Paragraph(
            "Resume & Interview Performance Report",
            styles["Heading3"]
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # =========================================
    # CANDIDATE INFORMATION
    # =========================================

    story.append(
        Paragraph(
            "Candidate Information",
            heading_style
        )
    )

    candidate_data = [

        ["Candidate Name", str(name)],

        ["Target Role", str(role)],

        ["ATS Score", f"{ats_score}%"]

    ]

    table = Table(
        candidate_data,
        colWidths=[150, 330]
    )

    table.setStyle(
        TableStyle([

            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#fff1e6")
            ),

            (
                "TEXTCOLOR",
                (0, 0),
                (-1, -1),
                colors.black
            ),

            (
                "GRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#ffb347")
            ),

            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            )

        ])
    )

    story.append(table)

    story.append(
        Spacer(1, 20)
    )

    # =========================================
    # SKILLS
    # =========================================

    story.append(
        Paragraph(
            "Technical Skills",
            heading_style
        )
    )

    story.append(
        Paragraph(
            "<b>Skills Found:</b> "
            + (
                ", ".join(found_skills)
                if found_skills
                else "None"
            ),
            normal_style
        )
    )

    story.append(
        Spacer(1, 8)
    )

    story.append(
        Paragraph(
            "<b>Missing Skills:</b> "
            + (
                ", ".join(missing_skills)
                if missing_skills
                else "None"
            ),
            normal_style
        )
    )

    story.append(
        Spacer(1, 20)
    )

    # =========================================
    # STRENGTHS
    # =========================================

    story.append(
        Paragraph(
            "Strengths",
            heading_style
        )
    )

    for item in strengths:

        story.append(
            Paragraph(
                "✓ " + str(item),
                normal_style
            )
        )

    story.append(
        Spacer(1, 15)
    )

    # =========================================
    # WEAKNESSES
    # =========================================

    story.append(
        Paragraph(
            "Areas for Improvement",
            heading_style
        )
    )

    for item in weaknesses:

        story.append(
            Paragraph(
                "• " + str(item),
                normal_style
            )
        )

    story.append(
        Spacer(1, 15)
    )

    # =========================================
    # SUGGESTIONS
    # =========================================

    story.append(
        Paragraph(
            "Resume Suggestions",
            heading_style
        )
    )

    for item in suggestions:

        story.append(
            Paragraph(
                "→ " + str(item),
                normal_style
            )
        )

    story.append(
        Spacer(1, 25)
    )

    # =========================================
    # INTERVIEW PERFORMANCE
    # =========================================

    story.append(
        Paragraph(
            "Interview Performance",
            heading_style
        )
    )

    if interview_results:

        scores = [
            item["score"]
            for item in interview_results
        ]

        average_score = round(
            sum(scores) / len(scores)
        )

        story.append(
            Paragraph(
                f"<b>Questions Attempted:</b> "
                f"{len(interview_results)}",
                normal_style
            )
        )

        story.append(
            Paragraph(
                f"<b>Average Interview Score:</b> "
                f"{average_score}%",
                normal_style
            )
        )

        story.append(
            Spacer(1, 15)
        )

        # =====================================
        # EACH QUESTION
        # =====================================

        for index, result in enumerate(
            interview_results,
            start=1
        ):

            story.append(
                Paragraph(
                    f"Question {index}",
                    styles["Heading3"]
                )
            )

            story.append(
                Paragraph(
                    "<b>Question:</b> "
                    + str(result["question"]),
                    normal_style
                )
            )

            story.append(
                Spacer(1, 5)
            )

            story.append(
                Paragraph(
                    "<b>Candidate Answer:</b> "
                    + str(result["answer"]),
                    normal_style
                )
            )

            story.append(
                Spacer(1, 5)
            )

            story.append(
                Paragraph(
                    f"<b>Score:</b> "
                    f"{result['score']}%",
                    normal_style
                )
            )

            story.append(
                Spacer(1, 5)
            )

            story.append(
                Paragraph(
                    "<b>Feedback:</b> "
                    + str(result["feedback"]),
                    normal_style
                )
            )

            story.append(
                Spacer(1, 5)
            )

            story.append(
                Paragraph(
                    "<b>Suggested Answer:</b> "
                    + str(result["ideal_answer"]),
                    normal_style
                )
            )

            story.append(
                Spacer(1, 20)
            )

    else:

        story.append(
            Paragraph(
                "No interview questions have been attempted yet.",
                normal_style
            )
        )

    # =========================================
    # FINAL SUMMARY
    # =========================================

    story.append(
        Spacer(1, 15)
    )

    story.append(
        Paragraph(
            "Final Summary",
            heading_style
        )
    )

    if interview_results:

        scores = [
            item["score"]
            for item in interview_results
        ]

        average = round(
            sum(scores) / len(scores)
        )

        overall = round(
            (ats_score + average) / 2
        )

        story.append(
            Paragraph(
                f"<b>Overall Career Readiness Score:</b> "
                f"{overall}%",
                normal_style
            )
        )

    else:

        story.append(
            Paragraph(
                f"<b>ATS Score:</b> {ats_score}%",
                normal_style
            )
        )

    story.append(
        Spacer(1, 25)
    )

    story.append(
        Paragraph(
            "Generated by AI Interview Analyzer",
            styles["Italic"]
        )
    )

    # =========================================
    # BUILD PDF
    # =========================================

    document.build(story)

    buffer.seek(0)

    return buffer.getvalue()