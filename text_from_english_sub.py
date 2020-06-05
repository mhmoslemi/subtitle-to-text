raw_sub=[]
in_1=open('input_file.txt', 'r' ,encoding='utf8')
input_file=in_1.readline().strip()
in_1.close()
if input_file[-3:]!='srt':
    input_file=input_file+'.srt'
    
    
input_sub=open(input_file, 'r' ,encoding='utf8')
x=input_sub.readline()
while(x):
    try:
        x=input_sub.readline()
        raw_sub.append(x)
    except:
        break
input_sub.close()


sub_text=[]       
for row in raw_sub:
    try:
        if  row[2]!=':' :
            try:
                int(row.strip())
            except:
                if row.strip():
                    sub_text.append(row.rstrip())
    except:
        pass

output_text=input_file.rstrip('.srt')+'.txt'
fop=open(output_text,'w')
i=0
for row in sub_text:
    try:
        fop.write(row+'\n')
        i+=1
    except:
        pass
fop.close()