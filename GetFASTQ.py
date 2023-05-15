import os
import subprocess
from pathlib import Path

sra_toolkit_path = "C:/Softwares/sratoolkit.current-win64/sratoolkit.3.0.1-win64/bin"
sra_accessions_file = "tennessee_sra_accessions.txt"
output_folder = "C:/Users/caleb/Desktop/DataProjects/Python/COVID_Wastewater/FASTQ"

os.makedirs(output_folder, exist_ok=True)

with open(sra_accessions_file, "r") as file:
    accessions = [line.strip() for line in file.readlines()]

# Remove duplicates
unique_accessions = list(set(accessions))

for acc in unique_accessions:
    print(f"Processing SRA accession {acc}")

    home = str(Path.home())
    sra_file = os.path.join(home, "ncbi", "public", "sra", f"{acc}.sra")

    if not os.path.exists(sra_file):
        prefetch_cmd = f"{sra_toolkit_path}/prefetch {acc}"
        subprocess.run(prefetch_cmd, shell=True)

    fastq_folder = "C:/Users/caleb/Desktop/DataProjects/Python/COVID_Wastewater/FASTQ"
    fastq_file_prefix = os.path.join(fastq_folder, acc)
    if not os.path.exists(f"{fastq_file_prefix}_1.fastq.gz") or not os.path.exists(f"{fastq_file_prefix}_2.fastq.gz"):
        fastq_dump_cmd = f"{sra_toolkit_path}/fastq-dump --split-files --gzip -O {fastq_folder} {sra_file}"
        print(f"Running fastq-dump for {acc}")
        subprocess.run(fastq_dump_cmd, shell=True)
        print(f"Finished running fastq-dump for {acc}")

fastq-dump --split-files --gzip --outdir /Users/caleb/Desktop/DataProjects/Python/COVID_Wastewater/FASTQ *.sra