from scipy.stats import ttest_ind

tube1=[0.005866666666666667,0.0036166666666666665,0.0026888888888888887,0.0018166666666666667,0.0016183333333333334,0.0015888888888888888,0.001522]
tube2=[0.005333333333333333,0.0034166666666666664,0.0027333333333333333,0.0017900000000000001,0.0015916666666666666,0.001538888888888889,0.0014673333333333333]
tube3=[0.0054666666666666665,0.003683333333333333,0.002777777777777778,0.0018833333333333332,0.0015983333333333333,0.001521111111111111,0.0014126666666666669]
tube4=[0.005166666666666667,0.0034166666666666664,0.002777777777777778,0.00172,0.0015849999999999998,0.0015144444444444443,0.0014426666666666667]

t_st1, p1 = ttest_ind(tube1,tube2)
t_st2, p2 = ttest_ind(tube1,tube3)
t_st3, p3 = ttest_ind(tube1,tube4)

print(p1,p2,p3)