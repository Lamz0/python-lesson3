#Global variable 
global_var = 10 

def add_variables():
    #Local variable set initialy 
    local_var = 5 
    #adding global and local variable the first time 
    first_result= global_var + local_var

    #change the local variable for the second calculation 
    local_var = 10 
    second_result = global_var + local_var 
   
    return first_result, second_result
first, second = add_variables()
print('First result:', first)
print('Second result:', second)
