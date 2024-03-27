import json
class JsonData:
    def __init__(self, json_FP):
        with open(json_FP) as file:
            data = json.load(file)
            self.results = data.get('results', {})
  
json_data = JsonData("N:\\CERN\\W3_Run_63\\results\\SN20USBHX2001092_20231009_63_4_RESPONSE_CURVE_PPA.json")

keys_extract = {'gain_away': 'gain away AR', 'gain_mean_away': 'gain_mean_away_AR',
                'gain_mean_under': 'gain_mean_under_AR', 'gain_rms_away': 'gain_rms_away_AR',
                 'gain_rms_under': 'gain_rms_under-AR', 'gain_under':'gain_under_AR' }

keys_extract_2 = {'innse_away':'innse_away_AR', 'innse_mean_away': 'innse_mean_away_AR', 
                  'innse_mean_under':'innse_mean_under_AR', 'innse_rms_away':'innse_rms_away_AR',
                  'innse_rms_under':'innse_rms_under_AR', 'innse_under':'innse_under_AR'}

# innse = input noise

keys_extract_3 = {'offset_mean_away':'offset_mean_away_AR', 'offset_rms_away':'offset_rms_away_AR',
                  'offset_rms_under': 'offset_rms_under_AR', 'offset_mean_under':'offset_mean_under_AR'}

keys_extract_4 = {'outnse_away':'outnse_away_AR', 'outnse_under':'outnse_under_AR'}
# outnse = output noise
#find the difference between the 2. 
keys_extract_5 = {'rc_fit_away':'rc_fit_away_AR','rc_fit_under':'rc_fit_under_AR'}

keys_extract_6 = {'vt50_away': 'vt50 away AR', 'vt50_away': 'vt50_away_AR',
                'vt50_under': 'vt50_mean_under_AR', 'vt50_rms_away': 'vt50_rms_away_AR',
                 'vt50_rms_under': 'vt50_rms_under-AR', 'vt50_under':'vt50_under_AR' }


extracted_arrays ={}
"""
for key, array_name in keys_extract.items():
    array = json_data.get_array(key)
    extracted_arrays[array_name] = array 

"""