import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beemoviespam-pkg-enzoloup", # Replace with your own username
    version="0.0.1",
    author="Enzo Loup",
    author_email="anthonius.enzo@gmail.com",
    description="Bee Movie spam",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/Enzoloup/BeeMovie_Spam",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)