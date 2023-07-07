from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from pathlib import Path
import shutil

VERSION = "0.1.8"


def read_requirements():
    with open("requirements.txt") as file:
        return list(file)


def get_long_description():
    with open("README.md", encoding="utf8") as file:
        return file.read()


setup(
    name="LLM-Toolbox",
    description="A versatile collection of CLI tools leveraging large language models",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Sébastien De Revière",
    url="https://github.com/sderev/llm-toolbox",
    project_urls={
        "Documentation": "https://github.com/sderev/llm-toolbox",
        "Issues": "http://github.com/sderev/llm-toolbox/issues",
        "Changelog": "https://github.com/sderev/llm-toolbox/releases",
    },
    license="Apache Licence, Version 2.0",
    version=VERSION,
    packages=find_packages(),
    package_data={
        "llm_toolbox": ["tools/templates/*.yaml"],
    },
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "cheermeup=llm_toolbox.cli:cheermeup",
            "codereview=llm_toolbox.cli:codereview",
            "commitgen=llm_toolbox.cli:commitgen",
            "critique=llm_toolbox.cli:critique",
            "define=llm_toolbox.cli:define",
            "explain=llm_toolbox.cli:explain",
            "lessonize=llm_toolbox.cli:lessonize",
            "life=llm_toolbox.cli:life",
            "llm-toolbox=llm_toolbox.cli:cli",
            "lmt=lmt_cli.cli:lmt",
            "pathlearner=llm_toolbox.cli:pathlearner",
            "proofread=llm_toolbox.cli:proofread",
            "shellgenius=shellgenius.cli:shellgenius",
            "study=llm_toolbox.cli:study",
            "summarize=llm_toolbox.cli:summarize",
            "teachlib=llm_toolbox.cli:teachlib",
            "thesaurus=llm_toolbox.cli:thesaurus",
            "translate=llm_toolbox.cli:translate",
            "vocabmaster=vocabmaster.cli:vocabmaster",
        ]
    },
    python_requires=">=3.8",
)
