# Use the file name mbox-short.txt as the file name
fname = "C:\\Users\\otavi\\OneDrive\\Documentos\\GitHub\\Progress_Python\\Novo_curso\\Progresso\\Coursera\\03_modulo\\02_3.txt"
with open(fname, 'r') as fh:
    count = 0
    total = 0.0

    for line in fh:
        if not line.startswith("X-DSPAM-Confidence: "):
            continue
        
        line_str = line.replace('X-DSPAM-Confidence: ','').rstrip()
        
        line_float = float(line_str)
        total += line_float
        count += 1

print(total)
print(count)
average = total/count
print(average)