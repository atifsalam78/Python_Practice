def addback():
    qty = float(input('Quantity: '))
    pri = float(input('Price: '))
    per = float(input('Percentage: '))
    per1 = (100 - per) / 100
    pri1 = pri / per1
    add_back = qty * pri1
    # print('Percentage is %.3f' % per1)
    # print('Price is %.3f ' % pri1)
    print('Valve to be add in quotation after income tax: %.2f'%add_back)
addback()