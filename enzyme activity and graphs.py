import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

times= [30,60,90,300,600,900,1500]
tube1= [0.528, 0.651, 0.726, 1.635, 2.913, 4.290, 6.849]
tube2= [0.480, 0.615, 0.738, 1.611, 2.865, 4.155, 6.603]
tube3= [0.492, 0.663, 0.750, 1.696, 2.877, 4.107, 6.357]
tube4= [0.465, 0.615, 0.750, 1.548, 2.853, 4.089, 6.492]
enzyme_concs=[0.67,1.33,2.00,2.67]

def enzyme_activity(data):
    enzyme_a=0
    count = 0

    for i in range(len(data)):
        activity=data[i]/times[i]
        enzyme_a+=activity
        count+=1

    return enzyme_a/count*10000

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
plt.plot( df["concs"],df["activities"], "bo", label="Data")
plt.plot(trendx,trendy, "r--", label="Trendline")
plt.xlabel("Enzyme concentration (uL/mL)")
plt.ylabel("Enzyme activity (10e-4) (uL/second)")
plt.legend(loc="best")
plt.title("Enzyme Activity of Different Enzyme Concentrations")
plt.show()
