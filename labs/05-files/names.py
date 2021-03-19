path="S:/Daten/pythonworkspace/pythonlearn/labs/05-files/"
filein=path+"names.txt"
fileout=path+"names_sorted.txt"

with open(filein,"r") as fin:
    linesstr = fin.read()

print(linesstr)
lines=linesstr.split()
srt_lines=sorted(lines)
print(srt_lines)
srt_linestr="\n".join(srt_lines)
print(srt_linestr)
with open(fileout,"w") as fout:
    fout.write(srt_linestr)