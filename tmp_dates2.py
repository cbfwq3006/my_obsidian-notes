from datetime import datetime,timedelta
for n in [46266,46296,46327,46357,46722]: print(n,(datetime(1899,12,30)+timedelta(days=n)).date())
