import requests
import datetime
EN_START_DATE = datetime.date(2022, 9, 18)
def get_answer(day):
    return requests.get(f"https://api.contexto.me/machado/en/giveup/{day}").json()["word"]
for day in range((datetime.date.today() - EN_START_DATE).days+1):
    answer = get_answer(day)
    print (f"{answer} - {day}")
    with open("English.txt", "a+") as f:
        f.write(f"{answer} - {day}\n")
with open("English.txt", 'r') as f:
    print (f"Finished writing {len(f.readlines())-1} lines")