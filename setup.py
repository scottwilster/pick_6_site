from setuptools import setup, find_packages

setup(
    name="pickapp",
    version="0.0",
    install_requires=[
        "pandas",
        "django"
    ],
    setup_requires=[],
    tests_require=["pytest"],
    packages=find_packages(),
)
