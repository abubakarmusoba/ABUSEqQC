import argparse
from Bio import SeqIO
import numpy as np


def analyze_sequences(input_file):
    # Detect file format
    if input_file.endswith(('.fasta', '.fa', '.fna')):
        fmt = "fasta"
    elif input_file.endswith(('.fastq', '.fq')):
        fmt = "fastq"
    else:
        raise ValueError("Unsupported file type. Use FASTA or FASTQ.")

    lengths = []
    gc_counts = 0
    n_counts = 0
    total_bases = 0

    quality_scores = []

    for record in SeqIO.parse(input_file, fmt):
        seq = str(record.seq)
        length = len(seq)
        lengths.append(length)

        # GC and N counting
        gc_counts += seq.upper().count('G') + seq.upper().count('C')
        n_counts += seq.upper().count('N')
        total_bases += length

        # If FASTQ, collect quality scores
        if fmt == "fastq":
            quality_scores.extend(record.letter_annotations["phred_quality"])

    # Basic stats
    num_sequences = len(lengths)
    min_len = min(lengths)
    max_len = max(lengths)
    mean_len = sum(lengths) / num_sequences

    # N50 calculation
    sorted_lengths = sorted(lengths, reverse=True)
    cumulative = 0
    n50 = 0
    for l in sorted_lengths:
        cumulative += l
        if cumulative >= sum(lengths) / 2:
            n50 = l
            break

    # GC and N %
    gc_percent = (gc_counts / total_bases) * 100
    n_percent = (n_counts / total_bases) * 100

    # FASTQ quality stats (only if FASTQ)
    if fmt == "fastq":
        mean_quality = np.mean(quality_scores)
        min_quality = np.min(quality_scores)
        max_quality = np.max(quality_scores)
    else:
        mean_quality = None
        min_quality = None
        max_quality = None

    return {
        "num_sequences": num_sequences,
        "min_length": min_len,
        "max_length": max_len,
        "mean_length": mean_len,
        "n50": n50,
        "gc_percent": gc_percent,
        "n_percent": n_percent,
        "mean_quality": mean_quality,
        "min_quality": min_quality,
        "max_quality": max_quality
    }


def generate_report(stats, output_file):
    report = []
    report.append("FASTA/FASTQ QC REPORT")
    report.append("==============================")
    report.append(f"Num Sequences       : {stats['num_sequences']}")
    report.append(f"Min Length          : {stats['min_length']}")
    report.append(f"Max Length          : {stats['max_length']}")
    report.append(f"Mean Length         : {stats['mean_length']:.2f}")
    report.append(f"N50                 : {stats['n50']}")
    report.append(f"Gc Percent          : {stats['gc_percent']:.1f}")
    report.append(f"N Percent           : {stats['n_percent']:.1f}")

    # Add quality stats only if FASTQ
    if stats["mean_quality"] is not None:
        report.append(f"Mean Quality        : {stats['mean_quality']:.1f}")
        report.append(f"Min Quality         : {stats['min_quality']}")
        report.append(f"Max Quality         : {stats['max_quality']}")

    with open(output_file, "w") as f:
        f.write("\n".join(report))

    print("\n".join(report))


def main():
    parser = argparse.ArgumentParser(description="FASTA/FASTQ QC tool")
    parser.add_argument("-i", "--input", required=True, help="Input FASTA/FASTQ file")
    parser.add_argument("-o", "--output", required=True, help="Output report file")
    args = parser.parse_args()

    stats = analyze_sequences(args.input)
    generate_report(stats, args.output)


if __name__ == "__main__":
    main()

