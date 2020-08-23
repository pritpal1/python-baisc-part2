from numpy import  *
arr = array([8,15,16])
#arr = array([8,15,16.0])#one float value convert all data into float
#arr = array([7,8],float)#data in Int,if write float as type it convert into float
print(arr.dtype)
print(arr)

#linspace it contain 3 element:start,stop,step is breaking range into parts
ls = linspace(0,16,10)
#ls=linspace(0,20) #skip mid value it give 15 parts
#print(ls)

#arange:start,stop,step is move no. of step
ar = arange(1,15,2)
#print(ar)

#logspace:start ,end,step:it print using log values
log = logspace(1,40,5)
#print(log)
#print('%.2f' %log[0])#to print 1st value

#zeros() and ones() are used when all val. are 0 or 1,with their size
z = zeros(4)
o = ones(5,int)
#print(z)
#print(o)