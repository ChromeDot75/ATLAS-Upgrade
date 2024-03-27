import uproot 
import os



general_path1 = r"N:\CERN\W3_Run_63\data\strun63_"
file_number = 10  # Change this to the specific file number you want to process

file_path = f"{general_path1}{file_number}.root"
print("File path:", file_path)

uproot_obj = uproot.open(file_path)

charge = uproot_obj['configuration/module_0/chip_4/Calibration voltage']
print("Charge:", charge)
"""
general_path = r"N:\CERN\W3_Run_63\data\strun63_"

start, end = 4, 18

files = [f"{general_path}{i}.root" for i in range(start, end)]
print(files)
#print(files)

uproot_objects = {}  



for i, files in enumerate(files):
    key = f"fh{i+1}"
    uproot_objects[key] = uproot.open(files)

#print(uproot_objects.items())

charges = {key: uproot_obj['configuration/module_0/chip_4/Calibration voltage'] 
           for key, uproot_obj in uproot_objects.items()}

print(charges.items())
for key, charge in charges.items():
    print(f"{key}: {charge}, ", end='')
    
    

>    if (qCentre == 1.0) {
>      charges[0] = 0.4993;
>      charges[1] = 0.998;
>      charges[2] = 1.4969;
> 
>      chargesInDAC[0] = 22;
>      chargesInDAC[1] = 48;
>      chargesInDAC[2] = 74;
>    } else if (qCentre == 2.0) {
>      charges[0] = 0.998;
>      charges[1] = 1.996;
>      charges[2] = 2.993;
> 
>      chargesInDAC[0] = 48;
>      chargesInDAC[1] = 100;
>      chargesInDAC[2] = 152;


   Float_t chargesInDAC[10] =
     {6, 22, 38, 48, 62,
      74, 100, 152, 204, 308};
   Float_t charges[10] =
     {0.192, 0.4993, 0.806, 0.998, 1.267,
      1.4969, 1.996, 2.993, 3.991, 5.985};
      

   Float_t charges[12] =
{0.749,0.998,1.248,1.497,1.746,1.996,2.993,4.010,5.007,6.004,7.999,9.897};
   Float_t chargesInDAC[12] = {   35,   48,   61,   74,   87,  100, 
152,  205,  258,  309,  413,  511};



"""