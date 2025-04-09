## FAQ

1、报错 “超出时间限制”，打印时间，定位哪行代码导致的。
```
import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
```