from math import ceil

print("\n***************************Response Time Analyse***************************\n")

t1 = (7,3)   #execution time,time period,deadline
t2 = (12,3)
t3 = (20,5)

no_task = 3
#PRIORITY T1 > T2 > T3                  #according to rate monotonic
execution = [ t1[1],t2[1],t3[1] ]       #values entered in priority order
period = [ t1[0],t2[0],t3[0] ]          #values entered in priority order
deadline = [ t1[0],t2[0],t3[0] ]        #values entered in priority order

for t in range(no_task):
    print( "task "+ str(t) +" -> exe time: "+ str(execution[t]) +" period: "+ str(period[t]) )
print("\n")
  
def response_time(n,memory):     #for first process give n=0 not 1 and 
    ans = execution[n]    #adding execution time
    for i in range(n):
        ans += ceil(memory/period[i])*execution[i]
    return ans
            
for t in range(no_task):
    flag = 0
    memory = execution[t]           #value of first response time
    rt = response_time(t,memory)
    while rt <= deadline[t]:
        if rt == memory:
            flag = 1
            print("Task "+ str(t+1) +" is schedulable as: R = "+ str(memory) +" <= "+ str(deadline[t]))
            break
        else:
            memory = rt
            rt = response_time(t,memory)
    if flag != 1:
        print("Task "+ str(t+1) +" is NOT schedulable as: R = "+ str(memory) +" <= "+ str(deadline[t]))
        
    
