import shutil
import os
if not os.path.isdir('textFile/2'):
    os.mkdir('textFile/2/')
if not os.path.isdir('textFile/2/2-1'):
    os.mkdir('textFile/2/2-1/')
if not os.path.isdir('textFile/2/2-2'):
    os.mkdir('textFile/2/2-2/')
    
################## 2 ###################

inFile = open('textFile/2/2-1/text2.txt','r', encoding = 'utf-8')
outFile = open('textFile/2/2-2/text2.txt', 'w', encoding = 'utf-8')

print('원본 파일')

for line in inFile.readlines():
    print(line, end='')
    outFile.writelines(line)
    
inFile.close()
outFile.close()

outFile = open('textFile/2/2-2/text2.txt', 'r', encoding = 'utf-8')
print('\n\n복제된 파일')
for line in outFile.readlines():
    print(line, end='')
    
outFile.close()
