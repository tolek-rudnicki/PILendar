from datetime import date

todayfy = date.today()
todayfy = str(todayfy)
todayfy = todayfy.split("-")

temp = ["","",""]
temp[0] = todayfy[2]
temp[1] = todayfy[1]
temp[2] = todayfy[0]

print(temp)