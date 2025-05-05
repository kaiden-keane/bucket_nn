import os

l = 'labels2'

for file_name in os.listdir(l):
    file_path = os.path.join(l, file_name)

    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        parts = line.strip().split()
        for i in range(1, len(parts)):
            if  float(parts[i]) < 0:
                parts[i]=str(0)
                print(file_name)
            elif float(parts[i]) > 1:
                parts[i]=str(1)
                print(file_name)
        new_lines.append(" ".join(parts))
    with open(file_path, 'w') as f:
        for line in new_lines:
            f.write(line + "\n")
    
