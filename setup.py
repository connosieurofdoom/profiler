import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="connosieurofdoom", # Replace with your own username
    version="0.0.1",
    author="Shreyas",
    author_email="shreyasajitrajendran@gmail.com",
    description="Print memory and cpu usage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/connosieurofdoom/profiler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)