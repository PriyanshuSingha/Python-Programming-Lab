from matplotlib import colors
import matplotlib.pyplot as plt
sizes=[15,30,45,10]
labels=['A','B','C','D']
colours=['gold','yellowgreen','lightcoral','lightskyblue']
explode=(0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colours,autopct='%1.1f%%',shadow=True,startangle=140)
plt.title('Pie Chart')
plt.axis('equal')
plt.show()
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 50)
y =np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))
plt.contourf(x, y, z,levels=10, cmap='viridis')
plt.title('Contour Plot')
plt.colorbar()
plt.show()