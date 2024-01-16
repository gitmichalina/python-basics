import pytz
from datetime import datetime

u = pytz.utc
k = pytz.timezone('Asia/Kolkata')
print('UTC Time =', datetime.now(tz=u))
print('Asia Time =', datetime.now(tz=k))

# UTC Time = 2024-01-16 14:43:28.432714+00:00
# Asia Time = 2024-01-16 20:13:28.432714+05:30