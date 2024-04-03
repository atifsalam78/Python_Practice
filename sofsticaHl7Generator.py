'''HL7 ADT A01 messages generater'''
import random, string
from tkinter import *
import customtkinter
from customtkinter import *
from hl7apy.core import Message, Segment
from hl7apy.parser import parse_message, parse_segment, parse_field
from hl7apy import get_default_version, set_default_version, DEFAULT_ENCODING_CHARS
import random, string
from datetime import datetime as d
import datetime
import time
import sys
from hl7.client import MLLPClient
import json
from random import randrange
from datetime import timedelta

def sel():
   "To select options" 
   global opt  
   option_dict = {"P":"PRE Patients", "I":"In Patients", "E":"ER Patients", "O":"Out Patients"}   
   opt = check_var.get()   
     
   if check_var.get() == "P":
      opt = option_dict["P"]
   elif check_var.get() == "I":
      opt = option_dict["I"]
   elif check_var.get() == "E":
      opt = option_dict["E"]
   elif check_var.get() == "O":
      opt = option_dict["O"]     
   else:
      pre_checkbox.deselect()      

def spin():
   "Selection interval of time in which messages to be generate"           
   
def optionmenu_callback(choice):
    "Selection of HL7 message type"

    call_back_dict = {"A01":"ADT^A01^ADT_A01", "Other":"Others"}

    if optionmenu_var.get() == "A01":
      call_back = call_back_dict["A01"]
    elif optionmenu_var.get() == "Other":
      call_back = call_back_dict["Other"]
      
def exit_button():
   sys.exit()

def message_ADT_A01():
   '''HL7 ADT_A01 Message Generator according to version 2.4'''   
   global hl7_msg
   set_default_version("2.4")
   get_default_version()
   hl7_msg = Message("ADT_A01", version="2.4", encoding_chars=DEFAULT_ENCODING_CHARS)
   
   # Generating MSH message
   hl7_msg.msh.msh_3 = "REG"
   hl7_msg.msh.msh_4 = "AKUHNBH"
   hl7_msg.msh.msh_6 = "AKUHNBH"
   hl7_msg.msh.msh_7 = "202302031233"
   hl7_msg.msh.msh_9 = "ADT^A01^ADT_A01"
   hl7_msg.msh.msh_10 = "4203117"
   hl7_msg.msh.msh_11 = "P"
   hl7_msg.msh.msh_15 = "AL"
   hl7_msg.msh.msh_16 = "NE"

   # Generating EVN message
   hl7_msg.evn.evn_1 = "A01"
   hl7_msg.evn.evn_2 = "202302031233"
   hl7_msg.evn.evn_4 = "ENADMIN"
   hl7_msg.evn.evn_5 = "KOMBALEX00^Kombo^Alexander^Muoti^^^^^^^^^XX~Desktop"
   hl7_msg.evn.evn_6 = "202302031230"

   # Generating PID message
   hl7_msg.pid.pid_1 = "1"
   patient_identifier_list = "SO"+''.join((random.choice(string.digits) for i in range(8)))
   hl7_msg.pid.pid_3.pid_3_1 = patient_identifier_list
   
   # Generating Log File for Patient Identifier List
   mr_log = "log_file_mr" + ".csv"   
   with open (mr_log, "a") as log_file:
      log_file.write("\n")
      log_file.write(patient_identifier_list)

   hl7_msg.pid.pid_3.pid_3_4 = "SO"
   hl7_msg.pid.pid_3.pid_3_5 = "MR"
   hl7_msg.pid.pid_3.pid_3_6 = "SOFSTICA~" + "S"+''.join((random.choice(string.digits) for i in range(8)))+"^^^SO^EMR^SOFSTICA"

   last_name_list = ["Last1","Last2","Last3","Last4","Last5"]
   first_name_list = ["First1","First2","First3","First4","First5"]
   middle_name_list = ["middle1","middle2","middle3","middle4","middle5"]

   hl7_msg.pid.pid_5.pid_5_1 = random.choice(last_name_list)
   hl7_msg.pid.pid_5.pid_5_2 = random.choice(first_name_list)
   hl7_msg.pid.pid_5.pid_5_3 = random.choice(middle_name_list)

   # Generate random date of birth for PID_7
   def random_dob(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)   
   d1 = d.strptime('197001010130', '%Y%m%d%H%M')
   d2 = d.strptime('202301010450', '%Y%m%d%H%M')
   ad = random_dob(d1, d2)   

   hl7_msg.pid.pid_7 = ad.strftime('%Y%m%d%H%M')  
   hl7_msg.pid.pid_8 = ''.join((random.choice("MFU") for i in range(1)))
   hl7_msg.pid.pid_10 = "AS"
   hl7_msg.pid.pid_11.pid_11_1 = ''.join((random.choice(["Nishtar Road", "Abdullah Haroon Road","Zaibunnisa Street","Rashid Minhas Road","I. I. Chundrigar Road"]) for i in range(1)))
   hl7_msg.pid.pid_11.pid_11_2 = ''.join((random.choice(["Jehangir Road", "Saddar","Mohammad Ali Jinnah Road","Drigh Road ","Shaheen Complex"]) for i in range(1)))
   hl7_msg.pid.pid_11.pid_11_3 = "Karachi"
   hl7_msg.pid.pid_11.pid_11_4 = "Sindh"
   hl7_msg.pid.pid_11.pid_11_5 = "75230"
   hl7_msg.pid.pid_11.pid_11_6 = "PAK"
   hl7_msg.pid.pid_13.pid_13_1 ="92-326-51238"
   hl7_msg.pid.pid_13.pid_13_2 ="PRN"
   hl7_msg.pid.pid_13.pid_13_3 ="CELL"
   hl7_msg.pid.pid_16 = ''.join((random.choice("SMU") for i in range(1)))
   hl7_msg.pid.pid_17 = ''.join((random.choice(["MS", "CH"]) for i in range(1)))
   hl7_msg.pid.pid_18 = "AC"+''.join((random.choice(string.digits) for i in range(8)))
   hl7_msg.pid.pid_22 = ''.join((random.choice(["AS", "AF"]) for i in range(1)))

   # Genrating PV1 messag         
   hl7_msg.pv1.pv1_1 = "1"   

   if check_var.get() == "I":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_3.pv1_3_1 = ''.join((random.choice(["Ward1", "Ward2", "Ward3", "HDU", "ICU", "CCU", "Private"]) for i in range(1)))
      hl7_msg.pv1.pv1_3.pv1_3_2 = "Room"
      hl7_msg.pv1.pv1_3.pv1_3_3 = "1"      
      concatenate_pv1_3 = f"{hl7_msg.pv1.pv1_3.pv1_3_1}^{hl7_msg.pv1.pv1_3.pv1_3_2}^{hl7_msg.pv1.pv1_3.pv1_3_3}"

   elif check_var.get() == "E":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_3.pv1_3_1 = "Emergency"      
      concatenate_pv1_3 = f"{hl7_msg.pv1.pv1_3.pv1_3_1}^{hl7_msg.pv1.pv1_3.pv1_3_2}^{hl7_msg.pv1.pv1_3.pv1_3_3}"

   elif check_var.get() == "O" or check_var.get() == "P":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_3.pv1_3_1 = ''.join((random.choice(["Clinic1", "Clinic2", "Clinic3"]) for i in range(1)))
      concatenate_pv1_3 = f"{hl7_msg.pv1.pv1_3.pv1_3_1}^{hl7_msg.pv1.pv1_3.pv1_3_2}^{hl7_msg.pv1.pv1_3.pv1_3_3}"

   if check_var.get() == "I" or check_var.get() == "E" or check_var.get() == "P":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_4 = "ER"
   
   doct_id = ''.join((random.choice(["Doctor1", "Doctor2", "Doctor3"]) for i in range(1)))
   hl7_msg.pv1.pv1_7 = doct_id+"^"+doct_id+"Last"+"^"+doct_id+"First"+"^"+doct_id+"Middle"+"^^Dr.^^^^^^^XX"
   hl7_msg.pv1.pv1_8 = hl7_msg.pv1.pv1_7   

   if check_var.get() == "I":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_10 = "MED"
   else:
      hl7_msg.pv1.pv1_2 = check_var.get()  
   
   if check_var.get() == "I":   
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_14 = "ER"
   else:
      hl7_msg.pv1.pv1_2 = check_var.get()   
      
   if check_var.get() == "I":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_17 = hl7_msg.pv1.pv1_7
   else:
      hl7_msg.pv1.pv1_2 = check_var.get()

   if check_var.get() == "I":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_18 = "IN"
   elif check_var.get() == "E":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_18 = "ER"
   elif check_var.get() == "O":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_18 = "CLI"
   elif check_var.get() == "P":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_18 = "PRE"

   hl7_msg.pv1.pv1_19 = hl7_msg.pid.pid_18
   hl7_msg.pv1.pv1_20 = "SP"
   hl7_msg.pv1.pv1_39 = "SOFSTICA"

   if check_var.get() == "I":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_41 = "ADM"
   elif check_var.get() == "O" or hl7_msg.pv1.pv1_2 == "E":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_41 = "REG"
   elif check_var.get() == "P":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv1.pv1_41 = "PRE"

   date = d.now()
   hl7_msg.pv1.pv1_44 = date.strftime("%Y%m%d%H%M")

   # Generating PV2 message
   hl7_msg.pv2.pv2_1 = "1"     
   if check_var.get() == "O":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv2.pv2_36 = "N"        
   elif check_var.get() == "I":
         hl7_msg.pv1.pv1_2 = check_var.get()
         hl7_msg.pv2.pv2_2 = hl7_msg.pv1.pv1_3
         hl7_msg.pv2.pv2_10 = "5"
         hl7_msg.pv2.pv2_11 = "5"
         hl7_msg.pv2.pv2_25 = "ER"
         hl7_msg.pv2.pv2_36 = "N"        
   elif check_var.get() == "E" or check_var.get() == "P":
      hl7_msg.pv1.pv1_2 = check_var.get()
      hl7_msg.pv2.pv2_25 = "ER"
      hl7_msg.pv2.pv2_36 = "N"    

   # Generating OBX messages
   obx1 = Message("ADT_A01", version="2.4")
   obx1 = Segment('OBX', version="2.4")   
   obx1.obx_1 = "1"
   obx1.obx_2 = "ST"
   obx1.obx_3 = "1010.1^WEIGHT^CPT4D"
   obx1.obx_5 = "70"
   obx1.obx_6 = "kg"
   obx1.obx_11 = "F"
   obx1.obx_14 = date.strftime("%Y%m%d%H%M")

   obx2 = Message("ADT_A01", version="2.4")
   obx2 = Segment('OBX', version="2.4")
   obx2.obx_1 = "2"
   obx2.obx_2 = "ST"
   obx2.obx_3 = "1010.3^HEIGHT^CPT4"
   obx2.obx_5 = "175"
   obx2.obx_6 = "cm"
   obx2.obx_11 = "F"
   obx2.obx_14 = date.strftime("%Y%m%d%H%M")

   obx3 = Message("ADT_A01", version="2.4")
   obx3 = Segment('OBX', version="2.4")
   obx3.obx_1 = "3"
   obx3.obx_2 = "TX"
   obx3.obx_3 = "APS.FSMRL^Morse Fall Scale Risk Level^ADM"
   obx3.obx_5 = "No Fall Risk"
   obx3.obx_11 = "F"
   
   obx4 = Message("ADT_A01", version="2.4")
   obx4 = Segment('OBX', version="2.4")
   obx4.obx_1 = "4"
   obx4.obx_2 = "TX"
   obx4.obx_3 = "APS.FSMSC^Morse Fall Scale Score^ADM"
   obx4.obx_5 = "0"
   obx4.obx_11 = "F"

   obx5 = Message("ADT_A01", version="2.4")
   obx5 = Segment('OBX', version="2.4")
   obx5.obx_1 = "5"
   obx5.obx_2 = "CE"
   obx5.obx_3 = "APS.FSMSD^Morse Fall Scale Secondary Diagnosis^ADM"
   obx5.obx_5 = "1^No"
   obx5.obx_11 = "F"

   obx6 = Message("ADT_A01", version="2.4")
   obx6 = Segment('OBX', version="2.4")
   obx6.obx_1 = "6"
   obx6.obx_2 = "CE"
   obx6.obx_3 = "NED.TRL^Limitations *^ADM||1^No Limitations"
   obx6.obx_5 = "1^No"
   obx6.obx_11 = "F"

   obx7 = Message("ADT_A01", version="2.4")
   obx7 = Segment('OBX', version="2.4")
   obx7.obx_1 = "7"
   obx7.obx_2 = "CE"
   obx7.obx_3 = "NED.TRMOA.AKUG^Mode of Arrival *^ADM"
   obx7.obx_5 = "7^Walk-In"
   obx7.obx_11 = "F"

   obx8 = Message("ADT_A01", version="2.4")
   obx8 = Segment('OBX', version="2.4")
   obx8.obx_1 = "8"
   obx8.obx_2 = "CE"
   obx8.obx_3 = "NED.TRSI^Source of Information *^ADM"
   obx8.obx_5 = "4^Relative~1^Patient"
   obx8.obx_11 = "F"

   obx9 = Message("ADT_A01", version="2.4")
   obx9 = Segment('OBX', version="2.4")
   obx9.obx_1 = "9"
   obx9.obx_2 = "TX"
   obx9.obx_3 = "NEURO.PA2^Pain Intensity^ADM"
   obx9.obx_5 = "8"
   obx9.obx_11 = "F"

   obx10 = Message("ADT_A01", version="2.4")
   obx10 = Segment('OBX', version="2.4")
   obx10.obx_1 = "10"
   obx10.obx_2 = "CE"
   obx10.obx_3 = "RESP.OXDMT^Oxygen Delivery Method^ADM"
   obx10.obx_5 = "1^Room Air"
   obx10.obx_11 = "F"

   obx11 = Message("ADT_A01", version="2.4")
   obx11 = Segment('OBX', version="2.4")
   obx11.obx_1 = "11"
   obx11.obx_2 = "TX"
   obx11.obx_3 = "RESP.POSAT^Pulse Oximetry^ADM"
   obx11.obx_5 = "96"
   obx11.obx_11 = "F"

   obx12 = Message("ADT_A01", version="2.4")
   obx12 = Segment('OBX', version="2.4")
   obx12.obx_1 = "12"
   obx12.obx_2 = "TX"
   obx12.obx_3 = "VS.BMI^BMI^ADM"
   obx12.obx_5 = "22.8"
   obx12.obx_11 = "F"

   obx13 = Message("ADT_A01", version="2.4")
   obx13 = Segment('OBX', version="2.4")
   obx13.obx_1 = "13"
   obx13.obx_2 = "TX"
   obx13.obx_3 = "VS.BMICLAS^Body Mass Index (BMI) Classification^ADM"
   obx13.obx_5 = "Normal"
   obx13.obx_11 = "F"

   obx14 = Message("ADT_A01", version="2.4")
   obx14 = Segment('OBX', version="2.4")
   obx14.obx_1 = "14"
   obx14.obx_2 = "TX"
   obx14.obx_3 = "VS.BP^Blood Pressure^ADM"
   obx14.obx_5 = "148/88"
   obx14.obx_11 = "F"

   obx15 = Message("ADT_A01", version="2.4")
   obx15 = Segment('OBX', version="2.4")
   obx15.obx_1 = "15"
   obx15.obx_2 = "CE"
   obx15.obx_3 = "VS.BPLO^Blood Pressure Location^ADM"
   obx15.obx_5 = "1^Lt brachial"
   obx15.obx_11 = "F"

   obx16 = Message("ADT_A01", version="2.4")
   obx16 = Segment('OBX', version="2.4")
   obx16.obx_1 = "16"
   obx16.obx_2 = "TX"
   obx16.obx_3 = "VS.BPM^Blood Pressure Mean^ADM"
   obx16.obx_5 = "108"
   obx16.obx_11 = "F"

   obx17 = Message("ADT_A01", version="2.4")
   obx17 = Segment('OBX', version="2.4")
   obx17.obx_1 = "17"
   obx17.obx_2 = "CE"
   obx17.obx_3 = "VS.BPP^Blood Pressure Position^ADM"
   obx17.obx_5 = "1^Supine"
   obx17.obx_11 = "F"
   
   obx18 = Message("ADT_A01", version="2.4")
   obx18 = Segment('OBX', version="2.4")
   obx18.obx_1 = "18"
   obx18.obx_2 = "TX"
   obx18.obx_3 = "VS.PULSE^Pulse Rate^ADM"
   obx18.obx_5 = "57"
   obx18.obx_11 = "F"

   obx19 = Message("ADT_A01", version="2.4")
   obx19 = Segment('OBX', version="2.4")
   obx19.obx_1 = "19"
   obx19.obx_2 = "CE"
   obx19.obx_3 = "VS.PULSEA1^Pulse Strength^ADM"
   obx19.obx_5 = "4^3+ Normal"
   obx19.obx_11 = "F"

   obx20 = Message("ADT_A01", version="2.4")
   obx20 = Segment('OBX', version="2.4")
   obx20.obx_1 = "20"
   obx20.obx_2 = "CE"
   obx20.obx_3 = "VS.PULSERY^Pulse Rhythm^ADM"
   obx20.obx_5 = "1^Regular"
   obx20.obx_11 = "F"

   obx21 = Message("ADT_A01", version="2.4")
   obx21 = Segment('OBX', version="2.4")
   obx21.obx_1 = "21"
   obx21.obx_2 = "TX"
   obx21.obx_3 = "VS.RESP^Respiratory Rate^ADM"
   obx21.obx_5 = "16"

   obx22 = Message("ADT_A01", version="2.4")
   obx22 = Segment('OBX', version="2.4")
   obx22.obx_1 = "22"
   obx22.obx_2 = "CE"
   obx22.obx_3 = "VS.RESPD^Respiratory Depth^ADM"
   obx22.obx_5 = "1^Normal"
   obx22.obx_11 = "F"

   obx23 = Message("ADT_A01", version="2.4")
   obx23 = Segment('OBX', version="2.4")
   obx23.obx_1 = "23"
   obx23.obx_2 = "CE"
   obx23.obx_3 = "VS.RESPE1^Respiratory Effort^ADM"
   obx23.obx_5 = "1^Normal for Patient~2^Spontaneous~3^Non-Labored"
   obx23.obx_11 = "F"

   obx24 = Message("ADT_A01", version="2.4")
   obx24 = Segment('OBX', version="2.4")
   obx24.obx_1 = "24"
   obx24.obx_2 = "CE"
   obx24.obx_3 = "VS.RESPT^Respiratory Pattern^ADM"
   obx24.obx_5 = "1^Normal"
   obx24.obx_11 = "F"

   obx25 = Message("ADT_A01", version="2.4")
   obx25 = Segment('OBX', version="2.4")
   obx25.obx_1 = "25"
   obx25.obx_2 = "TX"
   obx25.obx_3 = "VS.TEMP^Temperature^ADM"
   obx25.obx_5 = "36.2^97.2"
   obx25.obx_11 = "F"

   # Generating AL1 message
   rand_al1 = str(random.randint(1,3))
   if rand_al1 == "1":
      hl7_al1 = Message("ADT_A01", version="2.4")
      hl7_al1 = Segment('AL1', version="2.4")
      hl7_al1.al1_1 = "1"
      hl7_al1.al1_2 = "DA"
      hl7_al1.al1_3 = "MS01092264^No Known Drug Allergy^^No Known Drug Allergy^^allergy.id"
      hl7_al1.al1_4 = "U"      
      hl7_al1.al1_6 = "20221109"   
   elif rand_al1 == "2":
      hl7_al1 = Message("ADT_A01", version="2.4")
      hl7_al1 = Segment('AL1', version="2.4")
      hl7_al1.al1_1 = "1"
      hl7_al1.al1_2 = "DA"
      hl7_al1.al1_3 = "MS00747674^Nsaids^^Nsaids^^allergy.id"
      hl7_al1.al1_4 = "MI"
      hl7_al1.al1_5 = "Known Asthmatic"
      hl7_al1.al1_6 = "20221202"
   elif rand_al1 == "3":
      hl7_al1 = Message("ADT_A01", version="2.4")
      hl7_al1 = Segment('AL1', version="2.4")
      hl7_al1.al1_1 = "1"
      hl7_al1.al1_2 = "DA"
      hl7_al1.al1_3 = "MS01095679^Clindamycin^^Clindamycin^^allergy.id"
      hl7_al1.al1_4 = "U"
      hl7_al1.al1_5 = "rash"
      hl7_al1.al1_6 = "20230203"

   # Get Data from config
   with open("config.json", 'r') as c:
      params = json.load(c) ["params"]

   host = params["local_host"]
   port = params["port"]   

   # Generating and printing DG1 message
   rand_dg1 = str(random.randint(1,2))
   msg_dg1 = ""  
   if rand_dg1 == "1":
      hl7_dg1 = Message("ADT_A01", version="2.4")
      hl7_dg1 = Segment('DG1', version="2.4")
      hl7_dg1.dg1_1 = "1"
      hl7_dg1.dg1_3 = "K59.00^K59.00 - Constipation, unspecified^I10"
      hl7_dg1.dg1_6 = "W"      
      msg_dg1 = hl7_dg1.to_er7().replace('\r','\n')


   msg_1 = hl7_msg.to_er7().replace("\R\\", "~").replace("\S\\","^")
   msg = msg_1+"\n"+obx1.to_er7().replace("\r","\n")+"\n"+obx2.to_er7().replace("\r","\n")+"\n"+obx3.to_er7().replace("\r","\n")+"\n"+obx4.to_er7().replace("\r","\n")+"\n"+obx5.to_er7().replace("\r","\n")+"\n"+obx6.to_er7().replace("\r","\n")+"\n"+obx7.to_er7().replace("\r","\n")+"\n"+obx8.to_er7().replace("\r","\n")+"\n"+obx9.to_er7().replace("\r","\n")+"\n"+obx10.to_er7().replace("\r","\n")+"\n"+obx11.to_er7().replace("\r","\n")+"\n"+obx12.to_er7().replace("\r","\n")+"\n"+obx13.to_er7().replace("\r","\n")+"\n"+obx14.to_er7().replace("\r","\n")+"\n"+obx15.to_er7().replace("\r","\n")+"\n"+obx16.to_er7().replace("\r","\n")+"\n"+obx17.to_er7().replace("\r","\n")+"\n"+obx18.to_er7().replace("\r","\n")+"\n"+obx19.to_er7().replace("\r","\n")+"\n"+obx20.to_er7().replace("\r","\n")+"\n"+obx21.to_er7().replace("\r","\n")+"\n"+obx22.to_er7().replace("\r","\n")+"\n"+obx23.to_er7().replace("\r","\n")+"\n"+obx24.to_er7().replace("\r","\n")+"\n"+obx25.to_er7().replace("\r","\n")+"\n"+hl7_al1.to_er7().replace("\r","\n")+"\n"+msg_dg1  

   # Sending to mirth connector
   with MLLPClient(host, port) as client:
      client.send_message(msg)      
   
def messageGenerator():
   "printing/generated desired number of messages"      
   counter = 1   
   os.system('cls' if os.name=='nt' else 'clear')
   while counter <= int(msg1.get()):            
      message_ADT_A01()              
      if counter > int(msg1.get()):         
         break
      else:
         counter += 1
def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

def time_interval_generator():
   "printing/generated desired number of messages" 
   num_msg = time_end_var.get()
   current_msg = 0

   while num_msg > current_msg:      
      message_ADT_A01()
      current_msg += 1  
      time.sleep(time_int_var.get())
      
if __name__=="__main__":

   customtkinter.set_appearance_mode("System")
   customtkinter.set_default_color_theme("green")
   root = customtkinter.CTk()
   root.title("HL7 Message Generator")
   root.geometry(f"{700}x{400}")
   root.resizable(0,0)

   opt_var = IntVar()
   check_var = StringVar()
   optionmenu_var = StringVar(value="A01")  # set initial value
   time_end_var = IntVar(value=0)
   time_int_var = IntVar(value=0)  

   # Option Frame 2
   Opt_frame2 = customtkinter.CTkFrame(master=root,width=25, height=25)
   Opt_frame2.pack(anchor=CENTER, pady=25)   

   # HL7 Message Type
   msg_type_heading = customtkinter.CTkLabel(master=Opt_frame2, text=" Type of Messages",font=("Tahoma", 14))
   msg_type_heading.pack()

   msg_type = customtkinter.CTkOptionMenu(master=Opt_frame2,values=["A01","Other"], command=optionmenu_callback, variable=optionmenu_var)
   msg_type.pack()

   # create tab view
   tabview = customtkinter.CTkTabview(master=Opt_frame2, width=250)
   tabview.pack()
   tabview.add("CTkTabview")
   tabview.add("No. of Messages")
   tabview.add("Time Interval")   
   
   # Number of Messages
   msg_heading = customtkinter.CTkLabel(tabview.tab("No. of Messages"), text=" Number of Messages",font=("Tahoma", 14)).pack()
   msg1 = Spinbox(tabview.tab("No. of Messages"), text="Number of Messages", font=("Tahoma", 12),from_= 1, to = 100)
   msg1.pack(padx=3)
   generate_btn_msg = customtkinter.CTkButton(tabview.tab("No. of Messages"), text="Generate",text_color="black",width=80, height=30,font=("Tahoma", 12),command=messageGenerator).pack(padx=3, pady=8)
   exit_btn = customtkinter.CTkButton(tabview.tab("No. of Messages"), text="Exit",text_color="black",width=80, height=30,font=("Tahoma", 12), command=root.quit).pack(padx=3)   

   # Time Interval
   time_heading = customtkinter.CTkLabel(tabview.tab("Time Interval"), text="Time Interval (Seconds)",font=("Tahoma", 14)).pack()
   time_interval = Spinbox(tabview.tab("Time Interval"), text="Time Interval", font=("Tahoma", 12),textvariable = time_int_var, from_= 0, to = 59).pack(padx=3)
   # Time Ending
   time_end_heading = customtkinter.CTkLabel(tabview.tab("Time Interval"), text="Number of Messages",font=("Tahoma", 14)).pack()
   time_end = Spinbox(tabview.tab("Time Interval"), text="Number of Messages", font=("Tahoma", 12),textvariable = time_end_var,from_= 0, to = 59).pack(padx=3)
   generate_btn_time = customtkinter.CTkButton(tabview.tab("Time Interval"), text="Generate",text_color="black",width=80, height=30,font=("Tahoma", 12),command=time_interval_generator).pack(padx=3, pady=8)
   exit_btn = customtkinter.CTkButton(tabview.tab("Time Interval"), text="Exit",text_color="black",width=80, height=30,font=("Tahoma", 12), command=root.quit).pack(padx=3)   

   # Radio Button
   pre_checkbox = customtkinter.CTkRadioButton(master=Opt_frame2, text="P - Pre Patients", font=("Tahoma", 12),variable=check_var, value="P",command=sel)
   pre_checkbox.pack(side=LEFT,padx=20, pady=10)

   in_checkbox = customtkinter.CTkRadioButton(master=Opt_frame2, text="I-In Patients", font=("Tahoma", 12), variable=check_var, value="I", command=sel)
   in_checkbox.pack(side=LEFT,padx=20, pady=10)

   er_checkbox = customtkinter.CTkRadioButton(master=Opt_frame2, text="E-ER Patients", font=("Tahoma", 12), variable=check_var, value="E", command=sel)
   er_checkbox.pack(side=LEFT, padx=20, pady=10)

   op_checkbox = customtkinter.CTkRadioButton(master=Opt_frame2, text="O-Out Patients", font=("Tahoma", 12), variable=check_var, value="O", command=sel)
   op_checkbox.pack(side=LEFT, padx=20, pady=10)
   
   root.mainloop()