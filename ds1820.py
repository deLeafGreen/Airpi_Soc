#!/usr/bin/python
import csv
import datetime
from time import gmtime,strftime,sleep


def gettemp(id):
  try:
    mytemp = ''
    filename = 'w1_slave'
    f = open('/sys/bus/w1/devices/' + id + '/' + filename, 'r')
    line = f.readline() # read 1st line
    crc = line.rsplit(' ',1)
    crc = crc[1].replace('\n', '')
    if crc=='YES':
      line = f.readline() # read 2nd line
      mytemp = line.rsplit('t=',1)
    else:
      mytemp = 99999
    f.close()

    return int(mytemp[1])

  except:
    return 99999

if __name__ == '__main__':
  
  #counter daily hours
  counter = 0
  
  # Script has been called directly
  
  '''id_1 = '10-000802de6afd'
  id_2 = '10-000802de8b83'
  id_3 = '10-000802de3d35'
  id_4 = '10-000802de3a5f'''

  id_lang_5 = '28-0000066fe385'
  id_lang_4 = '28-000006706408'
  id_lang_3 = '28-0000067087c3'
  id_lang_2 = '28-0000066faf85'
  id_lang_1 = '28-0000066eb214'
  
def miss():  
    clock = strftime("%Y-%m_%d %H:%M:%S",gmtime())
    t1 = str(gettemp(id_lang_1)/float(1000))
    t2 = str(gettemp(id_lang_2)/float(1000))
    t3 = str(gettemp(id_lang_3)/float(1000)) 
    t4 = str(gettemp(id_lang_4)/float(1000))
    t5 = str(gettemp(id_lang_5)/float(1000))
  
    #new hour
    with open('/home/pi/csv/temp.csv','a') as csvfile:
        writer = csv.writer(csvfile,delimiter=',',quotechar = '|',quoting=csv.QUOTE_MINIMAL)
        writer.writerow([clock,t1,t2,t3,t4,t5])



while True:
    miss()
    sleep(5)
    

