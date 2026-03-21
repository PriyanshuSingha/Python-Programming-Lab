import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,7,6,8,7]
plt.scatter(x,y,color='b',label='scatter points')
plt.title("scatter plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
import matplotlib.pyplot as plt
categories=['A','B','C','D']
values=[3,7,8,5]
plt.bar(categories,values,colour='g',label='Bar Data')
plt.title('bar Plot')
plt.xlabel("categories")
plt.ylabel("values")
plt.legend()
plt.show()