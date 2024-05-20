import pandas as pd
import pyautogui as py
import subprocess
from tkinter import filedialog
import time


def reduzir():
        
        link = 'https://docs.google.com/spreadsheets/d/1CiRe1cbT6MVjp5j_v2S3-EYvZNLTyFWjKBua9DCx3xc/edit#gid=1410983719'
        subprocess.run(r'C:\Users\Olá\AppData\Local\Programs\Opera\opera.exe')

        time.sleep(2)
        py.write(link)
        py.press('enter')

        filepath = filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])

        if filepath:
            df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
            df.columns = ['Nome','Horas','Motivo']

            time.sleep(2)        
            py.click(x=75, y=706)
            py.click(x=75, y=706)    

            return df            
            