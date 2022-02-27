from datetime import date

todayfy = date.today()
todayfy = str(todayfy)
todayfy = todayfy.split("-")

today = ["","",""]
today[0] = todayfy[2]
today[1] = todayfy[1]
today[2] = todayfy[0]



print(today)