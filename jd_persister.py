"""Save the JD"""

import pypandoc
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt

DOCS_FOLDER = "docs"


def save_jd_and_retrieve(llm_response, job_title):
    """Persist the JD into folder"""

    save_jd_txt(llm_response, file_name=job_title)
    save_jd_doc(llm_response, file_name=job_title)
    # save_jd_pdf(llm_response, file_name)

    return job_title


def save_jd_doc(llm_response, file_name):
    """Persist the JD as Document"""
    bullet_style = "List Bullet"

    doc = Document()
    page_title = doc.add_heading(
        file_name,
        level=0,
    )
    page_title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    doc.add_heading("Description:", level=1)
    doc.add_paragraph(llm_response.get("Description"))

    doc.add_heading("Responsibilities:", level=1)
    for responsibility in llm_response.get("Responsibilities"):
        doc.add_paragraph(responsibility, bullet_style)

    doc.add_heading("Skills:", level=1)
    for responsibility in llm_response.get("Skills"):
        doc.add_paragraph(responsibility, bullet_style)

    doc.add_heading("Experience:", level=1)
    for responsibility in llm_response.get("Experience"):
        doc.add_paragraph(responsibility, bullet_style)

    for _ in range(2):
        doc.add_paragraph()

    paragraph = doc.add_paragraph(llm_response.get("Closing Statement"))
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    run = paragraph.runs[0]  # Access the first run in the paragraph
    # run.font.name = "Calibri"
    run.font.size = Pt(13)
    run.italic = True

    doc.save(f"{DOCS_FOLDER}/{file_name}.docx")
    return f"{file_name}.docx"


def save_jd_pdf(llm_response, file_name):
    """Persist the JD as PDF"""
    save_jd_doc(llm_response, file_name)
    pypandoc.convert_file(
        f"{DOCS_FOLDER}/{file_name}.docx",
        "pdf",
        outputfile=f"{DOCS_FOLDER}/{file_name}.pdf",
    )
    return f"{file_name}.pdf"


def save_jd_txt(llm_response, file_name):
    """Persist the JD as TXT"""
    save_jd_doc(llm_response, file_name)
    pypandoc.convert_file(
        f"{DOCS_FOLDER}/{file_name}.docx",
        "plain",
        outputfile=f"{DOCS_FOLDER}/{file_name}.txt",
    )
    return f"{file_name}.txt"
