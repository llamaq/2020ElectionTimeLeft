import datetime

def GetDaysLeft(target = "2020-10-03"):
    currentDay = datetime.date.today()
    target = datetime.date.fromisoformat(target)
    return (target - currentDay).days

print(f"{GetDaysLeft()} days left until election day!")
