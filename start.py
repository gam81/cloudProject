import os
def main():
    intro = """Welcome to Big Data Processing Application
    Please type the number that corresponds to which application you would like to run:
    1. Apache Hadoop
    2. Apache Spark
    3. Jupyter Notebook
    4. SonarQube and SonarScanner

    Type the number here > """

    choices = {'1':hd, '2':sp, '3':jp, '4':sn}
    run = input(intro)

    while run not in choices:
        run = input('Please enter a valid number > ')

    choices[run]()

def hd():
    

def sp():
   

def jp():
    

def sn():
    

if __name__ == '__main__':
    main()