import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="minimal-prediction-problems-kongaloosh",
    version="0.0.1",
    author="Alex Kearney",
    author_email="hi@alexkearney.com",
    description="A collection of problems that require temporal abstraction to solve.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kongaloosh/Minimal-Problems",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)