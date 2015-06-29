__author__ = 'jinlong'
# -*- coding: utf-8 -*-
import unittest
import random
import json
import requests
import web
import datetime


db = web.database(host="192.168.1.15", port=3307, dbn='mysql', user='admin', pw='12345678', db='elf_test')


# symbol = raw_input("input symbol: ")
symbol = "600000"

sql0 = "select count(MARKETDATADATE) as count from marketdatasnapshot_day where symbol = '%s'" % symbol
res0 = list(db.query(sql0))
count = res0[0].count

if count >= 4:
    count = 4
    print u"计算天数是：",count
    sql = "select MARKETDATADATE from marketdatasnapshot_day where symbol = '%s' order by MARKETDATADATE desc limit %d" % (symbol,count)
    res = list(db.query(sql))
    start_time = res[0].MARKETDATADATE
    end_time = res[3].MARKETDATADATE
else:
    count = count
    print u"计算天数是：",count
    sql5 = "select MARKETDATADATE from marketdatasnapshot_day where symbol = '%s' order by MARKETDATADATE desc limit %d" % (symbol,count)
    res5 = list(db.query(sql5))
    start_time = res5[0].MARKETDATADATE
    end_time = res5[count-1].MARKETDATADATE
# start_time = res
print u'最后交易日的时间:',start_time
print u'倒数第4个交易日时间:',end_time
# start_time = datetime.datetime.strptime(start_time,"%Y-%m-%d")
# end_time = (start_time - datetime.timedelta(days=4)).strftime("%Y-%m-%d")
# print u"前4天的时间：",end_time
sql1 = "select sum(VOLUME) as volume from marketdatasnapshot_day where MARKETDATADATE between '%s' and '%s' and symbol = '%s'" % (end_time,start_time,symbol)
res1 = list(db.query(sql1))
sum_volume = res1[0].volume
print "过去'%s'天得总交易量'%s':" % (count,sum_volume)
# print "countcountcount:",count
volume_avg = sum_volume/count       #数据库计算的

# print res
class valume_api(unittest.TestCase):

    def setUp(self):
        self.url = "http://192.168.1.64:38086/marketdata/taskK?action=volumeData"

    def test_api(self):
        r = requests.get(self.url)
        text = r.text.encode('utf-8')
        text2 = json.loads(text[7:])
        print u"数据条数：",len(text2)
        len_data = len(text2)
        for i in range(0,len_data+1,1):
            if text2[i].get('symbol') == unicode(symbol):
                print u"标志位是：%s" % i
                break
            else:
                pass
        text3 = text2[i]
        volume_api =  text3['volume']       #接口返回的
        print type(text3),text3
        print "\n\n" + "[数据库计算的]过去'%s'天得平均交易量'%s':" % (count,volume_avg)
        print "接口返回的过去'%s'天得平均交易量'%s':" % (count,volume_api)
        self.assertEqual(volume_api,volume_avg)


    def tearDown(self):
        pass

if __name__=="__main__":
    unittest.main()