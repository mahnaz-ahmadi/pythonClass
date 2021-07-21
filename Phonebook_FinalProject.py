class Contact:

    def __init__(self):
        self.list = []
        self.names =[]
        self.numbers =[]

    #------------------------- PhoneBook ---------------------------#
    def phonebook(self):
        print('\nTotal Contacts found:',len(self.list))
        for contact in self.list:
            print('\nNAME:',contact[0])
            print('Phone Number:',contact[1])
            print('Email:',contact[2])

    #-------------------------------------- Search Contact -----------------------------#
    def search(self,number=False,name=False):

        if name:
            if name in self.names:
                name_indexes = []
                for i, x in enumerate(self.names):
                    if x == name:
                        name_indexes.append(i)
                pointer = 1
                for iname in name_indexes:
                    print(pointer,'name:',self.names[iname],'details:',self.list[iname],'\n')
                    pointer+=1
            else:
                print('No contact found!')

        elif number:
            if number in self.numbers:
                number_indexes = []
                for i, x in enumerate(self.numbers):
                    if x == number:
                        number_indexes.append(i)
                pointer = 1
                for inumber in number_indexes:
                    print(pointer,'number:',self.numbers[inumber],'details:',self.list[inumber],'\n')
                    pointer+=1

            else:
                print('No contact found!')
        else:
                print('No contact found!')


    def create(self,name,number,email):

        self.list.append([name,number,email])
        self.names.append(name)
        self.numbers.append(number)
        print(name,'Contact created successfully')

    def update(self, name=False,number=False):

        # -------------------------------- Update Using Names ----------------------#
        if name:
            if name in self.names:

                name_indexes = []
                for i, x in enumerate(self.names):
                    if x == name:
                        name_indexes.append(i)

                print('No.of contacts found:',len(name_indexes),name_indexes)
                pointer = 1
                for iname in name_indexes:
                    print(pointer,'name:',self.names[iname],'details:',self.list[iname],'\n')
                    pointer+=1
                d = 'y'
                while d:
                    inp = input("Press 'y' to continue or exit to 'n':")
                    if inp =='y':
                        nm_i = int(input('Enter index of listed contact above:'))

                        try:
                            data = name_indexes[nm_i-1]
                            print('\nDetails:',self.list[data])
                            print(1,'- Name: ',self.list[data][0])
                            print(2,'- Number: ',self.list[data][1])
                            print(3,'- Email: ',self.list[data][2])
                            print(0,'- Exit')

                            v = 'y'
                            while v:
                                ch = int(input('Enter index of listed contact above:'))
                                if ch == 1:
                                    ch_name = input('Enter name to update:')
                                    self.list[data][0] = ch_name
                                    self.names[data] = ch_name

                                elif ch == 2:
                                    ch_number = input('Enter Number to update:')
                                    self.list[data][1] = ch_number
                                    self.numbers[data] = ch_number
                                elif ch == 3:
                                    ch_email = input('Enter Email to update:')
                                    self.list[data][2] = ch_email
                                elif ch==0:
                                    v = False
                                else:
                                    v= False

                            print('#---------------- Updated contact -------------#')
                            print(self.list[data])
                            print(self.names[data])
                            print(self.numbers[data])

                        except:
                            print('index not found!')

                    else:
                        break
            else:
                print('No contact Found!')

    # -------------------------------- Update Using Numbers ----------------------#
        elif number:
            if number in self.numbers:

                number_indexes = []
                for i, x in enumerate(self.numbers):
                    if x == number:
                        number_indexes.append(i)

                print('No.of contacts found:',len(number_indexes))
                pointer = 1
                for inumber in number_indexes:
                    print(pointer,'Number:',self.numbers[inumber],'details:',self.list[inumber],'\n')
                    pointer+=1


                d = 'y'
                while d:
                    inp = input("Press 'y' to continue or exit to 'n':")
                    if inp =='y':
                        nm_i = int(input('Enter index of listed contact above:'))

                        try:
                            data = number_indexes[nm_i-1]
                            print('\nDetails:',self.list[data])
                            print(1,'- Name: ',self.list[data][0])
                            print(2,'- Number: ',self.list[data][1])
                            print(3,'- Email: ',self.list[data][2])
                            print(0,'- Exit')

                            v = 'y'
                            while v:
                                ch = int(input('Enter index of listed contact above:'))
                                if ch == 1:
                                    ch_name = input('Enter name to update:')
                                    self.list[data][0] = ch_name
                                    self.names[data] = ch_name

                                elif ch == 2:
                                    ch_number = input('Enter Number to update:')
                                    self.list[data][1] = ch_number
                                    self.numbers[data] = ch_number
                                elif ch == 3:
                                    ch_email = input('Enter Email to update:')
                                    self.list[data][2] = ch_email
                                elif ch==0:
                                    v = False
                                else:
                                    v= False

                            print('#---------------- Updated contact -------------#')
                            print(self.list[data])
                            print(self.names[data])
                            print(self.numbers[data])

                        except:
                            print('index not found!')

                    else:
                        break
            else:
                print('No contact Found!')
        else:
            print('No conatact Found..!')


    #------------------------------ DELETE Contacts --------------------------#
    def delete(self,name=False,number=False):

        if name:
            if name in self.names:
                d = 'y'
                while d:
                    name_indexes = []
                    for i, x in enumerate(self.names):
                        if x == name:
                           name_indexes.append(i)
                    if len(name_indexes) >0:
                        print('No.of contacts found:',len(name_indexes),name_indexes)
                        c = 1
                        for iname in name_indexes:
                            print(c,'name:',self.names[iname],'details:',self.list[iname],'\n')
                            c+=1

                        inp = input("Press 'y' to continue or exit to 'n':")

                        if inp =='y':
                            nm_i = int(input('Enter index of listed CONTACT above:'))

                            try:
                                data = name_indexes[nm_i-1]
                                print('\nDetails:',self.list[data])

                                f = input('Are you sure want to DELETE..? (y/n):')
                                if f =='y':
                                    del self.list[data]
                                    del self.numbers[data]
                                    del self.names[data]

                                print('#---------------- Updated contact Book -------------#')
                                print('\nDetails:',self.list)
                                print('\nName Entries:',self.names)
                                print('\nNumber Entries:',self.numbers)
                            except:
                                print('\nindex not found!')
                        else:
                            break
                    else:
                        print('0 contacts found..!')
                        break
            else:
                print('Contact not found..!')


        elif number:
            if number in self.numbers:

                d = 'y'
                while d:

                    number_indexes = []
                    for i, x in enumerate(self.numbers):
                        if x == number:
                           number_indexes.append(i)
                    if len(number_indexes) >0:
                        c = 1
                        for inumber in number_indexes:
                            print(c,'number:',self.numbers[inumber],'details:',self.list[inumber],'\n')
                            c+=1

                        inp = input("Press 'y' to continue or exit to 'n':")
                        if inp =='y':
                            nm_i = int(input('Enter index of listed CONTACT above:'))

                            try:
                                data = number_indexes[nm_i-1]
                                print('\nDetails:',self.list[data])

                                f = input('Are you sure want to DELETE..? (y/n):')
                                if f =='y':
                                    del self.list[data]
                                    del self.numbers[data]
                                    del self.names[data]

                                print('#---------------- Updated contact Book -------------#')
                                print('\nDetails:',self.list)
                                print('\nName Entries:',self.names)
                                print('\nNumber Entries:',self.numbers)
                            except:
                                print('\nindex not found!')
                        else:
                            break
                    else:
                        print('0 contacts found..!')
                        break

            else:
                print('No contact Found!')


        else:
            print('No conatact Found..!')




menu ='''
          1.Create
          2.Update
          3.ListContacts
          4.Search
          5.Delete
          6.Exit
'''

if __name__ == "__main__":

    c = Contact()

    a = True
    while a:
        print('\n',menu,'\n')
        choice = int(input('\nEnter your Choice:'))
        if choice ==1:
            name = input('Enter Name:')
            phone = input('Enter phone number:')
            email = input('Enter your email:')
            c.create(name,phone,email)
        elif choice == 2:
            k =True
            while k:
                print(
                    '''
                    1. Update through name
                    2. Update through number
                    3. Exit
                    '''
                )
                inp = 0
                try:
                    inp = int(input('Enter input:'))
                except Exception as e:
                    continue

                if inp ==1:
                    name = input('Enter name:')
                    c.update(name=name)
                elif inp ==2:
                    number = input('Enter Number:')
                    c.update(number=number)
                else:
                    k = False
        elif choice == 3:
            c.phonebook()

        elif choice == 4:
            k =True
            while k:
                print(
                    '''
                    1. Search through name
                    2. Search through number
                    3. Exit
                    '''
                )
                inp = 0
                try:
                    inp = int(input('Enter input:'))
                except Exception as e:
                    continue

                if inp ==1:
                    name = input('Enter name:')
                    c.search(name=name)
                elif inp ==2:
                    number = input('Enter Number:')
                    c.search(number=number)
                else:
                    k = False

        elif choice == 5:
            k =True
            while k:
                print(
                    '''
                    1. Delete through name
                    2. Delete through number
                    3. Exit
                    '''
                )
                inp = 0
                try:
                    inp = int(input('Enter input:'))
                except Exception as e:
                    continue

                if inp ==1:
                    name = input('Enter name:')
                    c.delete(name=name)
                elif inp ==2:
                    number = input('Enter Number:')
                    c.delete(number=number)
                else:
                    k = False
        elif choice == 6:
            a = False
        else:
            break
