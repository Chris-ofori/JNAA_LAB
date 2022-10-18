#!/usr/bin/env python
# coding: utf-8

# DAY 1

# # COMMENTS AND HEADINGS
# VFBGDBNB THNFHG

# In[3]:


print('Daniel')


# In[4]:


print('Daniel')


# In[5]:


print ('rice')


# In[9]:


# hfjkfj


# In[7]:


'''print daniel'''


# In[ ]:


hdjfis


# # DATA TYPES

# In[12]:


10


# In[13]:


type(10)


# In[14]:


type(15.72)


# In[16]:


type('rain')


# In[18]:


type([12,34,56])


# In[21]:


type([2,3,5])


# In[22]:


type[2,3,4,5,6]


# In[24]:


type({3,4,6,9})


# In[25]:


type((3,7,8,0))


# # Variable Assignment

# In[31]:


s=6


# In[32]:


d=5


# In[34]:


zz= d+s


# In[35]:


zz


# In[37]:


g=7


# In[38]:


r=9898


# In[39]:


bk=r-g


# In[40]:


bk


# In[41]:


w=70


# In[42]:


v=30


# In[45]:


m=(w/v)*100


# In[46]:


m


# In[47]:


l=(v*w)+(v/w)


# In[48]:


l


# In[49]:


"g"


# In[55]:


a=5
b=10


# In[57]:


c=a+b


# In[52]:


c


# In[59]:


a=6
b=13

c=b+a


# In[60]:


c


# # Print 

# In[62]:


print (c)


# In[65]:


print('my name is chris\nMet student')


# In[69]:


print('question 1 is A\nquestion 2 is D\nquestion 3 is E')


# In[70]:


print('')


# In[71]:


print('my name is Chris\nI stay at Bomso')


# In[72]:


print('my name is Berthold\nI stay at Lagos Town')


# In[74]:


print(a+b*zz/a)


# In[77]:


course='METEOROLOGY AND CLIMATE SCIENCE'


# In[78]:


len(course)


# In[79]:


course[0]


# In[88]:


# indexing even


# In[80]:


course[0:2]


# In[81]:


course[0:3]


# In[87]:


# indexing odd


# In[82]:


course[::2]


# In[86]:


course[4::2]


# # concatenation

# In[89]:


# Joining words, letters,numbers together


# In[93]:


a='Meteorology '
b='and '
c='Climate '
d='Science'


# In[94]:


print(a+b+c+d)


# In[96]:


print(a,b,c,d)


# In[100]:


print('Vote Rhoda 2023\n'*20)


# In[102]:


print('vote for RHODA 2023\n'*10)


# # formatting strings

# In[103]:


a='FELLOW GHANAIANS, THE DOLLAR IS 12 CEDIS' 


# In[112]:


b=a.lower()


# In[114]:


b


# In[115]:


c=b.upper()


# In[116]:


c


# In[118]:


b.capitalize()


# In[121]:


c.capitalize()


# In[122]:


c.split()


# In[123]:


b.split()


# In[124]:


b.replace('dollar','euro')


# In[125]:


c.replace('GHANAIANS','CANADIANS')


# In[129]:


d=b.replace('ghanaians','kumericans')
d.replace('dollar','euro')


# In[134]:


first='welcome to the {year} {prog} organized by {organizers}'.format(year=2022, organizers = 'OneQuantum Ghana', prog = 'Christian')


# In[137]:


third='welcome to the {} {prog} organized by {organizers}'.format(2023, organizers = 'OneQuantum Ghana', prog = 'Christian')


# In[138]:


third


# In[136]:


first


# In[139]:


second='my name is {0}, I am {1}cm tall'.format('chris',167)


# In[140]:


second


# # basic mathematics

# In[ ]:


#floor division


# In[143]:


7//5


# # Boolean Data Type

# In[145]:


2>75


# In[146]:


11.2==11.22


# In[147]:


type(11.2==11.22)


# # Dictionary

# In[151]:


p= {
    'Name':'chris',
    'telephone': '0501401269',
    'Gender': 'prefer not to say'
}

type(p)


# In[ ]:


type


# In[149]:


q= {
    'Name': 'Berthold',
    'Telephone':'0501335890',
    'Sex': 'none'
}

type(q)


# # Comparisons

# In[152]:


2<=10


# In[158]:


4>5


# # logical Operators

# In[161]:


(5<2) & (5>3)


# In[ ]:


#both statements have to be true for a positive answer, if one is false, then the statement is false


# # One way decisions

# In[168]:


x=5


# In[171]:


if x == 5:
    print('x  equal 5')


# In[174]:


if x > 4:
    print('x is greater than 4')


# In[175]:


if x != 6:
    print('x does not equal to 5')
    


# # Two way decision

# In[ ]:





# In[183]:


name = input('name ')


# In[185]:


if name == 'ofori':
    print('YOU ARE WELCOME',name)
else:
    print('I dont know you')


# In[188]:


menu = input('place your order ')
if menu == 'jollof':
    print('how much')
else:
    print ('we dont do this here')


# In[192]:


menu = input('place your order')
if menu == 'jollof':
    print('how much')
else:
    print('gedad the fok')


# # NESTED LOOP

# In[200]:


grade= 100
if grade > 60:
    print('\tstudent scored a passing grade')
if grade >= 90:
    print('\tstudent passed with A')
if grade >= 96:
    print('\tstudent passed with A+')


# In[208]:


grade = int(input ('enter your grade'))
if grade > 60:
    print('\tstudent scored a passing grade')
if grade >= 90:
    print('\tstudent passed with A')
if grade >= 96:
    print('\tstudent passed with A+')


# In[1]:


num = int(input('enter your grade please '))
if num >= 70 and num ==100:
    print('A')
elif num >= 60 and num <= 69:
    print('B')
elif num >= 40 and num <= 59:
    print('C')
elif num == 0:
    print('You have failed')
else:
    print('Grade doesnt exist')


# In[ ]:





# In[ ]:




