import tkinter as gui

def main():
    window = gui.Tk()
    window.title('Cloud Project')
    window.geometry('720x360')

    hadoop_button = gui.Button(window, text='Apache Hadoop', command=hd)
    hadoop_button.pack(side='top')

    spark_button = gui.Button(window, text='Apache Spark', command=sp)
    spark_button.pack(side='left')

    jupyter_button = gui.Button(window, text='Jupyter Notebook', command=jp)
    jupyter_button.pack(side='bottom')

    sonar_button = gui.Button(window, text='SonarQube and SonarScanner', command=sn)
    sonar_button.pack(side='right')

    window.mainloop()

def hd():
    pass

def sp():
    pass

def jp():
    pass

def sn():
    pass

if __name__ == '__main__':
    main()