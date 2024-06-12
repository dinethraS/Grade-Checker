#Author - Dinethra(20221135/19541189)

#Part 4

#Only integer check
def int_check(message):
    while True:
        try:
            val=int(input(message))
        except ValueError:
            print('Integer Required\n')
        else:
            return val

#ID checking
def id_check(message='\nPlease enter your student ID: '):
    while True:
        stuid=input(message)
        if len(stuid)!=8 or stuid[0]!='w':
            print('Invaid ID.')
            continue
        else:
            return stuid

#Integer and range checking
def valid_check(message):
    while True:
        try:
            credit=int(input(message))
        except ValueError:
            print('Integer Required')
        else:
            if credit%20==0 and credit<=120:
                return credit
            else:
                print('Out of range')
    
#Dictionary access
def dic_access(dictionary):
    for key, value in dictionary.items():
        print(key,':',value, end=' ')
    

def main():
    x='y'
    pro_count=0
    tra_count=0
    ret_count=0
    ex_count=0
    dic={}

    while x == 'y':
        ID=id_check()
        while True:
            passes=valid_check('Please enter your credits at pass: ')
            defer=valid_check('Please enter your credits at defer: ')
            fail=valid_check('Please enter your credits at fail: ')
                    
            if (passes+defer+fail)!= 120:
                print('Total incorrect')
                continue

            else:

                if passes == 120:
                    name = 'Progress'
                    pro_count+=1
                elif passes >= 100 and (defer+fail) <= 20:
                    name = 'Progress(module trailer)'
                    tra_count+=1
                elif passes >= 0 and (defer+fail) <= 120 and not(fail>=80):
                    name = 'Module retriever'
                    ret_count+=1
                elif fail >= 80:
                    name = 'Exclude'
                    ex_count+=1
                print(name)

                #dictionary stage 1
                tempList = [name,passes,defer,fail]
                temp_dict_val=(str(tempList[0])+' - '+str(tempList[1])+' , '+str(tempList[2])+' , '+str(tempList[3]))
                dic[ID]=temp_dict_val
                break

        while True:
            print('\nWould you like to enter another set of data?')
            x = input("Enter 'y' to continue or 'q' to end and view: ")
            x = x.lower()
            if x!='y' and x!='q':
                continue
            else:
                break
            
    #dictonary funtion
    dic_access(dic)      
    



#Main program

while True:
    opt=int_check('If student press 1. \nIf staff member press 2: ')
    if opt==2:
        main()
        break
    elif opt==1:#Student version
        passes=valid_check('\nPlease enter your credits at pass: ')
        defer=valid_check('Please enter your credits at defer: ')
        fail=valid_check('Please enter your credits at fail: ')
                
        if (passes+defer+fail)!= 120:
            print('Total incorrect')

        else:

            if passes == 120:
                name = 'Progress'
            elif passes >= 100 and (defer+fail) <= 20:
                name = 'Progress(module trailer)'
            elif passes >= 0 and (defer+fail) <= 120 and not(fail>=80):
                name = 'Module retriever'
            elif fail >= 80:
                name = 'Exclude'
            print(name)
            break

    else:
        print('Selected option is not valid.\n')
        continue

