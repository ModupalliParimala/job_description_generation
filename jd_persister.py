"""Save the JD"""

import pypandoc
from docx import Document
from docx2pdf import convert
from docx.enum.text import WD_ALIGN_PARAGRAPH


def save_jd(llm_response, file_name, f_format=None):
    """Persist the JD into folder"""

    file_name = "docs/" + file_name + "_JD"

    if f_format == "txt":
        save_jd_txt(llm_response, file_name)
    elif f_format == "doc":
        save_jd_doc(llm_response, file_name)
    else:
        save_jd_pdf(llm_response, file_name)


def save_jd_doc(llm_response, file_name):
    """Persist the JD as Document"""
    bullet_style = "List Bullet"

    doc = Document()
    page_title = doc.add_heading(
        llm_response.get("Job Title"),
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

    doc.save(f"{file_name}.docx")


def save_jd_pdf(llm_response, f_name):
    """Persist the JD as PDF"""
    save_jd_doc(llm_response, f_name)
    convert(f"{f_name}.docx")


def save_jd_txt(llm_response, f_name):
    """Persist the JD as TXT"""
    save_jd_doc(llm_response, f_name)
    pypandoc.convert_file(f"{f_name}.docx", "plain", outputfile=f"{f_name}.txt")
