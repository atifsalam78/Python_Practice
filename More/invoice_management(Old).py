from datetime import datetime
import os
import csv

os.system('cls' if os.name=='nt' else 'clear')
s_no = 0

while True:
    try:
        s_no = s_no + 1
        print(s_no)
        purchase_order = input("Purchase Order Number: ")
        ebs_receipt_no = input("EBS Receipt Number: ")
        fusion_receipt_no = int(input("Fusion Receipt Number: "))
        invoice_ref = input("Invoice Reference Number: ")
        invoice_date = datetime.now().strftime('%Y-%m-%d')
        invoice_submit_date = datetime.now().strftime('%Y-%m-%d')
        invoice_amount = float(input("Invoice Amount: "))
        Concatenate_fusion  = f"{purchase_order}-{fusion_receipt_no}"
        Concatenate_ebs = f"{purchase_order}-{ebs_receipt_no}"
        
        header = ['Concatenate Fusion', 'Concatenate EBS','Serial No','Purchase Order No',
                  'EBS Receipt No','Fusion Receipt No', 'Invoice Ref','Invoice Dated',
                  'Invoice Submission Date', 'Invoice Amount']
        
        data = [Concatenate_fusion,Concatenate_ebs,s_no,purchase_order,ebs_receipt_no,
                fusion_receipt_no,invoice_ref,invoice_date,invoice_submit_date,invoice_amount]
        
        with open ("Invoice.csv","a", encoding="UTF8", newline="") as invoice:
            writer = csv.writer(invoice)
            # writer.writerow(header)
            writer.writerow(data)
            
        
        cont = input("Do you want to continue (Y/N): ")
        if cont == "n" or cont == "N":
            print("Thank you, Good Bye!")            
            break
        else:
            continue
    except ValueError:
        input("Value Error")
    except KeyError:
        print(f"Key Error")