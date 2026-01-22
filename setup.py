from setuptools import setup, find_packages

setup(
    name="abuseqqc",
    version="0.1.0",
    description="FASTA/FASTQ quality control tool for genome assemblies",
    author="Musoba Abubakar",
    author_email="abubakarmusoba630@gmail.com",
    url="https://github.com/abubakarmusoba/ABUSEqQC",
    packages=find_packages(),
    install_requires=[
        "biopython",
    ],
    entry_points={
        "console_scripts": [
            "abuseqqc=abuseqqc.__main__:main",
        ],
    },
    python_requires=">=3.8",
)
