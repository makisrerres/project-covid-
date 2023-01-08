import tkinter as tk
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
import Colors
import os

global cases,deaths,vac
cases=True
deaths=False
vac=False
# app = tk.Tk()
#plt.style.use('seaborn')
def plot(app=None,n=1,val=[],a=True,b=False,c=False,d=False,data1=None,data2=None,data3=None,data4=None,data5=None,data6=None, dark='#000000', light='#ffffff'):
    # print('d=',d)
    global App
    App=app

    color_light = light
    color_dark = dark

    #creation of figure
    plot1= plt.Figure(figsize=(12,7), dpi=100, facecolor=color_dark, edgecolor=color_light)
    plt.rcParams['axes.facecolor'] = color_dark
    plt.rcParams['axes.edgecolor'] = color_light
    line1= FigureCanvasTkAgg(plot1, app)
    line1.get_tk_widget().grid(row=1,column=0,columnspan=2, padx=10, pady= 10, sticky='n')
    ax1= plt.Figure.add_axes(plot1,rect=[0.1,0.16,.8,.8]) #ratio of plot window
    ax2 = ax1.twinx() #creating twin axis
    ax1.ticklabel_format(style='plain')
    ax2.ticklabel_format(style='plain')
    ax1.grid(axis='both',lw=1, linestyle=':', color=color_light) #set main grid
    ax1.set_ylabel('Θάνατοι', size='14', color = color_light) #set main y label

    #set line colors
    color1 = '#1f72ac'
    color2 = '#fd7e0e'
    color3 = '#3fa43d'
    color4 = 'blue'
    color5 = 'red'
    color6 = 'green'

    #set which plots are shown
    if a:
        df1 = data1
        df11={}
        df11['Data']=df1['Data'][val[0]:val[1]] #show data based on user's selection
        df11['Dates']=df1['Dates'][val[0]:val[1]] #show dates based on user's selection
        df11=pd.DataFrame(df11)
        df11=df11[['Data','Dates']].groupby('Dates').sum()
        df11.plot(kind='line',color=color1, ls='-', ax=ax2, legend=False,label='Cases') #plot

    if b:
        df2 = data2
        df22={}
        df22['Data']=df2['Data'][val[0]:val[1]]
        df22['Dates']=df2['Dates'][val[0]:val[1]]
        df22=pd.DataFrame(df22)
        df22=df22[['Data','Dates']].groupby('Dates').sum()
        df22.plot(kind='line',color=color2, ls='-', ax=ax1, legend=False,label='Deaths')

    if c and not data3.empty:
        df3 = data3
        df33={}
        df33['Data']=df3['Data'][val[0]:val[1]]
        df33['Dates']=df3['Dates'][val[0]:val[1]]
        df33=pd.DataFrame(df33)
        df33=df33[['Data','Dates']].groupby('Dates').sum()
        df33.plot(kind='line',color=color3, ls='-', ax=ax2, legend=False,label='Vac/tions')
    
    ax2.grid(axis='both',lw=.5, linestyle=':', color='#3fa43d') #set secondary grid
    ax2.set_ylabel('Κρούσματα, Εμβολιασμοί', size='14', color = color_light)
    
    if not c and a:
        ax2.set_ylabel('Κρούσματα', size='14', color = color_light)
    
    elif not a and c:
        ax2.set_ylabel('Εμβολιασμοί', size='14', color = color_light)

    if d:
        if a:
            df4 = data4
            df44={}
            df44['Data']=df4['Data'][val[0]:val[1]]
            df44['Dates']=df4['Dates'][val[0]:val[1]]
            df44=pd.DataFrame(df44)
            df44=df44[['Data','Dates']].groupby('Dates').sum()
            df44.plot(kind='line',color=color1, ls='--', ax=ax2, legend=False,label='Cases')

        if b:
            df5 = data5
            df55={}
            df55['Data']=df5['Data'][val[0]:val[1]]
            df55['Dates']=df5['Dates'][val[0]:val[1]]
            df55=pd.DataFrame(df55)
            df55=df55[['Data','Dates']].groupby('Dates').sum()
            df55.plot(kind='line',color=color2, ls='--', ax=ax1, legend=False,label='Deaths')

        if c and not data6.empty:
            df6 = data6
            df66={}
            df66['Data']=df6['Data'][val[0]:val[1]]
            df66['Dates']=df6['Dates'][val[0]:val[1]]
            df66=pd.DataFrame(df66)
            df66=df66[['Data','Dates']].groupby('Dates').sum()
            df66.plot(kind='line',color=color3, ls='--', ax=ax2, legend=False,label='Vac/tions')
    
            #set secondary y label
        if data3.empty and data6.empty: 
            ax2.set_yticks([])
            ax2.set_subtitle('Vaccination Data N/A', size='14', color = color_light)
            if a:
                ax2.set_ylabel('Κρούσματα', size='14', color = color_light)

        elif not data3.empty and data6.empty:
            ax2.set_ylabel('Vaccination Data N/A for Country 2', size='14', color = color_light)
            ax2.grid(axis='both',lw=.5, linestyle=':', color='#3fa43d')

        elif data3.empty and not data6.empty: 
            ax2.set_yticks([])
            ax2.set_subtitle('Vaccination Data N/A for Country 1', size='14', color = color_light)
            ax2.grid(axis='both',lw=.5, linestyle=':', color='#3fa43d')

        else:
            ax2.set_ylabel('Εμβολιασμοί', size='14', color = color_light)
            ax2.grid(axis='both',lw=.5, linestyle=':', color='#3fa43d')
            if a:
                ax2.set_ylabel('Κρούσματα, Εμβολιασμοί', size='14', color = color_light)
    
    #changing tick, label colors and styles
    ax1.tick_params(color=color_light)
    ax2.tick_params(color=color_light)

    for label in ax1.yaxis.get_ticklabels():
        label.set_color(color_light)
    
    for label in ax2.yaxis.get_ticklabels():
        label.set_color(color_light)

    labels = ax1.get_xticklabels()
    for label in labels:
        label.set_rotation(45) #x label rotation

    label= ax1.get_xticks()
    for label in labels:
        label.set_color(color_light)

    ax1.autoscale(enable=None, axis="y", tight=True)
    ax1.margins(y=.5)
    ax1.set_ylim(bottom=0)
    ax2.autoscale(enable=None, axis="y", tight=True)
    ax2.margins(y=.2)
    ax2.set_ylim(bottom=0)
    ax1.xaxis.label.set_text(' ') #delete x labe
    ax1.grid(axis='both',lw=1, linestyle=':', color=color_light) #set main gridl

def plot2(app=None,val=[],data=None,txt=None,light='#ffffff',dark='#000000'):
    # print('d=',d)
    global App
    App=app

    color_light = light
    color_dark = dark

    #creation of figure
    plot1= plt.Figure(figsize=(12,7), dpi=100, facecolor=color_dark, edgecolor=color_light)
    plt.rcParams['axes.facecolor'] = color_dark
    plt.rcParams['axes.edgecolor'] = color_light
    line1= FigureCanvasTkAgg(plot1, app)
    line1.get_tk_widget().grid(row=1,column=0,columnspan=2, padx=10, pady= 10, sticky='n')
    ax1= plt.Figure.add_axes(plot1,rect=[0.1,0.16,.8,.8]) #ratio of plot window
    ax1.ticklabel_format(style='plain')
    ax1.grid(axis='both',lw=1, linestyle=':', color=color_light) #set main grid
    ax1.set_title('Ημερήσια '+txt, size='14', color = color_light) #set main y label

    #set line colors
    if txt=='Κρούσματα':
        color1 = '#1f72ac'
        ax1.set_title('Ημερήσια Κρούσματα', size='14', color = color_light) #set main y label
    elif txt=='Θάνατοι':
        color1 = '#fd7e0e'
        ax1.set_title('Ημερήσιοι Θάνατοι', size='14', color = color_light) #set main y label
    elif txt=='Εμβολιασμοί':
        color1 = '#3fa43d'
        ax1.set_title('Ημερήσιοι Εμβολιασμοί', size='14', color = color_light) #set main y label

    df1 = data
    df11={}
    df11['Data']=df1['Data'][val[0]:val[1]] #show data based on user's selection
    df11['Dates']=df1['Dates'][val[0]:val[1]] #show dates based on user's selection
    df11=pd.DataFrame(df11)
    df11=df11[['Data','Dates']].groupby('Dates').sum()
    df11.plot(kind='area',color=color1, ax=ax1, legend=False,label='Cases') #plot

    ax1.autoscale(enable=None, axis="x", tight=True)
    ax1.margins(y=.3)
    ax1.set_ylim(bottom=0)

    #changing tick, label colors and styles
    ax1.tick_params(color=color_light)

    for label in ax1.yaxis.get_ticklabels():
        label.set_color(color_light)

    labels = ax1.get_xticklabels()
    for label in labels:
        label.set_rotation(45) #x label rotation

    label= ax1.get_xticks()
    for label in labels:
        label.set_color(color_light)

    ax1.xaxis.label.set_text(' ') #delete x labe
    ax1.grid(axis='both',lw=1, linestyle=':', color=color_light) #set main gridl
