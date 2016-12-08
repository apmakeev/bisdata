#!/usr/bin/env python

import os
import datetime
import zipfile

try:
    import zlib
    compression = zipfile.ZIP_DEFLATED
except:
    compression = zipfile.ZIP_STORED

modes = { zipfile.ZIP_DEFLATED: 'deflated',
          zipfile.ZIP_STORED:   'stored',
        }

date_list = list()

now_date = datetime.datetime.now()
time_delta = 2
str_date = now_date.strftime('%Y%m%d')
bisdata_dir = "/home/support/support/"
backup_dir = "/rt-mvno/bisdata/"


for file in os.listdir(bisdata_dir):
        if file.endswith(".txt"):
                date_file = file.split('_')
                if date_file not in date_list:
                        date_list.append(date_file[2])
date_list.sort()

for date in date_list:
        for file in os.listdir(bisdata_dir):
                if file.endswith(".txt"):
                        date_file = file.split('_')
                        if date == date_file[2]:
                                zip_file = backup_dir + 'bisdata_'+date+'.zip'
                                print 'Creating archive ' + zip_file
                                zf = zipfile.ZipFile(zip_file, mode='a')
                                try:
                                        print 'Adding ' + file +  'with compression mode', modes[compression]
                                        zf.write(file, compress_type=compression)
                                        os.remove(file)
                                finally:
                                        print 'Closing'
                                        zf.close()
