# ABUSEqQC

**ABUSEqQC** is a lightweight, command-line quality control (QC) tool for **FASTA and FASTQ** sequence files, designed for molecular biologists and bioinformaticians working in low- and middle-resource laboratory environments. The tool provides essential sequence statistics commonly required before downstream analyses such as assembly, annotation, or comparative genomics.

ABUSEqQC is written in **Python 3** and uses **Biopython**, making it easy to extend, audit, and integrate into existing bioinformatics workflows.

---

## ✨ Features

* Supports **FASTA (.fasta, .fa, .fna)** and **FASTQ (.fastq, .fq)** files
* Calculates core QC statistics:

  * Number of sequences
  * Minimum, maximum, and mean sequence length
  * **N50** statistic
  * GC content (%)
  * Ambiguous base (N) content (%)
* Simple command-line interface (CLI)
* Suitable for bacterial genomes, contigs, scaffolds, and raw reads

---

## 🧪 Installation

### 1️⃣ Requirements

* Python **≥ 3.8** (tested on Python 3.12)
* Biopython

### 2️⃣ Install Biopython

```bash
pip install biopython
```

### 3️⃣ Clone the Repository

```bash
git clone https://github.com/abubakarmusoba/ABUSEqQC.git
cd ABUSEqQC
```

---

## 🚀 Usage

Run ABUSEqQC from the terminal using:

```bash
python3 abuseqqc.py -i <input_file> -o <output_report.txt>
```

### Example

```bash
python3 abuseqqc.py -i regan1.fna -o qc_report.txt
```

---

## 📄 Output Example

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

---

## 📌 Notes

* FASTQ **quality score statistics** are not yet implemented and may be added in future versions.
* Designed to work efficiently on standard desktop or laptop computers.

---

## 🧬 Intended Use Cases

* Genome assembly quality assessment
* Pre-annotation sequence validation
* Teaching bioinformatics fundamentals
* QC for sequencing data in resource-limited settings

---

## 📚 Citation

If you use **ABUSEqQC** in your research, please cite:

> Musoba, A. (2026). *ABUSEqQC: A lightweight FASTA/FASTQ quality control tool for molecular biology and bioinformatics*. GitHub repository: [https://github.com/abubakarmusoba/ABUSEqQC](https://github.com/abubakarmusoba/ABUSEqQC)

---

## 🤝 Contributing

Contributions, bug reports, and feature requests are welcome. Please open an issue or submit a pull request via GitHub.

---

## 📜 License

This project is released under the **MIT License**.

---

## 👤 Author

**Abubakar Musoba**
Molecular Biologist & Bioinformatician
GitHub: [https://github.com/abubakarmusoba](https://github.com/abubakarmusoba)
