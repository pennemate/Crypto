
def gcd(r1, r2):
    if(r1==r2):     #if numbers are the same
        return r2
    i=0             #counter
    s=[1,0]         
    t=[0,1]
    q=[]            #quotient array
    l=[]            #the final list to print
    while r2!=0:    # condition- stay above 0
        q1=r1/r2
        q.extend([q1])          #add the quotient to its array
        l=[i,q[i],r1,r2]    
        (r1,r2)=(r2, r1%r2)     #get the mod and switch the variables
        if(i>1):                #only adjust s and t if i is greater than 1
            x=s[i-2]-q[i-2]*s[i-1]
            y=t[i-2]-q[i-2]*t[i-1]
            s.extend([x])       #add s and t to their respective arrays
            t.extend([y])
            
        l.extend([r2,s[i],t[i]])    
        i+=1
        print('\t'.join(map(str,l)))    #print with the tab
    x=s[i-2]-q[i-2]*s[i-1]              #takes care of the extra printout
    y=t[i-2]-q[i-2]*t[i-1]              #as per the algo
    l[5]=x                              #replace the old s and t
    l[6]=y
    print('\t'.join(map(str,l)))
    ret=[r1,l[6]]       #return both the gcf and inverse
    return ret
    
def main():
    print ("This is the extended Euclidean Algorithm Calculator\n")
    x=int(raw_input("Please enter the larger integer\n"))
    y=int(raw_input("Please enter the smaller integer\n"))
    z=gcd(x, y);
    if(type(z) is not int and z[1]<0):
        z[1]+=x
        print ("\nThe gcf of the two numbers is " + str(z[0]))
        print("\nThe inverse of "+ str(y) + " is "+ str(z[1]))
    else:
        print ("The gcf of the two numbers is " + str(x))
main()
