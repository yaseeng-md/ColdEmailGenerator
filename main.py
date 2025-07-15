from langchain_core.prompts import PromptTemplate
from jdExtract import JobDescriptionExtractor
from createChroma import CreateChromaDatabase

csvpath = r"data\yaseen-projects.csv"
collections = CreateChromaDatabase(csv_path = csvpath)

def prompt_template(self):
    mail_prompt = PromptTemplate.from_template(
        """
        ### JOB DESCRIPTION:
        {job_description}

        ### CANDIDATE PROFILE:
        You are Gandluru Mohammed Yaseen, an Arificial and Machine Learning Post Gradation Student, with experitice in Machine Learning and Generative AI.
        You are currently working upon LLM-based Article Summarization Tool using LLama 3B and you have a past experiece as Machine Learning Intern.
        You are a Research Student authored "Attension Based Explicit Content Detection - A Transformer based approcah".
        Your job is to write a cold email to the requirters regarding the job mentioned above describing the capability of you in fulfilling their needs.
        Also add the most relevant ones from the following links to showcase Yaseen's portfolio: {project_link}
        Remember you are Yaseen, Post Grad Student at LPU. 
        Do not provide a preamble.
        ### EMAIL (NO PREAMBLE):
        """
        )
    return mail_prompt


    
