from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers.json import JsonOutputParser
from langchain_core.runnables import RunnableLambda
from clean import clean_text

class JobDescriptionExtractor:
    def __init__(self, llm):
        self.llm = llm

    def scrapeWebsite(self, url):
        loader = WebBaseLoader(web_path=url)
        response = loader.load()
        cleaned_response = clean_text(response[0].page_content)
        return cleaned_response

    def promptTemplate(self):
        prompt_template = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        return prompt_template

    def extractJD(self, url: str):
        cleaned_response = self.scrapeWebsite(url)
        prompt_template = self.promptTemplate()
        json_parser = JsonOutputParser()

        chain = prompt_template | self.llm | RunnableLambda(lambda x: json_parser.parse(x.content))
        jd_response = chain.invoke({"page_data": cleaned_response})
        return jd_response
