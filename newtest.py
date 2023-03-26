import cv2 as cv
import pandas as pd
from datetime import datetime
from datetime import date
import face_recognition
import os
import twilio
from twilio.rest import Client
from csv import DictWriter
from getpass import getpass
from PoseModule import PoseDetector
import config
# shit to add later on in the code
# add new user - get image, id and password
# change password/ forgot password

def phone():
    account_sid= 'AC1d0c90790dd60673881b16208378e817'
    auth_token = '90382e721131eb6b81ef53ec1be715c2'
    client = Client(account_sid,auth_token)
    call = client.calls.create(twiml='<Response><Say>crime alert   crime alert  crime alert</Say></Response>',
                            to='+917010961953',
                            from_='+14754052472')
    

entries=pd.DataFrame(columns=["ID","Time of Entry","Date","Entry by"])
n=0


# entries.to_csv('Entries.csv', index=False)
# function to entries dataframe - works

def worthyEntrance(ID#, choice
):
    # is_choice = ""
    # if choice == "1":
    #     is_choice = "face_ID"
    # else:
    #     is_choice = "password"
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    dict = {'ID': ID, 'Time of Entry': current_time, 'Date': today,
           
            }
    with open('Entries.csv', 'a') as f_object:
        dictwriter_object = DictWriter(f_object, fieldnames=entries,delimiter= "|")
        dictwriter_object.writerow(dict)
        f_object.close()

# Reading and training images
worthyNames = ["intruder"] # a list of names who can enter
worthyFaces = [] # a list of images who can enter
path = 'worthy'
worth = os.listdir(path)
for ppl in worth:
    temp = cv.imread(os.path.join(path,ppl))
    worthyFaces.append(temp)
    worthyNames.append(os.path.splitext(ppl)[0])
    

encodeList = []
for image in worthyFaces:
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    #faces = face_recognition.face_locations(image)
    encodes = face_recognition.face_encodings(image)[0]
    encodeList.append(encodes)


#read a csv file with user ID and passwords in choice 3 - works

def check(ID, password):
    id_pass = pd.read_csv('ID_PASS.csv')
    for ind in id_pass.index:
        if ID == id_pass['ID'][ind]:
            if password == id_pass['passwords'][ind]:
                return True
    return False

#checking the admin password - wobreakrks
def checkAdmin(password):
    with open('adPass.txt') as f:
        newline_breaks=""
        for line in f: 
            stripped_line = line.strip()
            newline_breaks += stripped_line
        f.close()
    if password == newline_breaks:
         return True
    return False

#show file

def showEntries():
    df = pd.read_csv('Entries.csv')
    print(df.to_string()) 


while True:
    #User choices
    # print("What is your choice? Select: \n"+"1. inititate program\n"+"2. Check all the entries\n"+"3. Enter with password\n"+"4. Quit\n")
    # choice = input()
    
    # if choice == "4":    
    #     break

    # elif choice == "3":
    #     for i in range(3,0,-1):
    #         print("Enter your name: ")
    #         ID = input()
    #         print("\nEnter you password: ")
    #         password = getpass()
    #         if check(ID, password):
    #             print("\nWelcome\n")
    #             #checktime()
    #             worthyEntrance(ID, choice)
    #             break
    #         else:
    #             print("You have ",i-1," tries left\n")
    #     #else:
    #      #   restrictAccess(ID)
                
#     elif choice == "2":
#         for i in range(3,0,-1):
#             print("Enter admin password: \n")
#             # passwordAdmin = ""
#             passwordAdmin = getpass()
#             if checkAdmin(passwordAdmin):
#                 showEntries()
#                 break
#             else:
#                 print("You have ",i-1," tries left")
#  #        else:
#  #             restrictAccess()

    # elif choice == "1":

        webcam = cv.VideoCapture(0)
        
        webcam.set(3, 640) #width
        webcam.set(4, 480) #length
        webcam.set(10, 100) #brightness
        detector = PoseDetector()
            
        tempcount=0
        frndcount = 0
        while True:
            success, img = webcam.read()
            cv.imshow("Webcam Input", img)

            img_2 =detector.findPose(img) 
            lmList,bbox = detector.findPosition(img_2)
            img = cv.resize(img, (0, 0), fx=0.25, fy=0.25)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            faceImg = face_recognition.face_locations(img)
            encodes = face_recognition.face_encodings(img, faceImg)
            img_2 =detector.findPose(img) 
            lmList,bbox = detector.findPosition(img_2 ,draw = False, bboxWithHands=False)
            
            
                
                
            img_3 = cv.resize(img_2,(600,500))
            cv.imshow("MyHumanRecogonizer",img_3)
            areyouworthy=[]
            for encode in encodes:
                areyouworthy = face_recognition.compare_faces(encodeList, encode)
            
            if True in areyouworthy:
                # worthyIndex = areyouworthy.index(True)
                # worthyEntrance(worthyNames[worthyIndex]#, choice
                #)

                frndcount = frndcount +1
                if frndcount == 2:    
                    print("friendly in sight.....not a trespasser.....")
                    frndcount =0
            else:
                if len(lmList)== 0:
                    var=0
                    var= var+1
                    if var == 6:
                        print("area clear ..... no activity in vision.....")
                else:
                    worthyIndex = 0
                # worthyEntrance(worthyNames[worthyIndex])
                    tempcount = tempcount+1
                    if tempcount == 15:
                        worthyEntrance(worthyNames[worthyIndex])
                        print("tresspassing detected....initating primary safety initatives........")
                        tempcount = 0
                        n=n+1
                        if n>10:
                            phone()

            if cv.waitKey(1) &0xFF == ord('q'):
                break
        if cv.waitKey(1) &0xFF == ord('d'):
            break
        webcam.release()
        cv.destroyAllWindows()
        
