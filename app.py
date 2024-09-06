"""Python JD Generator"""

import os

from fastapi import BackgroundTasks, FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from jd_generator import get_jd_from_model_json
from jd_persister import save_jd_and_retrieve

app = FastAPI()


class JobDescriptionRequest(BaseModel):
    """Request Parameters"""

    job_title: str
    experience: str
    skills: str


def delete_file(file_path: str):
    """Deleting the generated files"""
    try:
        os.remove(f"{file_path}.txt")
        os.remove(f"{file_path}.pdf")
        os.remove(f"{file_path}.docx")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")


@app.post("/generate-jd")
async def generate_jd(request: JobDescriptionRequest):
    """Generating PDF Response"""
    llm_response = get_jd_from_model_json(
        request.job_title, request.skills, request.experience
    )
    file_path = save_jd_and_retrieve(llm_response, file_name=request.job_title)
    print("Job Description generated successfully!!!")
    return {"message": "Success", "file_name": file_path}


@app.get("/download")
async def download_jd(
    background_tasks: BackgroundTasks,
    f_name: str,
    f_type: str,
):
    """Serving PDF Response"""
    f_name = "docs/" + f_name
    background_tasks.add_task(delete_file, f_name)

    if f_type.endswith("txt"):
        return FileResponse(f_name + ".txt", media_type="text/plain")
    # elif f_type.endswith("pdf"):
    #     return FileResponse(f_name + ".pdf", media_type="application/pdf")
    else:
        return FileResponse(
            f_name + ".docx",
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )


def get_job_description_inputs():
    """Get the inputs from HR"""
    job_title = input("Job Title:")
    skills = input("Skills:")
    experience = input("Experience:")
    return job_title, skills, experience


def generate_job_description():
    """Gnereate the job description"""
    (job_title, skills, experience) = get_job_description_inputs()
    llm_response = get_jd_from_model_json(job_title, skills, experience)
    print("LLM Response", llm_response)
    save_jd_and_retrieve(llm_response, file_name=job_title)
    print("Job Description generated successfully!!!")


# if __name__ == "__main__":
#     # generate_job_description()
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)
