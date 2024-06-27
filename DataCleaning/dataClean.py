import pandas as pd
import re
import os

# List files in the current directory to verify the presence of the input file
print(os.listdir())

# Read the transcript data from the text file
with open('TranscriptionText.txt', 'r') as file:
    data = file.readlines()

# Create a DataFrame
df = pd.DataFrame(data, columns=['raw_text'])

# Define a function to clean the transcript data
def clean_transcript(row):
    # Remove speaker tags and timestamps
    cleaned_text = re.sub(r"Ses\d{2}[MF]_script\d{2}_\d_[MF]\d{3} \[\d{3}\.\d{4}-\d{3}\.\d{4}\]: ", "", row)
    cleaned_text = re.sub(r"Ses\d{2}[MF]_impro\d{2}_[MF]\d{3} \[\d{3}\.\d{4}-\d{3}\.\d{4}\]: ", "", cleaned_text)
    # Replace special sequences and strip leading/trailing whitespace
    cleaned_text = cleaned_text.replace("  ", " ").strip()
    return cleaned_text

# Apply the cleaning function to the DataFrame
df['cleaned_text'] = df['raw_text'].apply(clean_transcript)

# Filter out any empty strings resulting from the cleaning
df = df[df['cleaned_text'] != ""]

# Write the cleaned data to a new text file
with open('cleaned_transcript.txt', 'w') as file:
    for line in df['cleaned_text']:
        file.write(line + '\n')

# Print the cleaned data for verification
with open('cleaned_transcript.txt', 'r') as file:
    cleaned_data = file.read()

print(cleaned_data)
