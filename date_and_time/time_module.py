import time

t = time.time()
print(t)

# 1631509053.0120902
# The cited example prints ticks from January 1, 1970

local_t = time.localtime(time.time())
print(local_t)
# time.struct_time(tm_year=2024, tm_mon=1, tm_mday=16, tm_hour=15,
# tm_min=30, tm_sec=21, tm_wday=1, tm_yday=16, tm_isdst=0)

print(time.timezone)
# -3600

print(time.tzname)
# ('Środkowoeuropejski czas stand.', 'Środkowoeuropejski czas letni')