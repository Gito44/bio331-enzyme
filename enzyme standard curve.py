import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


tubes=[1/200,1/400,1/800,1/1600,1/3200]
absorbances=[1.225,0.627,0.314, 0.160, 0.082]

df= pd.DataFrame({"concentration": tubes, "absorbances": absorbances})
xtrend= np.linspace(0,df["concentration"].max()+0.002,100)
fit = np.polyfit(df["concentration"],df["absorbances"],1)
ytrend= np.polyval(fit,xtrend)
plt.plot(df['concentration'], df['absorbances'], 'bo',  label='Data')
plt.plot(xtrend, ytrend, 'r', label='Trendline')
plt.legend(loc='best')
plt.xlabel('Concentration (product volume/total volume)')
plt.ylabel('Optical Density')
plt.title("Standard Curve")
plt.show()


print(f'y = {fit[0]:.3f}x + {fit[1]:.3f}')