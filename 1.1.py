from datetime import datetime, timedelta

currentdate = datetime.now()

fivedaysbefore = datetime.now() - timedelta(5)

print(fivedaysbefore)
