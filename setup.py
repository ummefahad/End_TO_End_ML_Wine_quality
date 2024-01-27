import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    

__version__ = "0.0.0"

REPO_NAME = "Wine-Quality-project",
AUTHOR_USER_NAME = 'ummefahad',
SRC_REPO = "mlproject",
AUTHOR_EMAIL = "ummefahad97@gmail.com"



setuptools.setup(  
    version=__version__,  
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # Fixed the typo in Long_description_content
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": "https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)