# ABUSEqQC

**ABUSEqQC** is a lightweight, command-line quality control (QC) tool for **FASTA and FASTQ** sequence files. It is designed for molecular biologists and bioinformaticians who need quick, reliable summary statistics before downstream analyses such as genome assembly, annotation, or comparative genomics.

The tool automatically detects the input file type and safely supports **FASTA-only statistics** as well as **FASTQ quality-score analysis**, without compromising either format.

---

## Features

* Automatic detection of **FASTA** and **FASTQ** files
* Core sequence statistics:

  * Number of sequences
  * Minimum, maximum, and mean sequence length
  * **N50** statistic
  * GC content (%)
  * Ambiguous base (N) content (%)
* **FASTQ-only quality statistics**:

  * Mean Phred quality score
  * Minimum Phred quality score
  * Maximum Phred quality score
* Simple and reproducible **command-line interface (CLI)**
* Built with **Python 3** and **Biopython**

---

## Installation

### Requirements

* Python **≥ 3.8** (tested on Python 3.12)
* Biopython
* NumPy

### Install dependencies

```bash
pip install biopython numpy
```

### Clone the repository

```bash
git clone https://github.com/abubakarmusoba/ABUSEqQC.git
cd ABUSEqQC
```

---

## Usage

Run ABUSEqQC from the terminal:

```bash
python3 abuseqqc.py -i <input_file> -o <output_report.txt>
```

### Examples

#### FASTA input

```bash
python3 abuseqqc.py -i assembly.fna -o fasta_qc.txt
```

#### FASTQ input

```bash
python3 abuseqqc.py -i reads.fastq -o fastq_qc.txt
```

The tool automatically detects the file type and applies the correct analysis.

---

##  Output Examples

### FASTA output

```
FASTA/FASTQ QC REPORT
==============================
Num Sequences       : 13
Min Length          : 4434
Max Length          : 2589240
Mean Length         : 214726.54
N50                 : 2589240
Gc Percent          : 33.0
N Percent           : 0.0
```

### FASTQ output

```
FASTA/FASTQ QC REPORT
==============================
Num Sequences       : 100000
Min Length          : 100
Max Length          : 151
Mean Length         : 150.2
N50                 : 151
Gc Percent          : 52.3
N Percent           : 0.1
Mean Quality        : 34.6
Min Quality         : 20
Max Quality         : 41
```

---

## Use Cases

* Genome assembly quality assessment
* Pre-annotation sequence validation
* FASTQ read quality summarization
* Teaching introductory bioinformatics
* QC workflows in resource-limited laboratories

---

## Citation

If you use **ABUSEqQC** in your research, please cite:

> Musoba, A. (2026). *ABUSEqQC: A FASTA/FASTQ quality control tool with N50 and quality-score analysis*. GitHub repository: [https://github.com/abubakarmusoba/ABUSEqQC](https://github.com/abubakarmusoba/ABUSEqQC)

---

##  Future Development

* FASTQ quality score plots
* Length distribution plots
* HTML QC reports
* Unit tests and CI integration

---

##  License

This project is released under the **MIT License**.

---

##  Author

**Abubakar Musoba**
Molecular Biologist & Bioinformatician
GitHub: [https://github.com/abubakarmusoba](https://github.com/abubakarmusoba)

