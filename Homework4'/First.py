def temp_converter(Tf):
    Tc = (5/9)*(Tf-32)
    return  Tc;
Tf = int(input("Enter temp in Fahrenheit :")) 
print(temp_converter(Tf) ) 