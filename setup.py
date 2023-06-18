from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from pathlib import Path
import shutil

VERSION = "0.0.2"


class PostDevelopCommand(develop):
    """Post-installation for development mode."""

    def run(self):
        develop.run(self)
        self.execute(self.copy_files, (), {})

    def copy_files(self):
        dest_path = Path.home() / ".config/io.datasette.llm/templates"
        dest_path.mkdir(parents=True, exist_ok=True)

        src_path = Path(__file__).parent / "llm_toolbox/tools/templates"
        for file in src_path.glob("*.yaml"):
            shutil.copy2(file, dest_path)


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        self.execute(self.copy_files, (), {})

    copy_files = PostDevelopCommand.copy_files


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
    cmdclass={"develop": PostDevelopCommand, "install": PostInstallCommand},
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "llm-toolbox=llm_toolbox.cli:cli",
            "thesaurus=llm_toolbox.cli:thesaurus",
            "llm=llm.cli:cli",
            "translate=llm_toolbox.cli:translate",
            "define=llm_toolbox.cli:define",
            "proofread=llm_toolbox.cli:proofread",
            "lessonize=llm_toolbox.cli:lessonize",
            "commitgen=llm_toolbox.cli:commitgen",
            "codereview=llm_toolbox.cli:codereview",
            "summarize=llm_toolbox.cli:summarize",
            "critique=llm_toolbox.cli:critique",
            "pathlearner=llm_toolbox.cli:pathlearner",
            "explain=llm_toolbox.cli:explain",
            "cheermeup=llm_toolbox.cli:cheermeup",
            "shellgenius=shellgenius.cli:shellgenius",
            "study=llm_toolbox.cli:study",
            "teachlib=llm_toolbox.cli:teachlib",
            "vocabmaster=vocabmaster.cli:vocabmaster",
        ]
    },
    python_requires=">=3.8",
)
