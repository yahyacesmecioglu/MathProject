#kullandıgım kutuphaneler
import matplotlib.pyplot as plt
import numpy as np


print ("1. y=ax+b")
print ("2. y=ax^2+b")
print ("3. y=sin(x)")
sec=input ("seçeneği girin: ")

print(sec)
if sec=="1" :
    a=int(input ("a girin: "))
    b=int(input ("b girin: "))
    x1=int (input ("ilk x girin: "))
    x2=int(input ("son x girin: "))

    x = np.linspace(x1, x2, 100)
    y = a*x+b
 
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y)
    plt.show()


if sec=="2" :
    a=int(input ("a girin: "))
    b=int(input ("b girin: "))
    x1=int (input ("ilk x girin: "))
    x2=int(input ("son x girin: "))

    x = np.linspace(x1, x2, 100)
    y = a*x**2+b
 
    fig = plt.figure()

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x, y)
    plt.show()

if sec=="3" :
    x = np.linspace(-np.pi,np.pi,100)
    y = np.sin(x)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.plot(x,y, 'b-')
    plt.show()
   

# Kaynak: 
# https://scriptverse.academy/tutorials/python-matplotlib-plot-sine.html
    
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org matplotlib
# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org numpy

# https://www.shellhacks.com/pip-install-ssl-error-certificate_verify_failed/

