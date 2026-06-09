# write method()
# filename=open("sample.txt","w")
# print(filename.write("Hey learn Python"))
# filename.close()

# read method()
# filename=open("sample.txt","r")
# print(filename.write("Hey learn Python"))
# print(filename.read())
# filename.close()

# filename = open("sample.txt", "a+")
# filename.seek(0)          
# print(filename.read())    
# filename.close()


# filename=open("sample.txt","w+")
# print(filename.write("Hey learn Python"))
# filename.seek(0)
# print(filename.read())
# filename.close()

# filename=open("sample.txt","r+")
# print(filename.write("Hey learn Python"))
# filename.seek(0)
# print(filename.read())
# filename.close()

# filename=open("sample.txt","r")
# filename.seek(0)
# print(filename.read())
# filename.close()

# create a file as example.txt with the content of u selfintro using file modes r and w
# find lenth of file
# find the target is found or not
# find the number of vowels 
# update the contact number to file

# f=open("Example.txt","w+")
# print(f.write('''Goodafternoon I am Baby
#               I am currently pursuring B.tch final year in the
#               stream of AIML'''))
# f.seek(0)
# if "Baby" in f.read():
#     print("YES")
# else:
#     print("NO")
# f=open("Example.txt","w+")
# print(f.write('''Goodafternoon I am Baby
#                I am currently pursuring B.tch final year in the
#                stream of AIML'''))
# f.seek(0)
# e=f.read()
# vowels=0
# w="aeiouAEIOU"
# for ch in e:
#     if ch in w:
#         vowels+=1
#     else:
#         vowels+=0
# print("VOWELS:",vowels) 

# print(f.write("  Contact Number:8523077662"))
# f.seek(0)
# f.read()
# f.close()


# import csv
# with open("students.csv","w+",newline="") as file:
#     r=csv.writer(file)
#     r.writerow(["name","ID"])
#     r.writerow(["BABY","6142"])
#     # file.flush() 
#     file.seek(0)
#     b=csv.reader(file)
#     for i in b:
#         print(i)

# create a csv file employee with name id and salary
# import 10 emp detalisusing write mode
# 1.)print all the emp_details
# find the highest salary
# find the avg salary
# print the count of emps whose salary is > than avg  salary
 
import csv
with open("Employee.csv","w+",newline="") as file:
    r=csv.writer(file)
    r.writerow(['name','id','salary'])
    r.writerow(['Baby','6142','50000'])
    r.writerow(['mouni','6126','52000'])
    r.writerow(['keerthi','6131','53000'])
    r.writerow(['sony','6160','51000'])
    r.writerow(['namina','6148','50000'])
    r.writerow(['usha','6149','56000'])
    r.writerow(['jas','6163','57000'])
    r.writerow(['Aswini','614','58000'])
    r.writerow(['Param','6144','60000'])
    
    file.seek(0)
    b=csv.reader(file)
    salaries=[]
    for row in b:
        if row[2].isdigit():
            salaries.append(int(row[2]))
    max_salary=max(salaries)
    print("Maximum Salary:",max_salary)
    avg=sum(salaries)//len(salaries)
    
    print("AVERAGE:",avg)

    file.seek(0)
    b=csv.reader(file)
    count=0
    for i in salaries:
        if salaries[i]>=avg:
            count+=1
    print("COUNT OF SALARY:",count)
    for i in b:
        print(i)

