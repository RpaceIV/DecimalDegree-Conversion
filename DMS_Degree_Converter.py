import math

class DDegree_Converter:
    def __init__(self,int):    
        while True:
            #----|Display Menu Method|----#
            #def displayMenu():
            print('\n\nChoose a Search or Sort that you would like to preform? \n'
            +'======================================================= \n\n'
            + '               ' + '1 -- Convert DMS to Decimal Degrees. \n'
            + '               ' + '2 -- Convert Nautical Miles to Decimal Degrees. \n'
            + '               ' + '3 -- Exit \n'
            + '======================================================= \n\n')
            choice = input()
            if choice=='1':
                print('Enter the Degrees: ')
                decimal = float(input())
                print('Enter the Minutes: ')
                minutes = float(input())
                print('Enter the Seconds: ')
                seconds = float(input())
                convertNum = decimal + minutes/60.0 + seconds/3600.0 
                print('\n\n'+format(convertNum, '.16f'))
            elif choice=='2':
                print('Enter The amount of Nautical Miles')
                num = float(input())
                convertNum

            elif choice=='3':
                break
            else:
                print('Not an option')






    # def Dms_to_DD(self):
    #     decimal=0.0
    #     minutes=0.0
    #     seconds=0.0
    #     print('Enter the Degrees: ')
    #     input(decimal)
    #     print('Enter the Minutes: ')
    #     input(minutes)
    #     print('Enter the Seconds: ')
    #     input(seconds)
    #     convertNum= decimal + minutes/60 + seconds/3600
    #     return convertNum

    # def NM_to_DD(self):
    #     return "hi"

        # result = {1 : (Dms_to_DD),
        #           2 : (NM_to_DD),
        #           3 : "exit" }

        # data = result[choice]() 
        # print(data)
        
