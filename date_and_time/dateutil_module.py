from datetime import *
from dateutil.relativedelta import *
import calendar as c

NOW = datetime.now()
# Next month
print(NOW + relativedelta(months=+1))
# Next month, plus one week
print(NOW + relativedelta(months=+1, weeks=+1))
# Next month, plus one week, at 5 PM
print(NOW + relativedelta(months=+1, weeks=+1,
                          hour=17))

print(c.leapdays(1920, 2020))
print(date.today())

# 2024-02-16 15:47:04.682734
# 2024-02-23 15:47:04.682734
# 2024-02-23 17:47:04.682734
# 25
# 2024-01-16
