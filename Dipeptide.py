import csv
import numpy as np
from collections import Counter
from Bio import SeqIO
import os

data=[]
header = ["AA","AC","AD","AE", "AF","AG", "AH","AI","AK","AL", "AM","AN","AP","AQ","AR","AS","AT","AV","AW","AY","CA","CC","CD","CE", "CF","CG", "CH","CI","CK","CL", "CM","CN","CP","CQ","CR","CS","CT","CV","CW","CY","DA","DC","DD", "DE", "DF","DG", "DH","DI","DK","DL", "DM","DN","DP","DQ","DR","DS","DT","DV","DW","DY","EA","EC","ED", "EE", "EF","EG", "EH","EI","EK","EL", "EM","EN","EP","EQ","ER","ES","ET","EV","EW","EY","FA","FC","FD", "FE", "FF","FG", "FH","FI","FK","FL", "FM","FN","FP","FQ","FR","FS","FT","FV","FW","FY","GA","GC","GD", "GE", "GF","GG", "GH","GI","GK","GL", "GM","GN","GP","GQ","GR","GS","GT","GV","GW","GY","HA","HC","HD", "HE", "HF","HG", "HH","HI","HK","HL", "HM","HN","HP","HQ","HR","HS","HT","HV","HW","HY","IA","IC","ID", "IE", "IF","IG", "IH","II","IK","IL", "IM","IN","IP","IQ","IR","IS","IT","IV","IW","IY","KA","KC","KD", "KE", "KF","KG", "KH","KI","KK","KL", "KM","KN","KP","KQ","KR","KS","KT","KV","KW","KY","LA","LC","LD", "LE", "LF","LG", "LH","LI","LK","LL", "LM","LN","LP","LQ","LR","LS","LT","LV","LW","LY","MA","MC","MD", "ME", "MF","MG", "MH","MI","MK","ML", "MM","MN","MP","MQ","MR","MS","MT","MV","MW","MY","NA","NC","ND", "NE", "NF","NG", "NH","NI","NK","NL", "NM","NN","NP","NQ","NR","NS","NT","NV","NW","NY","PA","PC","PD", "PE", "PF","PG", "PH","PI","PK","PL", "PM","PN","PP","PQ","PR","PS","PT","PV","PW","PY","QA","QC","QD", "QE", "QF","QG", "QH","QI","QK","QL", "QM","QN","QP","QQ","QR","QS","QT","QV","QW","QY","RA","RC","RD", "RE", "RF","RG", "RH","RI","RK","RL", "RM","RN","RP","RQ","RR","RS","RT","RV","RW","RY","SA","SC","SD", "SE", "SF","SG", "SH","SI","SK","SL", "SM","SN","SP","SQ","SR","SS","ST","SV","SW","SY","TA","TC","TD", "TE", "TF","TG", "TH","TI","TK","TL", "TM","TN","TP","TQ","TR","TS","TT","TV","TW","TY","VA","VC","VD", "VE", "VF","VG", "VH","VI","VK","VL", "VM","VN","VP","VQ","VR","VS","VT","VV","VW","VY","WA","WC","WD", "WE", "WF","WG", "WH","WI","WK","WL", "WM","WN","WP","WQ","WR","WS","WT","WV","WW","WY","YA","YC","YD", "YE", "YF","YG", "YH","YI","YK","YL", "YM","YN","YP","YQ","YR","YS","YT","YV","YW","YY"]
'''with open('DPC.csv', 'a+', newline = '') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    writer.writeheader()'''

with open('Rnewdata.csv', mode='r', newline='') as csvreader:
    reader = csv.reader(csvreader)
    for rows,row in enumerate(reader,1):
        da = ''.join(row)
        #print(da)
        length = len(da) - 1
        #print(length)
        data1 = []
        for i in range(0, length):
            a = da[i] + da[i+1]
            data1.append(a)
        #print(data1)
        #data = []
        for symbol in header:
            ctr = 0
            for sym in data1:
                if sym == symbol:
                    ctr += 1
            data.append(float(ctr) / len(data1))

    ak = np.asarray(data)
    di = ak.reshape(7800, 400)  # For R new data 2017 (GPS-MSP)
    #di = ak.reshape(3038, 400)  # For K new data 2017 (GPS-MSP)
    # di = ak.reshape(1480, 400)  # For R-methylation data complete
    # di = ak.reshape(1745, 400)  # For K-methylation data complete
    # di = ak.reshape(370, 400)     #For R-methylation data
    #di = ak.reshape(443, 400)     #For K-methylation data
    # di = ak.reshape(2906, 400)      # For R data 2020
    print(di)
    print(di.shape)
        #print(data)

        #with open('DPC.csv', 'a', newline='') as csvfile:
            #writer = csv.writer(csvfile)
            #writer.writerow(data)
            #csvfile.close()

