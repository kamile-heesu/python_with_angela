# π¨ Don't change the code below π
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# π¨ Don't change the code above π


#Write your code below this row π

# for loopμ μ΄μ©ν΄μ νκ· κ°μ κ΅¬νμΈμ.

# μ μλ‘ λ°μλ£νμΈμ.

# len() μ΄λ sum() μ μ¬μ©νμ§ λ§μΈμ. 

print(student_heights)

# 157 183 167 160 163 148
sum = 0;
index = 0;
for student in student_heights:
  sum = sum + student;
  index = index + 1;
print(f"sum : {sum} \n length : {index}")
average = round(sum / index);
print(average)




