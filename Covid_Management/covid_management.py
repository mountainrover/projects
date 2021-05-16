''' Program to Automate Covid treatment process '''
print("Program to Automate Covid treatment process")

print("Select the process : ")
print("1 : Symtopms check")
print("2 : RAT/RTPCR Result Upload")
print("3 : Blood test Result Upload")
print("4 : Blood re-test Result Upload")
print("5 : Chest X-Ray result upload")
menu = int(input("Enter your choice : "))



def positive():
  print("Kindly contact health department and quarantine for 4 days")
  print("Select the followings")
  print("1 : no symptoms/ mild symptoms")
  print("2 : High grade(>100F)/ High Fever")
  sym = int(input("Enter your choice : "))
  if(sym == 1):
   print('''Home isolation with (if ): 
   Paracetamol 650 mg(SOS/4 times max)
   Ivermectin 12 mg 1-0-0 x 3/5 days
   Zincovit 1-0-1 & Vitamin C 1-0-1
   Liquids 2.5-3 liters/day
   Fever Charting and w/f pulse O2
   Be vigilant for comorbid & aged patient
   No Oral steroids in early phase ''')
  elif(sym==2):
   print("Do Blood tests(CBC, CRP, D-Dimser, LDH) and upload the results")
  else:
   print("Invalid choice")
   positive()
'''-----------------------------------------------------------------------------'''  
def blood_test():
    print("Enter the test results for the following in numerical format")
    cbc = float(input("Enter the CBC results : "))
    crp = float(input("Enter the CRP results : "))
    dimer = float(input("Enter the D-Dimser results : "))
    ldh = float(input("Enter the ldh results : "))
    if((cbc>3.5 or crp> 5*0.08) and dimer>2*0.5 and ldh>2.34):
        print("Patient to be admitted in isolation ward")
    #elif(cbc<3.5 and crp< 5*0.08 and dimser<2*0.5 and ldh>2.34):
    else:
        print('''Patient to be closely observed:
              * Pulse oxygen (Spo2) to be monitored
              * Strict bed rest required
              * Kindly redo blood test after 48hrs and update results''')


def blood_retest():
    print("Enter the test results for the following in numerical format")
    cbc = float(input("Enter the CBC results : "))
    crp = float(input("Enter the CRP results : "))
    dimer = float(input("Enter the D-Dimser results : "))
    ldh = float(input("Enter the ldh results : "))
    if((cbc>3.5 or crp> 5*0.08) and dimer>2*0.5 and ldh>2.34):
        print("Chest X-Ray required")
    #elif(cbc<3.5 and crp< 5*0.08 and dimser<2*0.5 ):
    else:
        print('''Patient to be closely observed:
              * Pulse oxygen (Spo2) to be monitored
              * Strict bed rest required
              * Kindly redo blood test after 48hrs and update results''')
        spo2a = input("Enter SpO2 level (in %)")
        rra = input("Enter RR level")
        if(spo2a<94 and rr>24):
            print("If the person is having severe cough/Fever : Admit in Oxygen Bed")
        else:
            print("Kindly contact physician")


def chest_xray():
        print("Enter the test results for chest X-Ray HRCT in numerical format")
        hrct = float(input("Enter chest X-Ray HRCT level"))
        spo2b = float(input("Enter SpO2 level (in %)"))
        rrb = float(input("Enter rrb level (in %)"))

        if(hrct<8 and spo2b>94):
         print('''Patient to be closely observed:
              * Pulse oxygen (Spo2) to be monitored
              * Strict bed rest required
              * Be in touch with your physician''')
        elif((hrct>8 and hrct<=15) and spo2b>94):
         print("Based on physicians decision, Patient to be urgently admitted in HDU/ ICU")
        elif((hrct>8 and hrct<=15) and (spo2b<94 and rrb>24)):
         print("Patient to be urgently admitted in HDU/ ICU")
        elif(hrct>15 and spo2b<90):
         print("Patient to be urgently admitted in HDU/ ICU")
        else:
         print("Kindly contact physician")



def symptoms_check():
    print(" Kindly mark if you have any below symptoms in y/n:")
    throat = input("Throat Pain : ")
    fever = input("Fever/Headache/Body Ache : ")
    smell = input("Loss of smell/ Taste : ")
    diarrhea = input("Diarrhea : ")
    print("------------------------------------------------------")
    yes_list = ['y', 'Y', 'Yes', 'YES']
    no_list = ['n', 'N', 'No', 'NO']
    rat = [throat,fever,smell]
    rtpcr = [throat,fever,smell,diarrhea]
    
    x= False
    y=False
    if(fever in yes_list):
     for ele in rat:
      if(ele in no_list):
       x=True
    if(x == True):
     print("Kindly go for Rapid Antigen Test and update the result afterwards")
     print("Thankyou and isolate yourself")
    
    else:
        for ele in rtpcr:
          if(ele in yes_list):
              y==True

    if(y==True):
     print("Kindly go for RTPCR Test and update the result afterwards")
     print("Thankyou and isolate yourself")


def result_upload():
    print("Select the test that you have done (1 / 2): ")
    print("1 : Rapid Antigen Test")
    print("2 : RTPCR Test")
    test = int(input("Enter your choice : "))

    print("Select the test result (1 / 2 /3): ")
    print("1 : Negative")
    print("2 : Positive")
    print("3 : Was negative earler and retested now negative again")
    result = int(input("Enter your choice : "))

    if(result == 1):
        print("Please stay in isolation for Three days and retest RTPCR for confirmation")
    elif(result == 3):
        print("Select the test result (1 / 2): ")
        print("1 : Negative")
        print("2 : Positive")
        retestResult = int(input("Enter your choice : "))
        if(retestResult):
            print("You are safe but please continue self isolation and take rest")
            print("Kindly contact the below number for ant further details")
            print("Health Dept. Phone Number : ")
    elif(result == 2):
         positive()
    else:     
         print("Invalid choice")
         result_upload()


if(menu ==1):
    symptoms_check()
elif(menu == 2):
    result_upload()
elif(menu == 3):
    blood_test()
elif(menu == 4):
    blood_retest()
elif(menu == 5):
    chest_xray()
else:
    print("Invalid choice")






