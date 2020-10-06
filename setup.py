import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="selenium_cookies",
    version="0.0.4",
    author="Adam Brewer",
    author_email="adamhb321@gmail.com",
    description="Cookie handling for selenium webdrivers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamhb123/selenium_cookies",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux"
    ],
    install_requires=['selenium'],
    python_requires='>=3.4',
)