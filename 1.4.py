from datetime import datetime

start = input("Enter the start date in Year Month Day Hour:Minute:Second format: ")
end = input("Enter the end date in Year Month Day Hour:Minute:Second format: ")

s_datetime = datetime.strptime(start, "%Y %m %d %H:%M:%S")
e_datetime = datetime.strptime(end, "%Y %m %d %H:%M:%S")

difference = int((e_datetime - s_datetime).total_seconds())

print(difference)
