import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

times= [30,60,90,300,600,900,1500]
tube1= [0.176, 0.217, 0.242, 0.545, 0.971, 1.430, 2.283]
tube2= [0.160, 0.205, 0.246, 0.537, 0.955, 1.385, 2.201]
tube3= [0.164, 0.221, 0.250, 0.565, 0.959, 1.369, 2.119]
tube4= [0.155, 0.205, 0.250, 0.516, 0.951, 1.363, 2.164]


dict= { "time": times,
        "tube1": tube1,
        "tube2": tube2,
        "tube3": tube3,
        "tube4": tube4}

df= pd.DataFrame(dict)

df["v1"]= np.gradient(df["tube1"],df["time"])
df["v2"]= np.gradient(df["tube2"],df["time"])
df["v3"]= np.gradient(df["tube3"],df["time"])
df["v4"]= np.gradient(df["tube4"],df["time"])


plt.plot(df["time"],df["tube1"],"bo" ,label="Tube 1")
plt.plot(df["time"],df["tube2"],"ro" , label="Tube 2")
plt.plot(df["time"],df["tube3"], "go" ,label="Tube 3")
plt.plot(df["time"],df["tube4"], "yo" ,label="Tube 4")
plt.plot(df["time"],df["tube1"],color="b",label="Tube 1")
plt.plot(df["time"],df["tube2"], color="r", label="Tube 2")
plt.plot(df["time"],df["tube3"],color="g",label="Tube 3")
plt.plot(df["time"],df["tube4"],color="y",label="Tube 4")
plt.legend(loc="best")
plt.title("Progress curves of Enzyme Catalysed Reactions")
plt.xlabel("Time (seconds)")
plt.ylabel("Volume (microliters)")
plt.show()

