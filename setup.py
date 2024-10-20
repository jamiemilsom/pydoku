from setuptools import setup, find_packages
import os

# Read the contents of README.md if it exists
try:
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "A Python-based Sudoku solver using backtracking algorithm."

# Read requirements.txt if it exists
try:
    with open('requirements.txt') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    requirements = [
        'numpy>=1.20.0',
        'pandas>=1.3.0',
    ]

setup(
    name="pydoku",
    version="0.1.0",
    author="Jamie Milsom",
    description="A Sudoku solver implemented in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pytest>=6.2.5',
            'pytest-cov>=2.12.0',
            'flake8>=3.9.0',
            'black>=21.5b2',
            'mypy>=0.910',
        ],
    },
)