import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HardwareProvider",
    version="0.0.6",
    author="Kethan",
    author_email="kethan@vegunta.com",
    description="A package used to get hardware info and specs. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kethan1/Hardware-Info",
    packages=setuptools.find_packages(),
    install_requires=['psutil', 'py-cpuinfo'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)