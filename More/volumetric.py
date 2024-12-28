# Volumetric Weight Calculator
def volumetric(l,w,h):
    const_inch = 305
    const_cm = 5000
    inch_con = 25.4
    cm_con = 10
    # l = input('Length: ')
    li = int(l) / inch_con
    lc = int(l) / cm_con
    # w = input('Width: ')
    wi = int(w) / inch_con
    wc = int(w) / cm_con
    # h = input('Height: ')
    hi = int(h) / inch_con
    hc = int(h) / cm_con
    vol_weight_inch = (li * wi * hi) / const_inch
    vol_weight_cm = (lc * wc * hc) / const_cm
    print('Volumetric Weight with respect of Inches %.2f Kgs'%vol_weight_inch)
    print('volumetric Weight with respect of Centimeters %.2f Kgs'%vol_weight_cm)
volumetric(380,350,285)