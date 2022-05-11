import os
username = os.getlogin()
from datetime import datetime
now = datetime.now()
current_date = datetime.today().strftime('%b-%d-%Y')
current_time = now.strftime("%H:%M %p")
local_now = now.astimezone()
local_tz = local_now.tzinfo
local_tzname = local_tz.tzname(local_now)
more_lines = [username, " , ",current_date," , ",current_time, " ", local_tzname]
fpath = '//netapp3/Cust Repairs/Engineering/One-Off group/REPAIR/18_QCPC_Turnback_Tracker/Log.txt'
with open(fpath, 'a', encoding='utf-8') as f:
    f.writelines(more_lines)
    f.writelines('\n')

#close the opened file
f.close()