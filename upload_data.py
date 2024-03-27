from flask import Flask, request, render_template
import os
import dash 
from dash import doc, html 
from dash.dependencies import Input, Output, State 
import schedule 
import time

Upload_Directory = "Uploads"

if not os.path.exists(Upload_Directory): 
    os.makedirs(Upload_Directory)
    
app = dash.Dash(__name__)

app.layout = html.Div([html.Div(id="data-upload-output")])

def saving_files(name, run):
    data = run.encode("utf8").split(b";base64, ")[1]
    with open(os.path.join(Upload_Directory, name), "wb") as  new_data:
        new_data.write(data)


def uploaded_files(): 
    files = [] 
    for filename in os.listdir(Upload_Directory):
        path = os.path.join(Upload_Directory, filename)
        if os.path.isfile(path):
            files.append(filename)
    
    return files

def update_to_directory(): 
    print("Checking for new files added inside directory...")
    
    files = uploaded_files()
    if len(files) > 0:
        print("The following new folders are found:", files)
    else:
        print("No new files are in directory")
        

duration_of_scan = 0 

schedule.every(duration_of_scan).minutes.do(update_to_directory)


# scan directory change to data. 
"""
@app.callback(
    Output("data-upload-output", "children"),
    
    [Input("data-upload-output", "children")]
 

def update_output(_): 
    
    return html.Div("Directory last time searched: {}.format(time.strftime("%Y-%m-%d %H:%M:%S")))

if __name__ == "__main__":

    while True: 
        schedule.run.pending()
        time.sleep(1)


    
"""
