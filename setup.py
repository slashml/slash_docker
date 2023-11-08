from setuptools import setup, find_packages

import os
try:
    BUILD_DIR = os.environ['BUILD_DIR']
    print('using the env var', BUILD_DIR) 
except:
    print('using the current directory as root for build')
    BUILD_DIR = f'{os.getcwd()}'

def read_req_file(req_type):
    with open(f"{BUILD_DIR}/requires-{req_type}.txt") as fp:  # pylint: disable=W1514
        requires = (line.strip() for line in fp)
        return [req for req in requires if req and not req.startswith("#")]

# Read the contents of the README file
with open("README.md", "r") as fh:
    long_description = fh.read()



setup(
    name="model_to_docker",
    version="0.0.1",
    author="eff-kay",
    author_email="faiizan14@gmail.com",
    description=(
        "A unified interface to convert pre-trained ML models to Docker images" "Developed by SlashML."
    ),
    long_description=long_description,  # Use the contents of the README file
    long_description_content_type="text/markdown",  # Set the type of the README file
    packages=find_packages("."),
    package_dir={"": "."},
    install_requires=read_req_file("install"),
    license="GNU GPLv3",
    python_requires=">=3.9",
)
