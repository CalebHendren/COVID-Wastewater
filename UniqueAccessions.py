# Open the input file for reading
with open('tennessee_sra_accessions.txt', 'r') as f:
    # Read in the contents of the file
    lines = f.readlines()

# Convert the lines to a set to remove duplicates, then back to a list
unique_lines = list(set(lines))

# Open the output file for writing
with open('tennessee_sra_accessions_unique.txt', 'w') as f:
    # Write the unique lines to the output file
    f.writelines(unique_lines)
