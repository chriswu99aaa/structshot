from setuptools import setup, find_packages

setup(
    name="structshot",
    packages=find_packages(),
    install_requires=[
        "pytorch-lightning~=1.8.6",
        "transformers~=4.35.2",
        "seqeval",
    ],
)
