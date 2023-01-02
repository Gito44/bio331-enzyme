tube1= [0.052,0.062,0.068,0.142,0.246,0.358,0.566]
tube2= [0.048,0.059,0.069,0.140,0.242,0.347,0.546]
tube3= [0.049,0.063,0.070,0.147,0.243,0.343,0.526]
tube4= [0.047,0.059,0.070,0.135,0.241,0.342,0.537]






def determine_product(data):
    product_conc = []
    for item in data:
        conc = (item - 0.009) / 243.966
        volume = conc * 3000
        product_conc.append(volume)
    print(product_conc)
    return


determine_product(tube1)
determine_product(tube2)
determine_product(tube3)
determine_product(tube4)