"""

Start
Get numbers of sheets
Sheets / 5
Round answer to next number
Output to user
End

"""



def calculate(sheet):
    answer = sheet / 5
    rounded_answer = round(answer)

    print("Sheet is: ", sheet)
    print("The answer is: ", answer)
    print("Rounded is: ", rounded_answer)
    print("=====================")
    return rounded_answer

output = calculate(1000)

print("The return statement is: ", output)