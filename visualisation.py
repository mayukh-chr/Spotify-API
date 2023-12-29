import matplotlib.pyplot as plt
import numpy as np

#todo: year vs quantity graph
#       genre vs graph

x = np.linspace(0, 2 * np.pi, 200) #this is just the basic example
y = np.sin(x)                      #from the docs

                                #because I'm learning and i'm a noob
                                #at plt

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()