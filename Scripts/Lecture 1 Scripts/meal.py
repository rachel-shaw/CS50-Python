"""
GOALS:
- breakfast: 7am - 8 am
- lunch: 12pm - 1pm
- dinner: 6pm - 7pm
- implement a program that prompts the user for a time
- outputs whether it is breakfast time, lunch time, or dinner time
- if not time, output nothing
- assume time formatted in 24-hour time #:## or ##:##
- assume each meal time range is inclusive
- convert function converts time, a string in 24hour format, to num of hours as float
"""

# def main():
#     userinput = input("What time is it? ")

#     if 7 <= convert(userinput) <= 8:
#         print("breakfast time")
#     elif 12 <= convert(userinput) <= 13:
#         print("lunch time")
#     elif 18 <= convert(userinput) <= 19:
#         print("dinner time")

# def convert(time):
#     hours, minutes = time.split(":")

#     totaltime = ((float(hours)) + (float(minutes)/60))

#     return totaltime    


# if __name__ == "__main__":
#     main()



def main():
    userinput = input("What time is it? ").strip().lower().replace(".", "")

    if userinput.endswith("am") or userinput.endswith("pm"):
        if 7 <= ampmconvert(userinput) <= 8:
            print("breakfast time")
        elif 12 <= ampmconvert(userinput) <= 13:
            print("lunch time")
        elif 18 <= ampmconvert(userinput) <= 19:
            print("dinner time")
    
    else:
        if 7 <= convert(userinput) <= 8:
            print("breakfast time")
        elif 12 <= convert(userinput) <= 13:
            print("lunch time")
        elif 18 <= convert(userinput) <= 19:
            print("dinner time")

def convert(time):
    hours, minutes = time.split(":")

    totaltime = float(hours) + float(minutes)/60

    return totaltime    

def ampmconvert(timeb):
    if "pm" in timeb:
        adjustedtime = timeb.replace("pm", "").strip()
        hours, minutes = adjustedtime.split(":")

        totaltime = (float(hours)+12) + float(minutes)/60
        return totaltime 
       
    elif "am" in timeb:
        adjustedtime = timeb.replace("am", "").strip()
        hours, minutes = adjustedtime.split(":")

        totaltime = float(hours) + float(minutes)/60
        return totaltime    


if __name__ == "__main__":
    main()

