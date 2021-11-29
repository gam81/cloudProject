import tkinter as gui
import os

def hd():
    link = 'localhost:9870' if local else '35.223.112.91:9870'

def sp():
    link = 'localhost:8080' if local else '34.132.29.196:8080'

def jp():
    link = 'localhost:8888' if local else '34.136.84.126:8888'

def sn():
    link = 'localhost:9000' if local else '104.197.67.245:9000'
    
def main():
    global local 
    
    if len(sys.argv) > 1:
        local = sys.argv[1].lower() == 'true'
        
    view = gui.Tk()
    view.title('Cloud Project')
    view.geometry('720x360')
    
    hadoop_button = gui.Button(view, text='Apache Hadoop', command=hd)
    hadoop_button.pack(side='top')
    
    sonar_button = gui.Button(view, text='SonarQube and SonarScanner', command=sn)
    sonar_button.pack(side='right')
    
    spark_button = gui.Button(view, text='Apache Spark', command=sp)
    spark_button.pack(side='left')

    jupyter_button = gui.Button(view, text='Jupyter Notebook', command=jp)
    jupyter_button.pack(side='bottom')

    view.mainloop()

if __name__ == '__main__':
    main()
