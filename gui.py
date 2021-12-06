import tkinter as gui
import os

def hd():
    link = 'localhost:9870' if local else ''

def sp():
    link = 'localhost:8080' if local else ''

def jp():
    link = 'localhost:8888' if local else ''

def sn():
    link = 'localhost:9000' if local else ''
    
def main():
    global local 
    
    if len(sys.argv) > 1:
        local = sys.argv[1].lower() == 'true'
        
    view = gui.Tk()
    view.title('CloudProj')
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
