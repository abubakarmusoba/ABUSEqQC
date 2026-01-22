#!/usr/bin/env python3

import argparse
from Bio import SeqIO
from statistics import mean
def calculate_n50(lengths):
    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    cumulative = 0

    for length in sorted_lengths:
        cumulative += length
        if cumulative >= total_length / 2:
            return length

def analyze_sequences(input_file):
    lengths = []
    gc_counts = []
    n_counts = []
    total_bases = 0

    for record in SeqIO.parse(input_file, "fasta"):
        seq = str(record.seq).upper()
        length = len(seq)

        lengths.append(length)
        total_bases += length
        gc_counts.append(seq.count("G") + seq.count("C"))
        n_counts.append(seq.count("N"))

    if not lengths:
        raise ValueError("No sequences found in file.")

    n50 = calculate_n50(lengths)

    return {
        "num_sequences": len(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "mean_length": round(mean(lengths), 2),
        "n50": n50,
        "gc_percent": round(sum(gc_counts) / total_bases * 100, 2),
        "n_percent": round(sum(n_counts) / total_bases * 100, 2),
    }


    return {
        "num_sequences": len(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "mean_length": round(mean(lengths), 2),
        "n50": n50,
        "gc_percent": round(sum(gc_counts) / total_bases * 100, 2),
        "n_percent": round(sum(n_counts) / total_bases * 100, 2),
    }


def write_report(stats, output_file):
    with open(output_file, "w") as out:
        out.write("FASTA/FASTQ QC REPORT\n")
        out.write("=" * 30 + "\n")
        for key, value in stats.items():
            out.write(f"{key.replace('_',' ').title():20}: {value}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Simple FASTA/FASTQ Quality Control Tool"
    )
    parser.add_argument(
        "-i", "--input", required=True, help="Input FASTA/FASTQ file"
    )
    parser.add_argument(
        "-o", "--output", required=True, help="Output report file"
    )

    args = parser.parse_args()

    stats = analyze_sequences(args.input)
    write_report(stats, args.output)

    print("Analysis complete!")
    print(f"Report written to: {args.output}")

if __name__ == "__main__":
    main()

