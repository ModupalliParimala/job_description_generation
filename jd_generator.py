"""Python JD Generator"""

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate


# from googlegenai_llm import load_llm

from groq_gemma_llm import load_llm

# from groq_llama_llm import load_llm

# from groq_mixtral_llm import load_llm

# from ollama_llama import load_llm

load_dotenv()


def get_jd_from_model_json(job_title, skills, experience):
    """Connect and Get the response"""
    llm = load_llm()

    prompt_template = ChatPromptTemplate(
        [
            (
                "system",
                get_job_description_sytem_propmt_msg(),
            ),
            (
                "user",
                get_job_description_user_propmt_msg(),
            ),
        ]
    )

    parser = JsonOutputParser()

    chain = prompt_template | llm | parser
    return chain.invoke(
        {
            "job_title": job_title,
            "skills": skills,
            "experience": experience,
            "num_words": 250,
        }
    )


def get_job_description_sytem_propmt_msg():
    """Instruct the system to follow this"""
    return """
            You are a hiring manager for a company TI-TechInterrupt.
            TI-TechInterrupt is a leading technology company specializing in software development.
            TI-TechInterrupt is into 'SAP Insurance' industry.
            You are looking to hire a new employee.
            You need to write a job description for a job posting.
            The job description should be SEO friendly and
            should highlight the unique features and benefits of the position.
            Please generate the JD in JSON format with the following fields
            * Job Title
            * Description
            * Responsibilities
            * Skills
            * Experience - more creative and list format
           """


def get_job_description_user_propmt_msg():
    """As Chat format is followed, the user message"""
    return """
              Write a job description for a {job_title}
              that is around {num_words} words in a neutral tone.
              Incorporate the following skils: {skills}.
              The experince needed is {experience}.
              The job position should be described in SEO friendly,
              highlighting its unique features and benefits."
           """
