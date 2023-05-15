import os

sra_folder = r"C:\Users\caleb\Desktop\DataProjects\Python\COVID_Wastewater\SRACache\sra"

for file in os.listdir(sra_folder):
    if file.endswith(".sra"):
        sra_name = os.path.splitext(file)[0]
        print(f"fastq-dump --split-files --gzip {sra_name}")
