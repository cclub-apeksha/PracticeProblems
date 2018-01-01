from datetime import datetime, timedelta
competition = int(input())
print(datetime.now() + timedelta(hours=competition))
print(format(datetime.now() + timedelta(hours=competition), '%H:%M:%S'))