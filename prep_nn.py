def z(w,x,b):
    wx = 0
    for i in range(len(w)):
        wx += w[i]*x[i]
    wxb = wx + b
    return wxb
'''
w = [0.37, 0.95, 0.73]
x = [1,2,3]
b = 0.6
print(z(w,x,b))
'''

def r(lst):
    ny_lst = []
    for num in lst:
        if num < 0:
            ny_lst.append(0)
        else:
            ny_lst.append(num)
    return ny_lst
'''
lst = [-1,2,4,-5]
print(r(lst))
'''

def f_pass(w,x,b):
    lst=[]
    weighted_sum = z(w,x,b)
    lst.append(weighted_sum)
    y = r(lst)
    return y
'''
w = [0.37, 0.95, 0.73]
x = [1,2,3]
b = 0.6
output = f_pass(w,x,b)
print("Weights:", w)
print("Bias:", b)
print("Input:", x)
print("Output of forward pass:", output)
'''
if __name__ == "__main__":
    w = [0.37, 0.95, 0.73]
    x = [1,2,3]
    b = 0.6
    Output = f_pass(w,x,b)
    print("Weights:", w)
    print("Bias:", b)
    print("Input:", x)
    print("Output of forward pass:", Output)

