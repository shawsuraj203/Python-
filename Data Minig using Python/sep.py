import re
import codecs
from positive import positive_words
from negative import negative_words
emotional_words = positive_words + negative_words
fx = open("petrol.txt", 'r');
fy = open("sep1.txt",'w');
for line in fx:
    line = re.sub(r'[ , ( )]','\n',line);
    fy.write(line);
fx.close();
fy.close();
fx = codecs.open("diesel.txt", encoding="utf-8")
#fx = open("diesel.txt", 'r');
fy = open("sep2.txt",'w');
for line in fx:
    line = re.sub(r'[ , ( )]','\n',line);
    fy.write(line);
fx.close();
fy.close();
fv = codecs.open("diesel.txt", encoding="utf-8")
fw = open("sep4.txt",'w');
count=0;
val = ""
for line in fv:
    val += fv.read()
print(val)
user_words = val.split(' ')
print(user_words)
for word in user_words:   #iterate through each word in the list user_words
    if word in emotional_words:   #check if word is also present in emotional_words
        fw.write(word + '\r\n')   #write word in the file
        print (word)
fv.close();
fw.close();
fv = open("petrol.txt", 'r');
fw = open("sep3.txt",'w');
count=0;
val = ""
for line in fv:
    val += fv.read()
print(val)
user_words = val.split(' ')
print(user_words)
for word in user_words:   #iterate through each word in the list user_words
    if word in emotional_words:   #check if word is also present in emotional_words
        fw.write(word + '\r\n')   #write word in the file
        print (word)
fv.close();
fw.close();

