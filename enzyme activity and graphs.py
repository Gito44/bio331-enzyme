import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

times= [30,60,90,300,600,900,1500]
tube1= [0.176, 0.217, 0.242, 0.545, 0.971, 1.430, 2.283]
tube2= [0.160, 0.205, 0.246, 0.537, 0.955, 1.385, 2.201]
tube3= [0.164, 0.221, 0.250, 0.565, 0.959, 1.369, 2.119]
tube4= [0.155, 0.205, 0.250, 0.516, 0.951, 1.363, 2.164]
enzyme_concs=[2/1000,4/1000,6/1000,8/1000]
def enzyme_activity(data):
    enzyme_a=0
    count = 0
    for i in range(len(data)):
        activity=data[i]/times[i]
        enzyme_a+=activity
        count+=1
    return enzyme_a/count

V1= enzyme_activity(tube1)
V2= enzyme_activity(tube2)
V3= enzyme_activity(tube3)
V4= enzyme_activity(tube4)

activities=[V1,V2,V3,V4]

dict= {"activities": activities,
       "concs": enzyme_concs}

df= pd.DataFrame(dict)
trend= np.polyfit( df["concs"],df["activities"],1)
trendx= np.linspace(0,df["concs"].max(),100)
trendy= np.polyval(trend,trendx)
plt.plot(df["activities"], df["concs"], "bo", label="Data")
plt.plot(trendy,trendx, "r--", label="Trendline")
plt.xlabel("Enzyme concentration (enzyme volume/total volume)")
plt.ylabel("Enzyme activity")
plt.legend(loc="best")
plt.title("Enzyme Activity of Different Enzyme Concentrations")
plt.show()