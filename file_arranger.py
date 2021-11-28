import os
import os.path
import shutil
import datetime

extension=['.py','.txt','.jpeg','.zip','.php','.html','.c','.c++','.doc','.pdf','.png','.mp4']
file_name_list  = ['Python','Text Files','Images','ZIP','PHP files','HTML files','C Files','C++ Files','Doc files','PDF files','Images','Videos']

print("Hello !!! Welcome to File Organizer")
print()

x=0
while x !=1:
    origin_input = input("Enter Origin Path :- ")
    try:
        os.chdir(origin_input)
        x=1
    except:
        x=0
        print("Invalid input path ")

path = os.listdir()
x=0
while x!=1:
    destination_input = input("Destination path :- ")
    try:
        os.chdir(destination_input)
        x=1
    except:
        x=0
        print("Invalid Destination path")


print("#########################################################")
print("Choose any how file should be orgonized?")
print("1.For category wise like (Images , Python ,Videos )")
print("2.For extension wise like (jpg,png,mp3,mp4,mkv)")
print("3.For (YYYY -> Month -> Week) nested structure ")
choice = int(input(" -> "))
print("#########################################################")

if(choice == 1):
    for i in path:
        skip = 0
        try:
            slice_var=i.index('.')
        except:
            skip = 1
        if skip ==0:
            extracted_extension = i[slice_var:]
        
            if extracted_extension in extension:
                pos=extension.index(extracted_extension)
                folder_name = file_name_list[pos]
                if not os.path.isdir(folder_name):
                    os.mkdir(folder_name)
                try:
                    shutil.move(f"{origin_input}/{i}",f'/{folder_name}')
                except:
                    print(f"{i} is already exists on {folder_name}")

elif choice ==2:
    for i in path:
        temp = i.index('.')
        folder_name  = i[temp+1:]
        if  not os.path.isdir(folder_name):
            os.mkdir(folder_name)
            shutil.move(f"{origin_input}/{i}",f"{destination_input}/{folder_name}")
        else:
            shutil.move(f"{origin_input}/{i}",f"{destination_input}/{folder_name}")

elif choice ==3:
    d = {}
    for i in path:
        
        time = str(datetime.datetime.fromtimestamp(os.path.getmtime(f"{origin_input}/{i}")))[0:11]
        if time in d.keys():
            d[time].append(i)
        else:
            d[time] = []
            d[time].append(i)
    if not os.path.isdir('Sorted_by_date_time'):
        os.mkdir("Sorted_by_date_time")
    os.chdir('Sorted_by_date_time')
 
    for i in d.keys():
        if not os.path.isdir(i[0:4]):
            os.mkdir(i[0:4])
        os.chdir(i[0:4])
        if not os.path.isdir(i[6:7]):
            os.mkdir(i[6:7])
        os.chdir(i[6:7])
        if not os.path.isdir(i[8:]):
            os.mkdir(i[8:])
       
        for j in range(0,len(d[i])):
           
            try:
                shutil.move(f"{origin_input}/{d[i][j]}",f"{destination_input}/Sorted_by_date_time/{i[0:4]}/{i[6:7]}/{i[8:10]}/")
            except Exception as e:
                pass
        os.chdir(f"{destination_input}/Sorted_by_date_time/")
else:
    print("Invalid Choice ")
        