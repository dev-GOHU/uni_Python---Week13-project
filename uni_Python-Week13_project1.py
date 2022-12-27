import shutil
import os

if not os.path.isdir('textFile'):
    os.mkdir('textFile/')
if not os.path.isdir('textFile/1'):
    os.mkdir('textFile/1/')

############### 한글 파일 ##############
KFile1 = open('textFile/1/KoreanFile1.txt', 'w', encoding = 'utf-8')
KFile2 = open('textFile/1/KoreanFile2.txt', 'r', encoding = 'utf-8')

while True:
    outStr = input()
    if outStr != "":
        KFile1.writelines(outStr+'\n')
    else:
        break
        
KFile1.close()
KFile1 = open('textFile/1/KoreanFile1.txt', 'r', encoding = 'utf-8')
        
KFile1Lines = KFile1.readlines()
KFile2Lines = KFile2.readlines()

print("한국어 파일 1")
for line1 in KFile1Lines:
    print(line1, end='')

    
print("\n한국어 파일 2")
for line2 in KFile2Lines:
    print(line2, end='')

KFile1.close()
KFile2.close()

########## 영어 파일 ############
EFile1 = open('textFile/1/EnglishFile1.txt', 'r')
EFile2 = open('textFile/1/EnglishFile2.txt', 'r')

print("\n\n영어파일 1")
for line1 in EFile1.readlines():
    print(line1, end='')

print("\n\n영어 파일 2")
for line2 in EFile2.readlines():
    print(line2, end='')

EFile1.close()
EFile2.close()
