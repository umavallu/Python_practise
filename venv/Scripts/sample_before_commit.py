def file_write(file_name):
    f=open(file_name,'a+')
    l=input('enter what you want to write into the file: ').split(" ")
    for i in l:
        f.writelines(i+' ')
def name_print(file_name):
    f=open(file_name,'r')
    l=[]
    i=f.readline()
    while i!=' ':
        if i==' ':
            break
        else:
            l.append(i)
            i=f.readline()
    return l