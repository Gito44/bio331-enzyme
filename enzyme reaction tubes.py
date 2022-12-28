import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

times= [30,60,90,300,600,900,1500]
tube1= [0.052,0.062,0.068,0.142,0.246,0.358,0.566]
tube2= [0.048,0.059,0.069,0.140,0.242,0.347,0.546]
tube3= [0.049,0.063,0.070,0.147,0.243,0.343,0.526]
tube4= [0.047,0.059,0.070,0.135,0.241,0.342,0.537]


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
plt.plot(df["time"],df["tube1"],color="b")
plt.plot(df["time"],df["tube2"], color="r")
plt.plot(df["time"],df["tube3"],color="g")
plt.plot(df["time"],df["tube4"],color="y")
plt.legend(loc="best")
plt.title("OD Values of Enzyme Catalysed Reactions")
plt.xlabel("Time (seconds)")
plt.ylabel("Optical Density")
plt.show()

