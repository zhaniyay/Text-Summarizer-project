import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer-project"
AUTHOR_USER_NAME = "Zhaniya"
SRC_REPO = "textSummarizer"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    description="small python package for NLP app",
    
)