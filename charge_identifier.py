import uproot 
import os

fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_4.root")

fh2 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_5.root")

fh3 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_6.root")

fh4 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_7.root")

fh5 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_8.root")

fh6 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_9.root")

fh7 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_10.root")

fh8 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_11.root")

fh9 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_12.root")

fh10 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_13.root")

fh11 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_14.root")

fh12 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_15.root")

fh13 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_16.root")

fh14 = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_17.root")
"""
folder_path = r"N:\CERN\W3_Run_63\data"

prefix = 'strun63_'
files = os.listdir(folder_path)
files_filtered = [file for file in files if file.startswith(prefix) and file.endswith('.root')]

threshold_start = files_filtered.index('strun63_4')

for file in files_filtered[threshold_start:]: 
    file_path = os.path.join(folder_path, file)
    with uproot.open(file_path) as fh: 
        charge_m0 = fh['configuration/module_0/chip_4/Calibration voltage']
        charge_m1 = fh['configuration/module_1/chip_4/Calibration voltage']
        
        print(f"Processing file: {file_path}")
        print(f"Charge data: {charge_m0}")
        print(f"Charge data: {charge_m1}")
        

"""

#different_charges = []
#fh = uproot.open(r"N:\CERN\W3_Run_63\data\strun63_4.root") 



#int(float)

#strun63_4
charge = fh['configuration/module_0/chip_4/Calibration voltage']

charge2 = fh2['configuration/module_0/chip_4/Calibration voltage']


charge3 = fh3['configuration/module_0/chip_4/Calibration voltage']

charge4 = fh4['configuration/module_0/chip_4/Calibration voltage']


charge5 = fh5['configuration/module_0/chip_4/Calibration voltage']
charge6 = fh6['configuration/module_1/chip_4/Calibration voltage']

charge7 = fh7['configuration/module_1/chip_4/Calibration voltage']

charge8 = fh8['configuration/module_1/chip_4/Calibration voltage']

charge9 = fh9['configuration/module_1/chip_4/Calibration voltage']

charge10 = fh10['configuration/module_1/chip_4/Calibration voltage']

charge11 = fh11['configuration/module_1/chip_4/Calibration voltage']

charge12 = fh12['configuration/module_1/chip_4/Calibration voltage']

charge13 = fh13['configuration/module_1/chip_4/Calibration voltage']

charge14 = fh14['configuration/module_1/chip_4/Calibration voltage']





print(charge, charge2, charge3, charge4, charge5, charge6, charge7, charge8, charge9, charge10, charge11, charge12, charge13, charge14)


#strun63_5



"""
print(fh)

print(fh.keys(recursive=False))


print(charge)"""