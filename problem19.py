import datetime

startDate = datetime.date(1901,1,1)
endDate = datetime.date(2000,12,31)

day = datetime.timedelta(days=1)

sundays = 0

while startDate <= endDate:
	if startDate.weekday() == 6 and startDate.day == 1:
		sundays += 1
	startDate+=day

print sundays
