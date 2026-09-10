program_name = "Leap year finder"
print("="*len(program_name))
print(program_name)
print("="*len(program_name))
print()
User_input = int(input("Enter Year : "))
if User_input%4 ==0:
    if User_input%100 != 0:
        print(f"{User_input} Leap Year")
    else:
        if User_input%400 ==0:
            print(f"{User_input} Leap Year")
        else:
            print(f"{User_input} Not a leap year")
else:
    print(f"{User_input} Not a leap year")