# def matrix(r,c):
#     mat=[]
#     for i in range(r):
#         row=[]
#         for j in range(c):
#             value=int(input(f"enter the value of{[i,j]}"))
#             row.append(value)
#         mat.append(row)
#     return mat 
# print(matrix(2,2))
#     #addition of matrix
# def add():
#     p=int(input("enter the number of matrix you have to add"))
#     for i in range(p):
#         r=int(input("enter the number of rows you want"))
#         c=int(input("enter the number of column you want"))
#         if i==0:
#             a=matrix(r,c)
#         else:
#             b=matrix(r,c)

a=[[1, 2], [3, 4]]
b=[[0, 3], [2, 1]]
c=[]
for i in range(len(a)):
    row=[]
    for k in range(len(b)):
        row.append(a[i][k] + b[i][k])
    c.append(row)
print(c)




