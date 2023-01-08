import customtkinter 
import tkinter as tk
import Colors
from os import *
from PlotV2 import *
from RangeSlider.RangeSlider import RangeSliderH
from data_fetchV2 import *
from newdatabase import *
from datetime import date, timedelta


class Covid(customtkinter.CTk):

    dateStart=0
    dateEnd=dur()
    graph_dates = [dateStart,dateEnd]

    def __init__(self):

        self.lbStart=date(int(get_first_date('Cases')[0]),int(get_first_date('Cases')[1]),int(get_first_date('Cases')[2])).strftime("%Y/%m/%d")
        self.lbEnd=(date(int(get_first_date('Cases')[0]),int(get_first_date('Cases')[1]),int(get_first_date('Cases')[2]))+timedelta(dur())).strftime("%Y/%m/%d")

        super().__init__()

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10), weight=1)
        
        self.loading=customtkinter.CTkLabel(self, text='Loading.Please Wait...')
        self.loading.grid(row=1,column=0,columnspan=2, padx=20, pady=(20, 10))
        self.update()

        database()

        #Frame
        n=2
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=11, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(0, weight=0)        
        Colors.colors(customtkinter.get_appearance_mode().capitalize())

        #Frame 2
        self.sidebar_frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame2.grid(row=0, column=4, rowspan=20, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure(16, weight=1)

        #Switches
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="ΜΕΝΟΥ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, rowspan=1, padx=20, pady=(20, 10))

        customtkinter.CTkLabel(self.sidebar_frame, text=" ").grid(row=n+1, column=0, padx=20, pady=(20, 10))    #}=>spacers
        customtkinter.CTkLabel(self.sidebar_frame, text=" ").grid(row=n, column=0, padx=20, pady=(20, 10))      #}
        
        self.vac_val = False    #}
        self.cases_val = True   #} => Starting values for switches
        self.deaths_val = False #}
        self.daily_val = False  #}

        self.cases = customtkinter.CTkSwitch(master=self.sidebar_frame,text='Κρούσματα',text_color='#1f72ac', command=self.cases_pressed)
        self.cases.grid(row=n+2, column=0, padx=20, pady=10, sticky='sw')
        self.cases.select()
        self.deaths= customtkinter.CTkSwitch(master=self.sidebar_frame,text='Θάνατοι',text_color='#fd7e0e', command=self.deaths_pressed)
        self.deaths.grid(row=n+3, column=0, padx=20, pady=10, sticky="sw")
        self.vaccinations = customtkinter.CTkSwitch(master=self.sidebar_frame, text='Εμβολιασμοί', text_color='#3fa43d', command=self.vaccinations_pressed)
        self.vaccinations.grid(row=n+4, column=0, padx=20, pady=10, sticky="sw")
        self.daily= customtkinter.CTkSwitch(master=self.sidebar_frame,text='Ημερησίως', command=self.daily_pressed)
        self.daily.grid(row=n+5, column=0, padx=20, pady=10, sticky="sw")        
        
        #Appearance Mode And Scaling
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame2, text="Appearance Mode:", anchor="w")#light,dark mode
        self.appearance_mode_label.grid(row=17, column=0, padx=20, pady=(10, 10))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame2, values=["Dark", "Light", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=18, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame2, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=19, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame2, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=20, column=0, padx=20, pady=(10, 20))
        self.scaling_optionemenu.set("100%")

        #δημιουργία πίνακα
        self.pinakas_frame=customtkinter.CTkFrame(self,width=400,height=200)
        self.pinakas_frame.grid(row=1,column=1,columnspan=2, rowspan=11,padx=10,pady=10, sticky="nesw")
        
        #Refresh button
        self.button=customtkinter.CTkButton(self.pinakas_frame, text='Refresh', width=70, height=50, command=self.refresh)
        self.button.grid(row=6, column=0, rowspan=2, columnspan=2, padx= 20, pady = 10, sticky='e')
        self.lbStart=customtkinter.CTkLabel(self.pinakas_frame, text='Αρχή: '+self.slider_time(self.dateStart))
        self.lbStart.grid(row=6, column=0)
        self.lbEnd=customtkinter.CTkLabel(self.pinakas_frame, text='Τέλος: '+self.slider_time(self.dateEnd))
        self.lbEnd.grid(row=6, column=1)

        #Dropdown Menus
        self.variable1=tk.StringVar(self)
        self.variable1.set('Greece')
        self.variable2=tk.StringVar(self)
        self.variable2.set('None')
        self.xwra1 = customtkinter.CTkOptionMenu(self,variable=self.variable1,values=country1(),command=self.country1)
        self.xwra1.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nw")
        self.xwra2 = customtkinter.CTkOptionMenu(self,variable=self.variable2,values=country2(),command=self.country2)
        self.xwra2.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="ne")
        self.country1()

        self.title('ΕΙΚΟΝΟΠΟΙΗΣΗ ΤΗΣ ΕΞΕΛΙΞΕΩΣ ΤΟΥ ΚΟΒΙΝΤ')
        
        self.slider(app=self.pinakas_frame, max=dur(), dark=Colors.colors.frame_color, light=Colors.colors.text_color, unselected=Colors.colors.unselected_color, accent=Colors.colors.main_accent_color)
        
        self.loading.destroy()      

        self.deiconify()    #show window again


    def slider(self, app, dark, light, unselected, max, accent):     #Double slider date picker  
        self.hVar1 = tk.DoubleVar(value=self.dateStart)              #left handle variable
        self.hVar2 = tk.DoubleVar(value=self.dateEnd)                #right handle variable
        rs1 = RangeSliderH( app , [self.hVar1, self.hVar2] , padX=30,show_value=False, bgColor=dark , max_val=max , bar_color_inner= accent , bar_color_outer= accent , line_s_color= light , line_color= unselected)   #horizontal
        rs1.grid(row=7, column=0, columnspan=2, padx= 20, pady = 10) # or grid or place method could be used
        self.hVar1.trace_add('write', self.doSomething)              #}
        self.hVar2.trace_add('write', self.doSomething)              #}=>call doSomething when Slider changes


    def country1(self, *args):
        n = self.xwra1.get()
        customtkinter.CTkLabel(self.pinakas_frame, text='Loading.Please Wait...').grid(row=1,column=0,columnspan=2, padx=20, pady=(20, 10))
        Covid.update(self)
        self.variable1=n
        #creating dataframes for country 1
        self.df1=self.dates(country=n,table='Cases')
        self.df1=pd.DataFrame(self.df1)
        self.df2=self.dates(country=n,table='Deaths')
        self.df2=pd.DataFrame(self.df2)
        self.df3=self.dates(country=n,table='Vaccinations')
        self.df3=pd.DataFrame(self.df3)
        self.df7=self.dates(country=n,table='Cases',daily=True)
        self.df7=pd.DataFrame(self.df7)
        self.df8=self.dates(country=n,table='Deaths',daily=True)
        self.df8=pd.DataFrame(self.df8)
        self.df9=self.dates(country=n,table='Vaccinations',daily=True)
        self.df9=pd.DataFrame(self.df9)
        self.country3()
        return n


    def labels(self, n=0):
        #Destroy all labels in frame 2
        try:
            self.lb1.destroy()
        except: pass
        try:
            self.lb2.destroy()
        except: pass
        try:
            self.lb3.destroy()
        except: pass
        try:
            self.lb4.destroy()
        except: pass
        try:
            self.lb5.destroy()
        except: pass
        try:
            self.lb6.destroy()
        except: pass
        try:
            self.lb7.destroy()
        except: pass
        try:
            self.lb8.destroy()
        except: pass
        try:
            self.lb9.destroy()
        except: pass
        try:
            self.lb10.destroy()
        except: pass
        try:
            self.lb11.destroy()
        except: pass
        try:
            self.lb12.destroy()
        except: pass
        try:
            self.lb13.destroy()
        except: pass
        try:
            self.lb14.destroy()
        except: pass

        #create labels for frame 2    
        if self.daily_val==False:
            self.lb1=customtkinter.CTkLabel(self.sidebar_frame2, font=customtkinter.CTkFont(size=20, weight="bold"), text=self.xwra1.get()+' Data')
            self.lb1.grid(row=0, column=0, padx=20, pady=(20, 10))
            n=0
            self.lb2=customtkinter.CTkLabel(self.sidebar_frame2, text="Κρούσματα (Μέγιστο)")
            self.lb2.grid(row=n+1, column=0, padx=20, pady=(0,0))
            self.lb3=customtkinter.CTkLabel(self.sidebar_frame2, text=list(self.df1['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])[-1])
            self.lb3.grid(row=n+2, column=0, padx=20, pady=(0,0))
            n+=2
            self.lb4=customtkinter.CTkLabel(self.sidebar_frame2, text="Θάνατοι (Μέγιστο)")
            self.lb4.grid(row=n+1, column=0, padx=20, pady=(0,0))
            self.lb5=customtkinter.CTkLabel(self.sidebar_frame2, text=list(self.df2['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])[-1])
            self.lb5.grid(row=n+2, column=0, padx=20, pady=(0,0))
            n+=2
            self.lb6=customtkinter.CTkLabel(self.sidebar_frame2, text="Εμβλιασμοί (Μέγιστο)")
            self.lb6.grid(row=n+1, column=0, padx=20, pady=(0,0))
            if not self.df3.empty:
                self.lb7=customtkinter.CTkLabel(self.sidebar_frame2, text=list(self.df3['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])[-1])
                self.lb7.grid(row=n+2, column=0, padx=20, pady=(0,0))
            else:
                self.lb7=customtkinter.CTkLabel(self.sidebar_frame2, text='N/A')
                self.lb7.grid(row=n+3, column=0, padx=20, pady=(0,0))
            n+=2

            if self.xwra2.get()!='None':
                self.lb8=customtkinter.CTkLabel(self.sidebar_frame2, font=customtkinter.CTkFont(size=20, weight="bold"), text=self.xwra2.get()+' Data')
                self.lb8.grid(row=n+1, column=0, padx=20, pady=(10,20))
                n+=1
                self.lb9=customtkinter.CTkLabel(self.sidebar_frame2, text="Κρούσματα (Μέγιστο)")
                self.lb9.grid(row=n+2, column=0, padx=20, pady=(0,0))
                self.lb10=customtkinter.CTkLabel(self.sidebar_frame2, text=list(self.df4['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])[-1])
                self.lb10.grid(row=n+3, column=0, padx=20, pady=(0,0))
                n+=3
                self.lb11=customtkinter.CTkLabel(self.sidebar_frame2, text="Θάνατοι (Μέγιστο)")
                self.lb11.grid(row=n+1, column=0, padx=20, pady=(0,0))
                self.lb12=customtkinter.CTkLabel(self.sidebar_frame2, text=list(self.df5['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])[-1])
                self.lb12.grid(row=n+2, column=0, padx=20, pady=(0,0))
                n+=2
                self.lb13=customtkinter.CTkLabel(self.sidebar_frame2, text="Εμβλιασμοί (Μέγιστο)")
                self.lb13.grid(row=n+1, column=0, padx=20, pady=(0,0))
                if not self.df3.empty:
                    self.lb14=customtkinter.CTkLabel(self.sidebar_frame2, text=list(self.df6['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])[-1])
                    self.lb14.grid(row=n+2, column=0, padx=20, pady=(0,0))
                else:
                    self.lb14=customtkinter.CTkLabel(self.sidebar_frame2, text='N/A')
                    self.lb14.grid(row=n+2, column=0, padx=20, pady=(0,0))
        else:
            self.lb1=customtkinter.CTkLabel(self.sidebar_frame2, font=customtkinter.CTkFont(size=20, weight="bold"), text=self.xwra1.get()+' Data')
            self.lb1.grid(row=0, column=0, padx=20, pady=(20, 10))
            n=0
            self.lb2=customtkinter.CTkLabel(self.sidebar_frame2, text="Κρούσματα (Μέγιστο)")
            self.lb2.grid(row=n+1, column=0, padx=20, pady=(0,0))
            self.lb3=customtkinter.CTkLabel(self.sidebar_frame2, text=max(list(self.df7['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])))
            self.lb3.grid(row=n+2, column=0, padx=20, pady=(0,0))
            self.lb4=customtkinter.CTkLabel(self.sidebar_frame2, text='Ημερομηνία')
            self.lb4.grid(row=n+3, column=0, padx=20, pady=(0,0))
            self.lb5=customtkinter.CTkLabel(self.sidebar_frame2, text=self.df7['Dates'][Covid.graph_dates[0]:Covid.graph_dates[1]][list(self.df7['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]]).index(max(list(self.df7['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])))])
            self.lb5.grid(row=n+4, column=0, padx=20, pady=(0,0))
            n+=4
            self.lb6=customtkinter.CTkLabel(self.sidebar_frame2, text="Θάνατοι (Μέγιστο)")
            self.lb6.grid(row=n+1, column=0, padx=20, pady=(0,0))
            self.lb7=customtkinter.CTkLabel(self.sidebar_frame2, text=max(list(self.df8['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])))
            self.lb7.grid(row=n+2, column=0, padx=20, pady=(0,0))
            self.lb8=customtkinter.CTkLabel(self.sidebar_frame2, text='Ημερομηνία')
            self.lb8.grid(row=n+3, column=0, padx=20, pady=(0,0))
            self.lb9=customtkinter.CTkLabel(self.sidebar_frame2, text=self.df8['Dates'][Covid.graph_dates[0]:Covid.graph_dates[1]][list(self.df8['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]]).index(max(list(self.df8['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])))])
            self.lb9.grid(row=n+4, column=0, padx=20, pady=(0,0))
            n+=4
            self.lb10=customtkinter.CTkLabel(self.sidebar_frame2, text="Εμβλιασμοί (Μέγιστο)")
            self.lb10.grid(row=n+1, column=0, padx=20, pady=(0,0))
            if not self.df3.empty:
                self.lb11=customtkinter.CTkLabel(self.sidebar_frame2, text=max(list(self.df9['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])))
                self.lb11.grid(row=n+2, column=0, padx=20, pady=(0,0))
                self.lb12=customtkinter.CTkLabel(self.sidebar_frame2, text='Ημερομηνία')
                self.lb12.grid(row=n+3, column=0, padx=20, pady=(0,0))
                self.lb13=customtkinter.CTkLabel(self.sidebar_frame2, text=self.df9['Dates'][Covid.graph_dates[0]:Covid.graph_dates[1]][list(self.df9['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]]).index(max(list(self.df9['Data'][Covid.graph_dates[0]:Covid.graph_dates[1]])))])
                self.lb13.grid(row=n+4, column=0, padx=20, pady=(0,0))
            else:
                self.lb11=customtkinter.CTkLabel(self.sidebar_frame2, text='N/A')
                self.lb11.grid(row=n+3, column=0, padx=20, pady=(0,0))


    def country2(self, *args):
        n = self.xwra2.get()
        customtkinter.CTkLabel(self.pinakas_frame, text='Loading.Please Wait...').grid(row=1,column=0,columnspan=2, padx=20, pady=(20, 10))
        Covid.update(self)
        if n!='None':
            #create dataframes for country2
            self.variable2=n
            self.df4=self.dates(country=n,table='Cases')
            self.df4=pd.DataFrame(self.df4)
            self.df5=self.dates(country=n,table='Deaths')
            self.df5=pd.DataFrame(self.df5)
            self.df6=self.dates(country=n,table='Vaccinations')
            self.df6=pd.DataFrame(self.df6)
            self.country3()
        Covid.update(self)
        return n


    def country3(self):
        if True:    
            if self.xwra2.get()!='None':
                plot(app=self.pinakas_frame,val=Covid.graph_dates,a=self.cases_val, b=self.deaths_val, c=self.vac_val,d=True, data1=self.df1, data2=self.df2, data3=self.df3, data4=self.df4, data5=self.df5, data6=self.df6, dark=Colors.colors.frame_color, light=Colors.colors.text_color) #plot
                self.labels()
            else:
                plot(app=self.pinakas_frame,val=Covid.graph_dates,a=self.cases_val, b=self.deaths_val, c=self.vac_val, data1=self.df1, data2=self.df2, data3=self.df3, dark=Colors.colors.frame_color, light=Colors.colors.text_color) #plot
                self.labels()
        Covid.update(self)


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        Colors.colors(customtkinter.get_appearance_mode().capitalize())
        self.slider(app=self.pinakas_frame, max=dur(), dark=Colors.colors.frame_color, light=Colors.colors.text_color, unselected=Colors.colors.unselected_color, accent=Colors.colors.main_accent_color)
        self.refresh()


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    #Daily cases plot
    def cases_plot(self):
        plot2(app=self.pinakas_frame,val=Covid.graph_dates,data=self.df7,txt='Κρούσματα',dark=Colors.colors.frame_color, light=Colors.colors.text_color) #plot
        self.labels()
    
    #Daily deaths plot
    def deaths_plot(self):
        plot2(app=self.pinakas_frame,val=Covid.graph_dates,data=self.df8,txt='Θάνατοι',dark=Colors.colors.frame_color, light=Colors.colors.text_color) #plot
        self.labels()
    
    #Daily vaccinations plot
    def vac_plot(self):
        plot2(app=self.pinakas_frame,val=Covid.graph_dates,data=self.df9,txt='Εμβολιασμοί',dark=Colors.colors.frame_color, light=Colors.colors.text_color) #plot
        self.labels()


    def vaccinations_pressed(self):
        print('vaccinations toggled')
        if self.vac_val==True:
            self.vac_val=False
            print('OFF')
            self.country3()

        else:
            self.vac_val=True
            print('ON')
            self.country3()


    def cases_pressed(self):
        print('cases toggled')
        if self.cases_val==True:
            self.cases_val=False
            print('OFF')
            self.country3()
        else:
            self.cases_val=True
            print('ON')
            self.country3()


    def deaths_pressed(self):
        print('deaths toggled')
        if self.deaths_val==True:
            self.deaths_val=False
            print('OFF')
            self.country3()
        else:
            self.deaths_val=True
            print('ON')
            self.country3()

    #Changing menu layout for daily mode
    def daily_pressed(self):
        print('daily toggled')
        if self.daily_val==True:
            self.daily_val=False
            print('OFF')
            self.country3()
            self.cases.configure(state="enabled")
            self.deaths.configure(state="enabled")
            self.vaccinations.configure(state="enabled")
            try:
                self.cases_d.destroy()
                self.deaths_d.destroy()
                self.vac_d.destroy()
            except: pass
        else:
            self.daily_val=True
            print('ON')
            self.cases_plot()
            self.cases.configure(state="disabled")
            self.deaths.configure(state="disabled")
            self.vaccinations.configure(state="disabled")
            #Radio buttons
            self.radio_var = tk.IntVar(value=0)
            self.cases_d = customtkinter.CTkRadioButton(self.sidebar_frame,text='Κρούσματα',text_color='#1f72ac', variable=self.radio_var, value=0,command=self.cases_plot)
            self.deaths_d = customtkinter.CTkRadioButton(self.sidebar_frame,text='Θάνατοι',text_color='#fd7e0e', variable=self.radio_var, value=1,command=self.deaths_plot)
            self.vac_d = customtkinter.CTkRadioButton(self.sidebar_frame,text='Εμβολιασμοί',text_color='#3fa43d',variable=self.radio_var, value=2,command=self.vac_plot)
            self.cases_d.grid(row=2+6, column=0, pady=10, padx=20, sticky="nsw")
            self.deaths_d.grid(row=2+7, column=0, pady=10, padx=20, sticky="nsw")
            self.vac_d.grid(row=2+8, column=0, pady=10, padx=20, sticky="nsw")

    #Slider date label values
    def slider_time(self,n):
        self.time=(date(int(get_first_date('Cases')[0]),int(get_first_date('Cases')[1]),int(get_first_date('Cases')[2]))+timedelta(days=n)).strftime("%Y/%m/%d")
        return str(self.time)
    
    #get slider values
    def doSomething(self, var, index, mode):
        n=[]
        n.append(int(round (self.hVar1.get(),0)))
        n.append(int(round (self.hVar2.get(),0)))
        Covid.graph_dates = n
        try:
            self.lbStart.destroy()
            self.lbEnd.destroy()
        except: pass
        #refresh slider date labels
        self.lbStart=customtkinter.CTkLabel(self.pinakas_frame, text='Αρχή: '+self.slider_time(Covid.graph_dates[0]))
        self.lbStart.grid(row=6, column=0)
        self.lbEnd=customtkinter.CTkLabel(self.pinakas_frame, text='Τέλος: '+self.slider_time(Covid.graph_dates[1]))
        self.lbEnd.grid(row=6, column=1)
    
    #Get data (creates a dictionary with data and dates)
    def dates(self, country, table,daily=False):
        if daily==True:
            df1 = {'Data':data(country, table, dates_between([self.dateStart,self.dateEnd]),daily=daily)}
            df2 = dates_between([self.dateStart,self.dateEnd])
            df = df1
            df['Dates']=df2
            if table == 'Vaccinations' and df1['Data']==[]: df={}
        else:
            df1 = {'Data':data(country, table, dates_between([self.dateStart,self.dateEnd]))}
            df2 = dates_between([self.dateStart,self.dateEnd])
            df = df1
            df['Dates']=df2
            if table == 'Vaccinations' and df1['Data']==[]: df={}
        return df


    def refresh(self):
        if self.daily_val==False:
            self.country3()
        else:
            if self.radio_var.get()==0:
                self.cases_plot()
                print(0)
            elif self.radio_var.get()==1:
                self.deaths_plot()
                print(1)
            elif self.radio_var.get()==2:
                self.vac_plot()
                print(2)


#root=customtkinter.CTk()
if __name__ == "__main__":
    myapp=Covid()
    myapp.mainloop()