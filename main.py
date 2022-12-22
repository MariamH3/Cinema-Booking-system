import os.path

open("movie 1.","a")
open("movie 2.","a")
open("movie 3.","a")
open("user","a")
print("Welcome!")
x=input("1.Sign in\n2.Sign up\n")
if x=="1":
    id=input("Enter your ID\n")#append in file
    if os.path.exists(id)==True:
        name = input("Enter your name\n")
        email = input("Enter your email\n")
        password = input("Enter your password\n")
        ln = open(id, "r")
        if id == "1":
            print("Welcome Admin!")
            p = input("Add a new movie?\n y or n\n")
            if p == "n":
                print("your current movies are:\n1.Asl Eswed\n2.SpiderMan\n3.Harry Potter\nThank You!")
            if p == "y":
                id_movie = input("Enter Movie ID Betwen 10 and 20")
                name = input("Enter Movie name\n")
                desc = input("Enter Movie description\n")
                r1 = open(id_movie, "a")
                r1.write("ID:" + id + "\nMovie name:" + name + "\nDescription:" + desc)
        else:
            y = input("Please choose a movie from the following:\n1.Asl Eswed\n2.SpiderMan\n3.Harry Potter")
            if y == "1":
                m = open("movie 1", "r")
                m1 = ["1", "2", "3", "4"]
                Lines = m.read()
                print(Lines, "availble seats", m1)
                print("your seat is no.", m1[0])
                f1 = open(id, "a")
                f1.write("\nYuor ticket no.is " + m1[0])
                m1.pop(0)
                print("remaining seats are", m1)
                i = open("m1", "a")
            if y == "2":
                m = open("movie 2", "r")
                m1 = ["1", "2", "3", "4"]
                Lines = m.read()
                print(Lines, "availble seats", m1)
                print("your seat is no.", m1[2])
                f1 = open(id, "a")
                f1.write("\nYuor ticket no.is " + m1[2])
                m1.pop(2)
                print("remaining seats are", m1)
                i = open("m1", "a")
            if y == "3":
                m = open("movie 3", "r")
                m1 = ["1", "2", "3", "4"]
                Lines = m.read()
                print(Lines, "availble seats", m1)
                print("your seat is no.", m1[3])
                f1 = open(id, "a")
                f1.write("\nYuor seat no. is " + m1[3])
                m1.pop(3)
                print("remaining seats are", m1)
    else:print("Please check your id or try to sign up")
if x=="2":
    id=input("Please choose a ID between 3 and 9\n")#append in file
    name=input("Enter your name\n")
    email=input("Enter your email\n")
    password=input("Enter your password\n")
    f1= open(id,"a")
    f1.write("ID:"+id+"\nName:"+name+"\nEmail:"+email+"\nPassword:"+password)
    y=input("Please choose a movie from the following:\n1.Asl Eswed\n2.SpiderMan\n3.Harry Potter")
  # if y=="1":
    if y == "1":
        m = open("movie 1", "r")
        m1 = ["1", "2", "3", "4"]
        Lines = m.read()
        print(Lines, "availble seats", m1)
        print("your seat is no.", m1[0])
        f1 = open(id, "a")
        f1.write("\nYuor ticket no.is " + m1[0])
        m1.pop(0)
        print("remaining seats are", m1)
        i = open("m1", "a")
    if y == "2":
        m = open("movie 2", "r")
        m1 = ["1", "2", "3", "4"]
        Lines = m.read()
        print(Lines, "availble seats", m1)
        print("your seat is no.", m1[2])
        f1 = open(id, "a")
        f1.write("\nYuor ticket no.is " + m1[2])
        m1.pop(2)
        print("remaining seats are", m1)
        i = open("m1", "a")
    if y == "3":
        m = open("movie 3", "r")
        m1 = ["1", "2", "3", "4"]
        Lines = m.read()
        print(Lines, "availble seats", m1)
        print("your seat is no.", m1[3])
        f1 = open(id, "a")
        f1.write("\nYuor ticket no.is " + m1[3])
        m1.pop(3)
        print("remaining seats are", m1)
