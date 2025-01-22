import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

REPO_NAME = "WineQualityCheck"
AUTHER_USERNAME = "Shubham999-del"
AUTHER_EMAIL = "shubhamslash18@gmail.com"

setuptools.setup(
    name="MLProject", # Replace with your own username
    version="0.0.1",
    author=f"{AUTHER_USERNAME}",
    author_email=AUTHER_EMAIL,
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHER_USERNAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHER_USERNAME}/{REPO_NAME}/issues",
    },
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)