import re

# Open input file in read mode and read contents
with open('input.txt', 'r', encoding='utf-8') as f_in:
    text = f_in.read()

# Remove line breaks before timestamps
text = re.sub(r'\n(\d|:)', r'\1', text)

# Remove timestamps (H:M or H:M:S)
text = re.sub(r'\d+:\d+(?::\d+)?', '', text)

# Write modified text to output file
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text)
