from Bio import Entrez
import xml.etree.ElementTree as ET
Entrez.email = "calebahendren@gmail.com"


def get_sra_accessions(query):
    search_handle = Entrez.esearch(db="sra", term=query, retmax=1000)
    search_results = Entrez.read(search_handle)
    search_handle.close()
    return search_results["IdList"]


def get_sra_metadata(accession):
    fetch_handle = Entrez.efetch(db="sra", id=accession, retmode="xml")
    metadata_xml = fetch_handle.read()
    fetch_handle.close()
    return metadata_xml


project_id = "PRJNA839090"
accessions = get_sra_accessions(f"{project_id}[Project] AND Tennessee[All Fields]")
print(f"Found {len(accessions)} SRA accessions for project {project_id} in Tennessee:")

#Save accessions to a text file
with open("tennessee_sra_accessions.txt", "w") as accession_file:
    for acc in accessions:
        accession_file.write(f"{acc}\n")

#Save metadata to Excel files
for acc in accessions:
    metadata_xml = get_sra_metadata(acc)
    with open(f"metadata_{acc}.xml", "w", encoding='utf-8') as metadata_file:
        metadata_file.write(metadata_xml.decode('utf-8'))
