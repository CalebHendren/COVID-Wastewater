#Retrieves accessions from metadata
import os
import re

metadata_folder = "C:\\Users\\caleb\\Desktop\\DataProjects\\Python\\COVID_Wastewater\\Metadata"

tennessee_sra_accessions = []

for filename in os.listdir(metadata_folder):
    if filename.endswith(".xml"):
        with open(os.path.join(metadata_folder, filename), "r") as file:
            metadata_xml = file.read()
            sra_matches = re.findall(r"(SRR\d+)", metadata_xml)
            if sra_matches:
                tennessee_sra_accessions.extend(sra_matches)

with open("tennessee_sra_accessions.txt", "w") as file:
    for acc in tennessee_sra_accessions:
        file.write(f"{acc}\n")

print(f"Found {len(tennessee_sra_accessions)} SRA accessions in Tennessee:")
print(tennessee_sra_accessions)
