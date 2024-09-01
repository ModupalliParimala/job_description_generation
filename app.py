"""Python JD Generator"""

from jd_generator import get_jd_from_model_json
from jd_persister import save_jd


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
    save_jd(llm_response, file_name=job_title, f_format="pdf")
    print("Job Description generated successfully!!!")


if __name__ == "__main__":
    generate_job_description()
