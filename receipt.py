'''
commission receipt generator
'''

#import(s)
import random

i = 1
serv = 0
diff = 0
tax = 0.3
final = {

     }

#FUNCTIONS----------
def intstuct():
     print('''
     Make sure to type the full words out as shown in the options.
     ALSO NOTE: MAKE SURE TO SKIP PAST THE FIRST PROMPT; FOR SOME REASON IT DOES NOT ADD TO DICT.
     ''')

def receipt():

     #CAM----------
     if work == cam and difficulty == easy:
          serv = 2
          diff = 200

     if work == cam and difficulty == med:
          serv = 2
          diff = 400

     if work == cam and difficulty == hard:
          serv = 2
          diff = 800

     if work == cam and difficulty == exp:
          serv = 2
          diff = 1200
     #/CAM----------

     #LIGHTING-----------
     if work == light and difficulty == easy:
          serv = 1.4
          diff = 200
     
     if work == light and difficulty == med:
          serv = 1.4
          diff = 400

     if work == light and difficulty == hard:
          serv = 1.4
          diff = 800

     if work == light and difficulty == exp:
          serv = 1.4
          diff = 1400
     #/LIGHTING----------

     #MAP BUILDING----------
     if work == build and difficulty == easy:
          serv = 1.5
          diff = 200

     if work == build and difficulty == med:
          serv = 1.5
          diff = 400

     if work == build and difficulty == hard:
          serv = 1.5
          diff = 800

     if work == build and difficulty == exp:
          serv = 1.5
          diff = 1400
     #/MAP BUILDING----------

     #UI----------
     if work == ui and difficulty == easy:
          serv = 2.1
          diff = 200
     
     if work == ui and difficulty == med:
          serv = 2.1
          diff = 400

     if work == ui and difficulty == hard:
          serv = 2.1
          diff = 800

     if work == ui and difficulty == exp:
          serv = 2.1
          diff = 1400
     #/UI----------

     #MODELING----------
     if work == model and difficulty == easy:
          serv = 3
          diff = 200

     if work == model and difficulty == med:
          serv = 3
          diff = 400

     if work == model and difficulty == hard:
          serv = 3
          diff = 800

     if work == model and difficulty == exp:
          serv = 3
          diff = 1400
     #/MODELING----------

     #LOGIC----------
     if work == log and difficulty == easy:
          serv = 2.2
          diff = 200

     if work == log and difficulty == med:
          serv = 2.2
          diff = 400

     if work == log and difficulty == hard:
          serv = 2.2
          diff = 800

     if work == log and difficulty == exp:
          serv = 2.2
          diff = 1400
     #/LOGIC----------

     #DATA----------
     if work == data and difficulty == easy:
          serv = 2.3
          diff = 200

     if work == data and difficulty == med:
          serv = 2.3
          diff = 400

     if work == data and difficulty == hard:
          serv = 2.3
          diff = 800

     if work == data and difficulty == exp:
          serv = 2.3
          diff = 1400
     
     print('Price: ', (diff * serv))
     print('Tax: ', (diff * serv) * tax)
     print('Total: ', (diff * serv) + ((diff * serv) * tax))
     final[i] = (diff * serv) + ((diff * serv) * 0.3)

#/FUNCTIONS----------

#OPTIONS----------

     #services
cam = 'Camera' #done
light = 'Lighting' #done
build = 'Map Building' #done
ui = 'UI' #done
model = 'Modeling' #done
log = 'Logic System' #done
data = 'Data Store'
     #difficulties
easy = 'Easy'
med = 'Medium'
hard = 'Hard'
exp = 'Expert'

#/OPTIONS----------

intstuct()
while True:
#INPUTS----------

     work = input('''
Your options for services: 
Camera
Lighting
Map Building
UI
Modeling
Logic System
Data Store
--------------------
What is the service?: ''')

     print('--------------------')

     difficulty = input('''
Your options for difficulties: 
Easy
Medium
Hard
Expert
--------------------
What is the difficulty?: ''')

#/INPUTS----------

#complete
     print(final)
     receipt()
     i = i + 1

#ask again
     print('Your total is:', sum(final.values()))
     ask = input('Submit another request?: ')
     if ask == 'n' or ask == 'no':
          break
