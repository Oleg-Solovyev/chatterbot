# https://chatbotslife.com/how-to-create-an-intelligent-chatbot-in-python-c655eb39d6b1
# https://chatterbot.readthedocs.io/en/stable/logic/

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

my_bot = ChatBot('test16')
list_trainer = ListTrainer(my_bot)


import pymysql
import re
connection = pymysql.connect(host='localhost',
                             user='bot',
                             password='*******',
                             db='bot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


import time
start_time = time.time()
with connection.cursor() as cursor:
    for id in range(10000): # 50514
        sql = "select TOPIC_ID, SHORT_TEXT from v1_post where TOPIC_ID = " + str(id) + ";"
        cursor.execute(sql)
        rows = cursor.fetchall()
        small_talk = []
        for row in rows:
            if row['SHORT_TEXT'] != None :
                small_talk = small_talk + [re.sub('[^а-яА-Я,.!? ]', '', row['SHORT_TEXT'])]
        #print(small_talk)
        list_trainer.train(small_talk)
        print(str(id) + " " + str((time.time() - start_time)/60))


print(my_bot.get_response('привет'))
print(my_bot.get_response('программисты'))
print(my_bot.get_response('привет, программисты'))




                 
small_talk = ['hi there!',
              'hi!',
              'how do you do?',
              'how are you?',
              'i\'m cool.',
              'fine, you?',
              'always cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'glad to hear that.',
              'i feel awesome',
              'excellent, glad to hear that.',
              'not so good',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
              
small_talk1 = [u'да',
              u'нет']
              
small_talk = ['да',
              'нет']


list_trainer = ListTrainer(my_bot)
for item in (small_talk):
    list_trainer.train(item)


print(my_bot.get_response(u'да'))

   
math_talk_1 = ['pythagorean theorem',
               'a squared plus b squared equals c squared.']
               
math_talk_2 = ['law of cosines',
               'c**2 = a**2 + b**2 - 2 * a * b * cos(gamma)']
               
small_talk = ['привет',
              'салют',
              '']
              
small_talk = [       
'зачем ты блуждаешь так поздно в горах?',
'но кто же пойдёт для меня за водою',
'зачем ты ведёшь незнакомца впотьмах?',
'но это не есть ли кувшин за спиною',
'зачем ты всегда в поцелуйных следах?',
'но как же я пятна родимые смою',
'зачем ты с извечной тоскою в глазах?',
'но разве не ты их наполнил тоскою'
]

  
list_trainer = ListTrainer(my_bot)
for item in (small_talk):
    list_trainer.train(item)


print(my_bot.get_response('hi'))


import pymysql
connection = pymysql.connect(host='localhost',
                             user='bot',
                             password='test01Test!',
                             db='bot',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


small_talk = []
with connection.cursor() as cursor:
    sql = "select TOPIC_ID, SHORT_TEXT from v1_post where TOPIC_ID = 17;"
    cursor.execute(sql)
    #res = cursor.fetchone()
    #print(res)
    rows = cursor.fetchall()
    for row in rows:
        print(row['SHORT_TEXT'])
        small_talk = small_talk + [row['SHORT_TEXT']]
        list_trainer.train(item)
    
    
print(my_bot.get_response('нет'))



i = 0
f = open('/home/j/Downloads/forum_clean.sql')
for line in f:
  i = i + 1
  if i > 2500:
    print(line)
  if i > 2600:
    break

f.close()



sudo mysql -u root -p bot < forum_clean.sql

show tables;

select *
from v1_post
limit 1;


select TOPIC_ID, SHORT_TEXT from v1_post limit 10;
select TOPIC_ID, SHORT_TEXT from v1_post where TOPIC_ID = 1;



