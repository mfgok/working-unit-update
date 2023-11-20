import requests
import time
from datetime import datetime
import WorkingUnit




workingUnitList = []
workingUnitList = WorkingUnit.WorkingUnit.getWorkingUnitList()

def getTime():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time

for x in workingUnitList:
  print(f"{x.name} Güncelleme Başladı {getTime()}")
  guncellemeStart =  time.time()
  BASE_URL = 'https://127.0.0.1:7227/api/points/updatearticlepointsforworkingunit?workingUnitId='
  response = requests.get(f"{BASE_URL}{x.id}",verify=False)
  guncellemeEnd = time.time()
  gecenSure = guncellemeEnd - guncellemeStart
  print(response.json())
  print(f"{x.name} Güncelleme Bitti {getTime()} - Geçen Süre : {round(gecenSure,2)} saniye")
  time.sleep(1)






