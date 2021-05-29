print('\t\t\tContact Tracing Program\n')

temp = 0.0
personalInformation = ['name','contact','address']
possibleCarrier = ['name','contact','address']

def showCases(location):
    if location == 1:
        print("There are  people from CALABARZON who are potentially carriers.")
    if location == 2:
        print("There are  people from CENTRAL LUZON who are potentially carriers.")
    if location == 3:
        print("There are  people from MANILA who are potentially carriers")

def calculateSafeDay(num1):
    safe_day = 14 - num1
    print(safe_day, 'day/s until you are safe to enter.\n')

def symptomsChecker():
    symptomatic = input('Are you experiencing any symptoms? (True or False):')
    if (symptomatic == 'True') or (symptomatic == 'true') or (symptomatic == 'T') or (symptomatic == 't'):
        print('what are your symptoms? (choose from these symtpoms shown) \n')
        showSymptoms()
    elif (symptomatic == 'False') or (symptomatic == 'false') or (symptomatic == 'F') or (symptomatic == 'f'):
        print('You may enter')
    showCases(personalInformation[2])

def showSymptoms():
        symptomsList = ['A', 'B', 'C', 'D', 'E', 'F']
        print(symptomsList[0], " FEVER - If the temperature of the interviewee is greater than 37.5 C, the person has fever and it might show as headaches and muscle soreness.")
        print(symptomsList[1], " DRY COUGH - Is a cough without phlegm in the throat. It might lead to sore throat and Tonsillitis.")
        print(symptomsList[2], " COLDS - Has two indicators which is coughing and running nose.")
        print(symptomsList[3], " LOSS OF TASTE - A sudden phenomena when a person can't taste anything.")
        print(symptomsList[4], " LOSS OF SMELL - A sudden phenomena when a person can't smell anything.")
        print(symptomsList[5], " DIFFICULTY BREATHING - Is an uncomfortable condition that makes it difficult to breath")

        print("\nPlease input your symptom/s")
        while True:
            symptom = input('Input the letter of your symptom/s: ')
            if symptom.isdigit():
                print("Error please try again")
            elif symptom.islower():
                print("Error please make sure your answer is in upper case")
            elif symptom == "A" or symptom == "B" or symptom == "C" or symptom == "AB" or symptom == "CB" or symptom == "AC" or symptom == "ABC":
                print("\nRest, take medications, and stay hydrated.\n")
                break
            elif symptom == "D" or symptom == "E" or symptom == "F" or symptom == "DE" or symptom == "EF" or symptom == "DF" or symptom == "DEF":
                print("Consult your doctor.")
                break
            else:
                break

        while True:
                check1 = input('Are there any other symptoms?(True or False): ')
                if check1 == 'True' or check1 == 'true' or check1 == 't' or check1 == 'T':
                    symptom1 = input('\nA. FEVER\n B. DRY COUGH\n C. COLDS\n D. LOSS OF TASTE\n E. LOSS OF SMELL\n F. DIFFICULTY BREATHING\n')
                    if symptom1.isdigit():
                        print("Error please try again")
                    elif symptom1.islower():
                        print("Error please make sure your answer is in upper case")
                    elif symptom1 == "A" or symptom1 == "B" or symptom1 == "C" or symptom1 == "AB" or symptom1 == "CB" or symptom1 == "AC" or symptom1 == "ABC":
                        print("\nRest, take medications, and stay hydrated")
                        print('You may not Enter')
                        return
                    elif symptom1 == "D" or symptom1 == "E" or symptom1 == "F" or symptom1 == "DE" or symptom1 == "EF" or symptom1 == "DF" or symptom1 == "DEF":
                        print("Please consult your doctor for more details.\n")
                        print('You may not Enter')
                        return
        else:
            return



while True:
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    if password =='a' and username =='a':
        print('\n\t\t\tYou may use the program\n')
    while True:
        repeat = input('Do you want to use the program?(True or False): ')
        if repeat == 'True' or repeat == 'true' or repeat == 't' or repeat == 'T':
            while True:
                    personalInformation[0] = input('Enter name (Last Name, First Name): ')
                    personalInformation[1] = input('Enter contact number in the format of (+63) XXXXXXXXXX: (+63) ')
                    personalInformation[2] = int(input('Please enter your location: \n1. CALABARZON\n 2. CENTRAL LUZON\n 3. METRO MANILA\n'))
                    if  personalInformation[0].isdigit():
                        print('Wrong input/s on personal information. Try again! \n')
                    elif not personalInformation[1].isdigit():
                        print('Wrong input/s on personal information. Try again! \n')
                    else:
                        print('\n\t\t\t',personalInformation[0])
                        print('\t\t\t',personalInformation[1])
                        print('\t\t\t',personalInformation[2])
                        break

            temp = float(input('\nEnter your temperature: '))
            if (temp >=36.5) and (temp <=37.5):
                print('Temperature is normal. The user has no fever \n')
            elif (temp <36.4) and (temp <=37.5):
                print('error temperature')
            elif (temp >37.5):
                print('The interviewee has fever! Input fever as one of the symptoms \n')

            exposureInput = input('Have you been exposed to someone with COVID-19? (True or False): ')
        
            if (exposureInput == 'True') or (exposureInput == 'true') or (exposureInput == 'T') or (exposureInput == 't'):
                exposure_days = int(input('In the past how many days?\n'))
                if (exposure_days <= 14):
                    print('\nThe number of days is alarming\n')
                    calculateSafeDay(exposure_days)
                    while True:
                                possibleCarrier[0] = input('Enter name (Last Name, First Name): ')
                                possibleCarrier[1] = input('Enter contact number in the format of (+63) XXXXXXXXXX: (+63) ')
                                possibleCarrier[2] = input('Enter address (City, Province): ')
                                if  possibleCarrier[0].isdigit():
                                    print('Wrong input/s on possible carrier information. Try again! \n')
                                elif not possibleCarrier[1].isdigit():
                                    print('Wrong input/s on possible carrier information. Try again! \n')
                                elif possibleCarrier[2].isdigit():
                                    print('Wrong input/s on possible carrier information. Try again! \n')
                                else:
                                    print(possibleCarrier[0])
                                    print(possibleCarrier[1])
                                    print(possibleCarrier[2])
                                    symptomsChecker()
                                    break
                elif (exposure_days > 14):
                    print('The number of days is safe')
                    symptomsChecker()
                    break
            elif (exposureInput == 'False') or (exposureInput == 'false') or (exposureInput == 'F') or (exposureInput == 'f'):
                symptomsChecker()
            else:
                print('Error input try again')
        else:
            print('Goodbye Have a good day!')
            break
    else:
        print('Incorrect username and password. Try again!')   
