name = input("Enter your name :")
age = int(input("Enter your age: "))
uni = input ("Enter the name of your university :")
degree = input ("Enter the name of the degree :")
dream_job = input ("What is your dream job :")
gpa = float(input ("Enter your GPA :"))
country =input ("Name of country :")
fav_language = input ("Enter your favorite programming language :")
# All the needed information is being extracted from the user
name = name.capitalize()
uni = uni.capitalize()
degree = degree.capitalize()
dream_job = dream_job.capitalize()
country = country.capitalize()
fav_language = fav_language.capitalize()


print ("")
print ("")
print ("")

print("==================================")
print("       STUDENT PROFILE MANAGER")
print("==================================")
print ("name             : ",name)
print ('age              : ',age)
print ('university       : ',uni )
print ('degree           : ',degree)
print ('dream job        : ',dream_job)
print ('gpa              : ',gpa )
print("country           : ", country)
print("favorite language : ", fav_language)
print ("")
print ("")
# The details her being displayed in a orderly fashion

print("----------------------------------")


print (f"THANK YOU {name}!")
print(f"Good luck becoming a {dream_job}")
print ("Have a wonderful delighted day")
# A personalized thank you message 

print ("next year you will turn ",age+1)

if age < 25 :
    print("You are early in your career!!")
else:
    print("Keep growing and learning!")

if gpa > 3.5 :
    print ("Excellent GPA! Keep it up.")
else :
    print("Focus on improving your skills.")