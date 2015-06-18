# -*- coding: utf-8 -*-
__author__ = 'jinlong'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

# mysql -uadmin -p12345678 -P3307 -h192.168.1.15
# command = "mysql -uadmin -h192.168.1.15 -P%s -pgdq_webdb_test"

# command = "cd /Users/jinlong/Downloads/icaopan_web/src/main/webapp && find . -type d -name '.svn'|xargs rm -rf && jar -cvf GDQ.war *"
command1 = "cd C:\Users\user\.jenkins\workspace\icaopan_web\src\main\webapp &&" \
           " jar -cvf GDQ_test.war * && " \
           "copy GDQ_test.war D:\\GDQ\\apache-tomcat-7.0.40\\webapps"
os.system(command1)
print command1 + "\n"




