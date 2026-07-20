

def welcome():
    print("==================================")
    print("       STUDENT PROFILE MANAGER")
    print("==================================")



def get_details():

    name = input("Enter your name : ")
    age = int(input("Enter your age: "))
    uni = input ("Enter the name of your university : ")
    degree = input ("Enter the name of the degree : ")
    dream_job = input ("What is your dream job : ")
    gpa = float(input ("Enter your GPA : "))
    country =input ("Name of country : ")
    fav_language = input ("Enter your favorite programming language : ")
    # All the needed information is being extracted from the user
    name = name.capitalize()
    uni = uni.capitalize()
    degree = degree.capitalize()
    dream_job = dream_job.capitalize()
    country = country.capitalize()
    fav_language = fav_language.capitalize()

    return name, age, uni, degree, dream_job, gpa, country, fav_language
    


def display_profile(name, age, uni, degree, dream_job, gpa, country, fav_language):

    print ("")
    print ("")
    print ("")

    print(f"Name             : {name}")
    print(f"Age              : {age}")
    print(f"University       : {uni}")
    print(f"Degree           : {degree}")
    print(f"Dream Job        : {dream_job}")
    print(f"GPA              : {gpa}")
    print(f"Country          : {country}")
    print(f"Favorite Language: {fav_language}")



    print("----------------------------------")



def show_feedback(name, dream_job, age, gpa):

    print(f"THANK YOU {name}!")
    print(f"Good luck becoming a {dream_job}")
    print("Have a wonderful delightful day")

    print(f"Next year you will turn {age+1}")

    if age < 25:
        print("You are early in your career!!")
    else:
        print("Keep growing and learning!")

    if gpa > 3.5:
        print("Excellent GPA! Keep it up.")
    else:
        print("Focus on improving your skills.")




def main():
    welcome()

    name, age, uni, degree, dream_job, gpa, country, fav_language = get_details()

    display_profile(name, age, uni, degree, dream_job, gpa, country, fav_language)

    show_feedback(name, dream_job, age, gpa)


main()