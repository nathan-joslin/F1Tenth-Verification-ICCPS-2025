
from setuptools import find_packages, setup

setup(
    name="verification",  # Replace with your package name
    version="0.1.0",  # Update with your version
    packages=find_packages(),  # Automatically discover Python packages
    # install_requires=[
    #     # List dependencies here, e.g., "numpy", "requests>=2.25.1"
    # ],
    # entry_points={
    #     "console_scripts": [
    #         # Define command-line scripts if needed, e.g., "mytool=my_package.module:main"
    #     ],
    # },
    author="Your Name",
    author_email="your.email@example.com",
    description="A short description of your package",
    # long_description=open("README.md").read(),
    # long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/yourrepo",  # Update with your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
