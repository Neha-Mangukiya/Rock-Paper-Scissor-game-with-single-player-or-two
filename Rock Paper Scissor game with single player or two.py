#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

while True:
    print('Rules ::: Rock vs paper-> paper wins \n\t Rock vs scissor-> Rock wins \n\t paper vs scissor-> scissor wins')
    print('1. One player \n 2. Two player')
    print('Enter the choice : \n 1. Rock \n 2. Paper \n 3.Scissor')
    
    choice_player = int(input('Enter the player choice ::'))
    
    if choice_player == 1:
        choice = int(input("Enter the choice (user) :"))
    
        while choice>3 or choice<1:
            print('Please enter valid input\n')
    
        if choice == 1:
            ch_name = 'Rock'
        elif choice == 2:
            ch_name = 'Paper'
        else:
            ch_name = 'Scissor'
            
        print('User choice is :' + ch_name)
    
        print('Now computer turn ==>')
    
        comp_ch = random.randint(1,3)
    
        while comp_ch == ch_name:
            comp_ch = random.randint(1,3)
        
        if comp_ch == 1:
            comp_name = 'Rock'
        elif comp_ch == 2:
            comp_name = 'Paper'
        else:
            comp_name = 'Scissor'
    
        print('Computer choice is :' + comp_name)
    
        if (choice == 1 and comp_ch == 2) or (choice == 2 and comp_ch == 2):
            print('Paper win \n')
            result = 'Paper'
        elif (choice == 1 and comp_ch == 3) or (choice == 3 and comp_ch == 1):
            print('Rock win \n')
            result = 'Rock'
        else:
            print('Scissor win \n ')
            result = 'Scissor'
        
        if result == ch_name:
            print('----User win----\n')
        else:
            print('----Computer win----\n')
        
        print('Do you want to play again Y/N')
        ans = input()
    
        if ans == 'N' or ans == 'n':
            break
        
    elif choice_player == 2:
        choice_user_1 = int(input("Enter the choice (user-1) :"))
    
        while choice_user_1>3 or choice_user_1<1:
            choice_user_1 = int(input("enter valid input: "))    
        if choice_user_1 == 1:
            ch_name_1 = 'Rock'
        elif choice_user_1 == 2:
            ch_name_1 = 'Paper'
        else:
            ch_name_1 = 'Scissor'
        
        print('User-1 choice is :' + ch_name_1)
    
        choice_user_2 = int(input("\n Enter the choice (user-2) :"))
    
        while choice_user_2>3 or choice_user_2<1:
            choice_user_2 = int(input("enter valid input: "))
    
        if choice_user_2 == 1:
            ch_name_2 = 'Rock'
        elif choice_user_2 == 2:
            ch_name_2 = 'Paper'
        else:
            ch_name_2 = 'Scissor'
        
        print('User-2 choice is :' + ch_name_2)
    
        if (choice_user_1 == 1 and choice_user_2 == 2) or (choice_user_1 == 2 and choice_user_2 == 1):
            print('\nPaper win \n')
            result = 'Paper'
        elif (choice_user_1 == 1 and choice_user_2 == 3) or (choice_user_1 == 3 and choice_user_2 == 1):
            print('Rock win \n')
            result = 'Rock'
        else:
            print('Scissor win \n ')
            result = 'Scissor'
        
        if result == ch_name_1:
            print('----User-1 win----\n')
        else:
            print('----User-2 win----\n')
        
        print('Do you want to play again Y/N')
        ans = input()
    
        if ans == 'N' or ans == 'n':
            break


# In[ ]:




