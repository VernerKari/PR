students={'Johny','Billo','Steven','Kendrik','Aron'}
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students_2=list(students)
students_2.sort()
stud_1=sum(grades[0])/len(grades[0])
stud_2=sum(grades[1])/len(grades[1]),
stud_3=sum(grades[2])/len(grades[2]),
stud_4=sum(grades[3])/len(grades[3]),
stud_5=sum(grades[4])/len(grades[4])
grades_2=[stud_1,stud_2,stud_3,stud_4,stud_5]



students_2.append('Maikl')
grades.append([4,3,2,4,5])

pro=dict(zip(students_2,grades_2))
print(pro)
