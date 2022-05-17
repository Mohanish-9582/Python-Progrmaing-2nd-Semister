print("Subjects         Total Marks         Marks Obtained")
e = int(input('EEE               100                  '))
s = int(input('SON               100                  '))
a = int(input('AM                100                  '))
l = int(input('LDC               100                  '))
c = int(input('CDE               100                  '))
t = e + s + a + l + c
per = (t * 100) / 500
print("You have got percentage: ", per)
if per > 75:
    print("---- Congratulations! You have passed the exam and achieved Distinction Grade ----")
elif 60 <= per < 75:
    print("---- Congratulations! You have passed the exam and achieved First Division Grade ----")
elif 50 <= per < 60:
    print("---- Congratulations! You have passed the exam and achieved Second Division Grade ----")
elif 40 <= per < 50:
    print("---- Congratulations! You have passed the exam and achieved Third Division Grade ----")
else:
    print("**** Sorry! You are Fail in the Exam and Got Percentage less than 40****")
