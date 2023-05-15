import os
import xmltodict
import requests
import time
import xml.parsers.expat
import pandas as pd


def get_sra_accession(biosample_accession, retries=3):
    url = f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id={biosample_accession}&retmode=xml'

    for i in range(retries):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = xmltodict.parse(response.content)
                if data is None:
                    print(f"Error: Could not parse XML data for biosample {biosample_accession}")
                    return None

                sra_id = data.get('BioSampleSet', {}).get('BioSample', {}).get('Ids', {}).get('Id')
                if sra_id:
                    sra_accession = None
                    for id_entry in sra_id:
                        if isinstance(id_entry, dict) and id_entry.get('@db') == 'SRA':
                            sra_accession = id_entry.get('#text')
                            break
                    if sra_accession is None:
                        print(f"Error: Could not find SRA accession for biosample {biosample_accession}")
                    return sra_accession
                else:
                    print(f"Error: Could not find SRA id for biosample {biosample_accession}")
                    return None
            else:
                print(f"Error: Could not fetch data for biosample {biosample_accession}. Status code: {response.status_code}")
                return None
        except (requests.exceptions.ChunkedEncodingError, xml.parsers.expat.ExpatError) as e:
            if i < retries - 1:  # If it's not the last retry
                print(f"Error: {e} for biosample {biosample_accession}. Retrying...")
                time.sleep(1)  # Add a delay before retrying
                continue
            else:
                print(f"Error: {e} for biosample {biosample_accession}")
                return None

def download_sra_files(sra_accessions, sra_toolkit_path):
    for sra_accession in sra_accessions:
        print(f'Downloading {sra_accession}...')
        os.system(f'{sra_toolkit_path} prefetch {sra_accession}')

def main():
    sra_toolkit_path = 'C:/Softwares/sratoolkit.current-win64/sratoolkit.3.0.1-win64/bin/prefetch.exe'
    biosample_file = 'biosample_result.txt'

    with open(biosample_file, 'r') as f:
        biosample_accessions = f.read().splitlines()

    sra_accessions = []
    for biosample_accession in biosample_accessions:
        sra_accession = get_sra_accession(biosample_accession)
        if sra_accession:
            sra_accessions.append(sra_accession)
        time.sleep(1)  # Add a delay between requests

    download_sra_files(sra_accessions, sra_toolkit_path)

if __name__ == '__main__':
    main()
