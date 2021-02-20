def count_f(mylist):
    f = {}
    for i in mylist:
        if(i in f):
            f[i] += 1
        else:
              f[i] = 1
    return f 
mylist=["one","two","eleven","one","three","two","eleven","three","seven","eleven"]
print(count_f(mylist))

