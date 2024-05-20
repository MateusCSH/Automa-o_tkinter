import pandas as pd
from tkinter import *
from tkinter import filedialog
import customtkinter as ctk
import pyautogui
import time
import subprocess
from Newprecess_func import func_mes
from Newprecess_mes import selec_mes
from Newprocess_redutor import reduzir
import cv2


ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')


class ap(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.apparence()


    def layout_config(self):
        self.title('Automação CEM')
        self.geometry('300x300')
        self.maxsize(width=400,height=400)
        self.minsize(width=250, height=250)
        
        #self.resizable(width=False, height=False)



    def apparence(self):

        pyautogui.PAUSE = 1.5
        

        

        def M4S3():   
               
            
            link = 'https://docs.google.com/spreadsheets/d/1CiRe1cbT6MVjp5j_v2S3-EYvZNLTyFWjKBua9DCx3xc/edit#gid=1410983719'

            subprocess.run(r'C:\Users\Olá\AppData\Local\Programs\Opera\opera.exe')

            time.sleep(2)

            pyautogui.write(link)

            pyautogui.press('enter')  

            filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
            
            if filepath:
                df = pd.read_csv(filepath, header=None, sep=',').drop(0).drop(columns=0)
                df.columns = ['Nome','Horas','Motivo']
                #print(df.head())                  
                time.sleep(2)

                #click_mes = pyautogui.locateCenterOnScreen('select_mês.png')
                #pyautogui.click(click_mes.x, click_mes.y)
                pyautogui.click(x=75, y=706)
                pyautogui.click(x=75, y=706)
                func_mes(2)
                pyautogui.press('enter')
                
                
                selec_mes(2)
                pyautogui.press('enter')

                click_nome = pyautogui.locateCenterOnScreen('quatro.png')
                pyautogui.click(click_nome.x, click_nome.y)  
                pyautogui.press('down')

                pyautogui.PAUSE = 0.3

                for lime in df.index:
                    nome = df.loc[lime, 'Nome']
                    pyautogui.write(nome)
                    pyautogui.press('down')

                pyautogui.scroll(1000)

                pyautogui.click(click_nome.x, click_nome.y)
                pyautogui.press('down')
                func_mes(1)
                

                for lh in df.index:
                    horas = df.loc[lh, 'Horas']
                    pyautogui.write(horas)
                    pyautogui.press('down')

                pyautogui.scroll(1000)
                pyautogui.click(click_nome.x, click_nome.y)

                pyautogui.press('down')
                func_mes(2)
                

                for limot in df.index:
                    motivo = df.loc[limot, 'Motivo']
                    pyautogui.write(motivo)
                    pyautogui.press('down')
        ###################################
        ####### FIM MÊS X #################

        
        def M5S2():
            link = 'https://docs.google.com/spreadsheets/d/1CiRe1cbT6MVjp5j_v2S3-EYvZNLTyFWjKBua9DCx3xc/edit#gid=1410983719'
            subprocess.run(r'C:\Users\Olá\AppData\Local\Programs\Opera\opera.exe')

            time.sleep(2)
            pyautogui.write(link)
            pyautogui.press('enter')

            filepath = filedialog.askopenfilename(filetypes=[('CSV files','*.csv')])

            if filepath:
                df = pd.read_csv(filepath, header=None).drop(0).drop(columns=0)
                df.columns = ['Nome','Horas','Motivo']
                
                pyautogui.click(x=75, y=706)
                pyautogui.click(x=75, y=706)                

                func_mes(2)
                pyautogui.press('enter')
                selec_mes(5)
                pyautogui.press('enter')

                click_nome = pyautogui.locateCenterOnScreen('quatro.png')
                pyautogui.click(click_nome.x, click_nome.y)

                pyautogui.press('down')
                pyautogui.PAUSE = 0.3
                for lime in df.index:
                    nome = df.loc[lime,'Nome']
                    pyautogui.write(nome)
                    pyautogui.press('down')

        def M4S1():
                
                df = reduzir()
                
                click_nome = pyautogui.locateCenterOnScreen('quatro.png', confidence=0.7)
                pyautogui.click(click_nome.x, click_nome.y)

                pyautogui.PAUSE = 0.3
                pyautogui.press('down')
                
                for name in df.index:
                    nome = df.loc[name, 'Nome']
                    pyautogui.write(nome)
                    pyautogui.press('down') 

                pyautogui.scroll(500)
                time.sleep(1.5)

                pyautogui.click(click_nome.x, click_nome.y)
                pyautogui.press('down')
                func_mes(1)
                

                for hor in df.index:
                    horas = df.loc[hor, 'Horas']
                    pyautogui.write(horas)
                    pyautogui.press('down')

                pyautogui.scroll(500)
                time.sleep(1.5)
                
                pyautogui.click(click_nome.x, click_nome.y)
                pyautogui.press('down')
                func_mes(2)
                
                for mt in df.index:
                    motivo = df.loc[mt,'Motivo']
                    pyautogui.write(motivo)
                    pyautogui.press('down')                
                

           




        btn_M4S3 = ctk.CTkButton(self, text='ABRIL - semana (3)',command=M4S3)
        btn_M4S3.place(x=75,y=125)

        btn_M5S2 = ctk.CTkButton(self, text='MAIO - Semana (2)', fg_color='#0bba9d',text_color='black', command=M5S2)
        btn_M5S2.place(x=75, y=160)

        btn_M4S1 = ctk.CTkButton(self, text='ABRIL - S(2)', command=M4S1)
        btn_M4S1.place(x=75, y=195)




if __name__=='__main__':
    Acess_Drive_copy2 = ap()
    Acess_Drive_copy2.mainloop()