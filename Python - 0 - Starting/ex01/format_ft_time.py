import time
import datetime

print(f"Seconds since January 1, 1970: {time.time():,.4f} or \
{time.time():.2e} in scientific notation")
print(f"{datetime.datetime.now():%b %d %Y}")
