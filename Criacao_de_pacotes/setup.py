from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hw",
    version="0.0.1",
    author="Leticia Gomes",
    author_email="leticiagomes_datascience@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leticiagcsilva/Cloud_Data_Engineer_Cognizant_-2-DIO/tree/main/Criacao_de_pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)