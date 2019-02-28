
from tkinter import*
import tkinter as tk
import sqlite3
import tkinter.messagebox

class Expenditure:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('FAMILY EXPENDITURE PLANNER')
        self.root.geometry('1200x600+100+50')
        self.file1=PhotoImage(file='family.gif')
        self.file2=PhotoImage(file='planner.gif')

        Button(self.root,image=self.file2,width=350,height=200,command=self.buttonClick1,bg="black",relief="raise").place(x=300,y=200)
        Button(self.root,image=self.file1,width=350,height=200,command=self.buttonClick2,bg="black",relief="raise").place(x=700,y=200)
        label1=tk.Label(self.root,text="PLANNER",width=100,height=3).place(x=120,y=150)
        label2=tk.Label(self.root,text="CUSTOMER",width=100,height=3).place(x=520,y=150)

        self.root.mainloop()
    def insert(self):
        conn=sqlite3.connect('test.db')
        conn.execute("CREATE TABLE IF NOT EXISTS PLANNER\
                    ( Name TEXT NOT NULL, Surname TEXT NOT NULL,Contact TEXT NOT NULL,Income FLOAT,\
                    Loan FLOAT,Ideal_Loan FLOAT,Tax FLOAT,Insurance FLOAT,Ideal_Insurance FLOAT,\
                    Saving FLOAT,Ideal_Saving FLOAT,Living FLOAT,Ideal_Living FLOAT)")
                     
        conn.execute("INSERT INTO PLANNER(Name,Surname,Contact,Income,Loan,Ideal_Loan,\
Tax,Insurance,Ideal_Insurance,Saving,Ideal_Saving,Living,Ideal_Living) \
VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.name,self.surname,self.contact,self.sumincome,\
                                    self.sumloan,self.idealloan,self.sumtax,self.suminsurance,\
                                    self.idealinsurance,self.sumsaving,self.idealsaving,\
                                    self.sumliving,self.idealliving))
        conn.commit()
        conn.close()
    #----------------------------------------------------------------------------------------------------

    def buttonClick1(self):
         self.root.quit()
         self.root.destroy()
         self.planner()
    def planner(self):
         winda=tk.Tk()
         winda.title("PLANNER")
         winda.geometry('1200x600+100+50')
         winda.after(1, lambda: winda.focus_force())

         label1=tk.Label(winda,text="USER NAME",height=5,width=30).grid(row=0,column=0)
         label1=tk.Label(winda,text="PASSWORD",height=5,width=30).grid(row=1,column=0)
         self.t1=Entry(winda)
         self.t1.focus_set()
         self.t1.grid(row=0,column=1,pady=5)
         self.t2=Entry(winda,show="*")
         self.t2.grid(row=1,column=1,pady=5)
         Button(winda,text="ENTER",width=10,height=3,command=winda.quit,bg='gray').grid(row=5,column=2)
     
         winda.mainloop()
         if(self.t1.get()==("Roma" or "Richa") and self.t2.get()==("12345")):
          winda.destroy()
          frame=tk.Tk()
          frame.title("DETAILS")
          frame.geometry('1200x600+100+50')
          conn=sqlite3.connect('test.db')
          cursor=conn.execute("SELECT rowid,Name,Surname,Contact,Income,Loan,Ideal_Loan,\
Tax,Insurance,Ideal_Insurance,Saving,Ideal_Saving,Living,Ideal_Living FROM PLANNER")
          
          label14=tk.Label(frame,text="Sr.No",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=0)
          label1=tk.Label(frame,text="NAME",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=1)
          label2=tk.Label(frame,text="SURNAME",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=2)
          label3=tk.Label(frame,text="CONTACT",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=3)
          label4=tk.Label(frame,text="INCOME",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=4)
          label5=tk.Label(frame,text="LOAN",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=5)
          label6=tk.Label(frame,text="IDEAL LOAN",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=6)
          label7=tk.Label(frame,text="TAX",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=7)
          label8=tk.Label(frame,text="INSURANCE",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=8)
          label9=tk.Label(frame,text="IDEAL INSURANCE",bg='ivory1',fg='red',height=2,width=15).grid(row=0,column=9)
          label10=tk.Label(frame,text="SAVING",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=10)
          label11=tk.Label(frame,text="IDEAL SAVING",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=11)
          label10=tk.Label(frame,text="LIVING",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=12)
          label13=tk.Label(frame,text="IDEAL LIVING",bg='ivory1',fg='red',height=2,width=10).grid(row=0,column=13)
          r=1
          col=0
          for row in cursor:
            for data in row:
                
                b=Label(frame,text=data,height=1,width=10,fg='darkblue')
                b.grid(row=r,column=col)
                col=col+1
            r=r+1
            col=0
          frame.grid_propagate(0)
          conn.close()
         else:
            tk.messagebox.showinfo("ERROR!!","Incorrect username or password TRY AGAIN!!")
            winda.quit()
            winda.destroy()
            self.planner()
            
    #--------------------------------------------------------------------------------------------------
     
#windinfo=tk.Tk()
    def buttonClick2(self):
        self.root.quit()
        self.root.destroy()
        self.personal_info()
   
#PERSONAL INFOMATION
    def personal_info(self):
        windinfo=tk.Tk()
        windinfo.title("PERSONAL INFORMATION")
        windinfo.geometry('1200x600+100+50')
        windinfo.after(1, lambda: windinfo.focus_force())


        label1=tk.Label(windinfo,text="FIRST NAME",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windinfo,text="LAST NAME",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windinfo,text="NUMBER OF FAMILY MEMBERS",height=5,width=30).grid(row=2,column=0)
        label4=tk.Label(windinfo,text="CONTACT NUMBER",height=5,width=30).grid(row=3,column=0)
        
        self.t3=Entry(windinfo)
        
        self.t3.grid(row=0,column=1,pady=5)
        self.t3.focus_set()
        
        self.t4=Entry(windinfo)
        self.t4.grid(row=1,column=1,pady=5)
        self.t5=Entry(windinfo).grid(row=2,column=1,pady=5)
        self.t6=Entry(windinfo)
        self.t6.grid(row=3,column=1,pady=5)
        Button(windinfo,text="NEXT   ->",width=10,height=3,command=windinfo.quit,bg='gray').grid(row=5,column=3)
   
    
        windinfo.mainloop()
        self.name=self.t3.get()
        self.surname=self.t4.get()
        self.contact=self.t6.get()
        windinfo.destroy()
        self.income()
#--------------------------------------------------------------------------------------------------------
            
        

#INCOME
    def income(self):
        windincome=tk.Tk()
        windincome.title("INCOME")
        windincome.geometry('1200x600+100+50')
        windincome.after(1, lambda: windincome.focus_force())

    
        label1=tk.Label(windincome,text="SALARY",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windincome,text="RENTAL INCOME",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windincome,text="PENSION",height=5,width=30).grid(row=2,column=0)
        label4=tk.Label(windincome,text="OTHER",height=5,width=30).grid(row=3,column=0)
        label5=Label(windincome)
        label5.config(text="*All fields are compulsory",width=40,fg='red',padx=5)
        label5.grid(row=0,column=3)
    
        self.t7=Entry(windincome)
        self.t7.grid(row=0,column=1,pady=5)
        self.t7.focus_set()
        self.t8=Entry(windincome)
        self.t8.grid(row=1,column=1,pady=5)
        self.t9=Entry(windincome)
        self.t9.grid(row=2,column=1,pady=5)
        self.t10=Entry(windincome)
        self.t10.grid(row=3,column=1,pady=5)
    
        Button(windincome,text="NEXT   ->",width=10,height=3,command=windincome.quit,bg='gray').grid(row=5,column=3)
    
        windincome.mainloop()
        if((self.t7.get().isdigit())and(self.t8.get().isdigit())and(self.t9.get().isdigit())and(self.t10.get().isdigit())):
            self.sumincome=int(self.t7.get())+int(self.t8.get())+int(self.t9.get())+int(self.t10.get())
            windincome.destroy()
            self.loan()
        else:
            tk.messagebox.showinfo("ERROR!!","Please fill all the details")
            windincome.destroy()
            self.income()
#--------------------------------------------------------------------------------------------------------
           
#LOAN
    def loan(self):
        windloan=tk.Tk()
        windloan.title("LOANS")
        windloan.geometry('1200x600+100+50')
        windloan.after(1, lambda: windloan.focus_force())

    
        label1=tk.Label(windloan,text="HOME LOAN",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windloan,text="CAR LOAN",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windloan,text="PERSONAL LOAN",height=5,width=30).grid(row=2,column=0)
        label4=tk.Label(windloan,text="OTHER",height=5,width=30).grid(row=3,column=0)
        label5=Label(windloan)
        label5.config(text="*All fields are compulsory",width=40,fg='red',padx=5)
        label5.grid(row=0,column=3)
    
        self.t11=Entry(windloan)
        self.t11.grid(row=0,column=1,pady=5)
        self.t11.focus_set()
        self.t12=Entry(windloan)
        self.t12.grid(row=1,column=1,pady=5)
        self.t13=Entry(windloan)
        self.t13.grid(row=2,column=1,pady=5)
        self.t14=Entry(windloan)
        self.t14.grid(row=3,column=1,pady=5)
    
        Button(windloan,text="NEXT   ->",width=10,height=3,command=windloan.quit,bg='gray').grid(row=5,column=3)
    
        windloan.mainloop()
        if((self.t11.get().isdigit())and(self.t12.get().isdigit())and(self.t13.get().isdigit())and(self.t14.get().isdigit())):
            self.sumloan=int(self.t11.get())+int(self.t12.get())+int(self.t13.get())+int(self.t14.get())
            self.sumloanperct=round((self.sumloan/self.sumincome)*100,2)
            self.idealloan=round(0.1*self.sumincome,2)
            windloan.destroy()
            self.tax()
        else:
            tk.messagebox.showinfo("ERROR!!","Please fill all the details")
            windloan.destroy()
            self.loan()
#---------------------------------------------------------------------------------------------------
        
         
    
#TAX
    def tax(self):
        windtax=tk.Tk()
        windtax.title("TAX")
        windtax.geometry('1200x600+100+50')
        windtax.after(1, lambda: windtax.focus_force())

       
        label1=tk.Label(windtax,text="INCOME TAX",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windtax,text="HOUSE TAX",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windtax,text="OTHER",height=5,width=30).grid(row=2,column=0)
        label4=Label(windtax)
        label4.config(text="*All fields are compulsory",width=40,fg='red',padx=5)
        label4.grid(row=0,column=3)
    
        self.t15=Entry(windtax)
        self.t15.grid(row=0,column=1,pady=5)
        self.t15.focus_set()
        self.t16=Entry(windtax)
        self.t16.grid(row=1,column=1,pady=5)
        self.t17=Entry(windtax)
        self.t17.grid(row=2,column=1,pady=5)

        Button(windtax,text="NEXT   ->",width=10,height=3,command=windtax.quit,bg='gray').grid(row=5,column=3)
    
        windtax.mainloop()
        if((self.t15.get().isdigit())and(self.t16.get().isdigit())and(self.t17.get().isdigit())):
             self.sumtax=int(self.t15.get())+int(self.t16.get())+int(self.t17.get())
             self.idealtax=round(0.18*self.sumincome,2)
             windtax.destroy()
             self.insurance()
        else:
            tk.messagebox.showinfo("ERROR!!","Please fill all the details")
            windtax.destroy()
            self.tax()
#------------------------------------------------------------------------------------------------------
        
#INSURANCE
    def insurance(self):
        windinsurance=tk.Tk()
        windinsurance.title("INSURANCE")
        windinsurance.geometry('1200x600+100+50')
        windinsurance.after(1, lambda: windinsurance.focus_force())

    
        label1=tk.Label(windinsurance,text="LIFE INSURANCE",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windinsurance,text="MEDICAL INSURANCE",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windinsurance,text="HOME INSURANCE",height=5,width=30).grid(row=2,column=0)
        label4=tk.Label(windinsurance,text="OTHER",height=5,width=30).grid(row=3,column=0)
        label5=Label(windinsurance)
        label5.config(text="*All fields are compulsory",width=40,fg='red',padx=5)
        label5.grid(row=0,column=3)
    
        self.t18=Entry(windinsurance)
        self.t18.grid(row=0,column=1,pady=5)
        self.t18.focus_set()
        self.t19=Entry(windinsurance)
        self.t19.grid(row=1,column=1,pady=5)
        self.t20=Entry(windinsurance)
        self.t20.grid(row=2,column=1,pady=5)
        self.t21=Entry(windinsurance)
        self.t21.grid(row=3,column=1,pady=5)

        Button(windinsurance,text="NEXT   ->",width=10,height=3,command=windinsurance.quit,bg='gray').grid(row=5,column=3)
    
        windinsurance.mainloop()
        if((self.t18.get().isdigit())and(self.t19.get().isdigit())and(self.t20.get().isdigit())and(self.t21.get().isdigit())):
            self.suminsurance=int(self.t18.get())+int(self.t19.get())+int(self.t20.get())+int(self.t21.get())
            self.suminsuranceperct=round((self.suminsurance/self.sumincome)*100,2)
            self.idealinsurance=round(0.15*self.sumincome,2)
            windinsurance.destroy()
            self.saving()
        else:
            tk.messagebox.showinfo("ERROR!!","Please fill all the details")
            windinsurance.destroy()
            self.insurance()

#-------------------------------------------------------------------------------------------------
        
           
            
        
#SAVING
    def saving(self):
        windsaving=tk.Tk()
        windsaving.title("SAVINGS")
        windsaving.geometry('1200x600+100+50')
        windsaving.after(1, lambda: windsaving.focus_force())

    
        label1=tk.Label(windsaving,text="MUTUAL FUNDS",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windsaving,text="DEPOSITS",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windsaving,text="STOCKS",height=5,width=30).grid(row=2,column=0)
        label4=Label(windsaving)
        label4.config(text="*All fields are compulsory",width=40,fg='red',padx=5)
        label4.grid(row=0,column=3)

        self.t22=Entry(windsaving)
        self.t22.grid(row=0,column=1,pady=5)
        self.t22.focus_set()
        self.t23=Entry(windsaving)
        self.t23.grid(row=1,column=1,pady=5)
        self.t24=Entry(windsaving)
        self.t24.grid(row=2,column=1,pady=5)

        Button(windsaving,text="NEXT   ->",width=10,height=3,command=windsaving.quit,bg='gray').grid(row=5,column=3)
    
        windsaving.mainloop()
        if((self.t22.get().isdigit())and(self.t23.get().isdigit())and(self.t24.get().isdigit())):
            self.sumsaving=int(self.t22.get())+int(self.t23.get())+int(self.t24.get())
            self.sumsavingperct=round((self.sumsaving/self.sumincome)*100,2)
            self.idealsaving=round(0.17*self.sumincome,2)
            windsaving.destroy()
            self.living()
        else:
            tk.messagebox.showinfo("ERROR!!","Please fill all the details")
            windsaving.destroy()
            
            self.saving()
#-------------------------------------------------------------------------------------------------
        
           
        
#living
    def living(self):
        windliving=tk.Tk()
        windliving.title("LIVING")
        windliving.geometry('1300x700+100+50')
        windliving.after(1, lambda: windliving.focus_force())

    
        label1=tk.Label(windliving,text="FOOD",height=5,width=30).grid(row=0,column=0)
        label2=tk.Label(windliving,text="ELECTRICITY",height=5,width=30).grid(row=1,column=0)
        label3=tk.Label(windliving,text="WATER",height=5,width=30).grid(row=2,column=0)
        label4=tk.Label(windliving,text="TELEPHONE",height=5,width=30).grid(row=3,column=0)
        label5=tk.Label(windliving,text="CLOTHING",height=5,width=30).grid(row=4,column=0)
        label6=tk.Label(windliving,text="MEDICINES",height=5,width=30).grid(row=5,column=0)
        label7=tk.Label(windliving,text="OTHER",height=5,width=30).grid(row=6,column=0)
        label8=Label(windliving)
        label8.config(text="*All fields are compulsory",width=40,fg='red',padx=5)
        label8.grid(row=0,column=3)
    
        self.t25=Entry(windliving)
        self.t25.grid(row=0,column=1,pady=5)
        self.t25.focus_set()
        self.t26=Entry(windliving)
        self.t26.grid(row=1,column=1,pady=5)
        self.t27=Entry(windliving)
        self.t27.grid(row=2,column=1,pady=5)
        self.t28=Entry(windliving)
        self.t28.grid(row=3,column=1,pady=5)
        self.t29=Entry(windliving)
        self.t29.grid(row=4,column=1,pady=5)
        self.t30=Entry(windliving)
        self.t30.grid(row=5,column=1,pady=5)
        self.t31=Entry(windliving)
        self.t31.grid(row=6,column=1,pady=5)
    
        Button(windliving,text="SUBMIT",width=10,height=3,command=windliving.quit,bg='gray').grid(row=7,column=5)
    
        windliving.mainloop()
        if((self.t25.get().isdigit())and(self.t26.get().isdigit())and(self.t27.get().isdigit())and(self.t28.get().isdigit())and(self.t29.get().isdigit())and(self.t30.get().isdigit())and(self.t31.get().isdigit())):
            self.sumliving=int(self.t25.get())+int(self.t26.get())+int(self.t27.get())+int(self.t28.get())+int(self.t29.get())+int(self.t30.get())+int(self.t31.get())
            self.sumlivingperct=round((self.sumliving/self.sumincome)*100,2)
            self.idealliving=round(0.4*self.sumincome,2)
            windliving.destroy()
            self.insert()
            self.display()
        else:
            tk.messagebox.showinfo("ERROR!!","Please fill all the details")
           
            windliving.destroy()
            self.living()
#-------------------------------------------------------------------------------------------------
        
           
    def display(self):
        winddisplay=tk.Tk()
        winddisplay.title("DISPLAY")
        winddisplay.geometry('1300x700+100+50')
        

        label1=Label(winddisplay)
        label1.config(text="NAME:",width=20,bg='ivory1',fg='royalblue')
        label1.place(x=100,y=100)

        text1=Label(winddisplay)
        text1.config(text=""+self.name+" "+self.surname,width=60,bg='lavenderblush1',fg='hotpink1')
        text1.place(x=200,y=100)

        label2=Label(winddisplay)
        label2.config(text="INCOME:",width=20,bg='ivory1',fg='royalblue')
        label2.place(x=100,y=125)

        text2=Label(winddisplay)
        text2.config(text=""+str(self.sumincome),width=60,bg='lavenderblush1',fg='hotpink',padx=5)
        text2.place(x=200,y=125)

        label3=Label(winddisplay)
        label3.config(text="LOAN:",width=20,bg='ivory1',fg='royalblue')
        label3.place(x=100,y=150)

        label4=Label(winddisplay)
        label4.config(text="IDEAL AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label4.place(x=200,y=150)

        text4=Label(winddisplay)
        text4.config(text=""+str(self.idealloan),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text4.place(x=350,y=150)

        label5=Label(winddisplay)
        label5.config(text="YOUR AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label5.place(x=200,y=175)

        text5=Label(winddisplay)
        text5.config(text=""+str(self.sumloan),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text5.place(x=350,y=175)

        if(10<self.sumloanperct):
             label6=Label(winddisplay)
             label6.config(text="* YOUR ARE SPENDING "+str(self.sumloanperct-10)+"% MORE ON LOAN",fg="red",width=50)
             label6.place(x=600,y=150)
        else:
              label6=Label(winddisplay)
              label6.config(text="*YOU CAN SPEND "+str(10-self.sumloanperct)+"% MORE ON LOAN",fg="red",width=50)
              label6.place(x=600,y=150)

        label3=Label(winddisplay)
        label3.config(text="TAX:",width=20,bg='ivory1',fg='royalblue')
        label3.place(x=100,y=200)

        label5=Label(winddisplay)
        label5.config(text="YOUR AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label5.place(x=200,y=200)

        text5=Label(winddisplay)
        text5.config(text=""+str(self.sumtax),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text5.place(x=350,y=200)

        label3=Label(winddisplay)
        label3.config(text="INSURANCE:",width=18,bg='ivory1',fg='royalblue')
        label3.place(x=100,y=225)

        label4=Label(winddisplay)
        label4.config(text="IDEAL AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label4.place(x=200,y=225)

        text4=Label(winddisplay)
        text4.config(text=""+str(self.idealinsurance),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text4.place(x=350,y=225)

        label5=Label(winddisplay)
        label5.config(text="YOUR AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label5.place(x=200,y=250)

        text5=Label(winddisplay)
        text5.config(text=""+str(self.suminsurance),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text5.place(x=350,y=250)

        if(15<self.suminsuranceperct):
         label6=Label(winddisplay)
         label6.config(text="*YOUR ARE SPENDING "+str(self.suminsuranceperct-15)+"% MORE ON INSURANCE",fg="red",width=50)
         label6.place(x=600,y=225)
        else:
          label6=Label(winddisplay)
          label6.config(text="*YOU CAN SPEND "+str(15-self.suminsuranceperct)+"% MORE ON INSURANCE",fg="red",width=50)
          label6.place(x=600,y=225)

        label3=Label(winddisplay)
        label3.config(text="SAVING:",width=20,bg='ivory1',fg='royalblue')
        label3.place(x=100,y=275)

        label4=Label(winddisplay)
        label4.config(text="IDEAL AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label4.place(x=200,y=275)

        text4=Label(winddisplay)
        text4.config(text=""+str(self.idealsaving),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text4.place(x=350,y=275)

        label5=Label(winddisplay)
        label5.config(text="YOUR AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label5.place(x=200,y=300)

        text5=Label(winddisplay)
        text5.config(text=""+str(self.sumsaving),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text5.place(x=350,y=300)

        if(17<self.sumsavingperct):
         label6=Label(winddisplay)
         label6.config(text="*YOUR ARE SPENDING "+str(self.sumsavingperct-17)+"% MORE ON SAVING",fg="red",width=50)
         label6.place(x=600,y=275)
        else:
          label6=Label(winddisplay)
          label6.config(text="*YOU CAN SPEND "+str(17-self.sumsavingperct)+"% MORE ON SAVING",fg="red",width=50)
          label6.place(x=600,y=275)

        label3=Label(winddisplay)
        label3.config(text="LIVING:",width=20,bg='ivory1',fg='royalblue')
        label3.place(x=100,y=325)

        label4=Label(winddisplay)
        label4.config(text="IDEAL AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label4.place(x=200,y=325)

        text4=Label(winddisplay)
        text4.config(text=""+str(self.idealloan),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text4.place(x=350,y=325)

        label5=Label(winddisplay)
        label5.config(text="YOUR AMOUNT:",width=20,bg='ivory1',fg='royalblue',padx=5)
        label5.place(x=200,y=350)

        text5=Label(winddisplay)
        text5.config(text=""+str(self.sumliving),width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text5.place(x=350,y=350)

        if(40<self.sumlivingperct):
         label6=Label(winddisplay)
         label6.config(text="* YOUR ARE SPENDING "+str(self.sumlivingperct-40)+"% MORE ON LIVING",fg="red",width=50)
         label6.place(x=600,y=325)
        else:
          label6=Label(winddisplay)
          label6.config(text="*YOU CAN SPEND "+str(40-self.sumlivingperct)+"% MORE ON LIVING",fg="red",width=50)
          label6.place(x=600,y=325)

        label12=Label(winddisplay)
        label12.config(text="FIELD",width=20,bg='ivory1',fg='royalblue',padx=5)
        label12.place(x=500,y=425)

        text12=Label(winddisplay)
        text12.config(text="IDEAL VALUES",width=40,bg='ivory1',fg='royalblue',padx=5)
        text12.place(x=650,y=425)
        
        label7=Label(winddisplay)
        label7.config(text="LOAN",width=20,bg='ivory1',fg='royalblue',padx=5)
        label7.place(x=500,y=450)

        text7=Label(winddisplay)
        text7.config(text="10% OF INCOME",width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text7.place(x=650,y=450)

        label8=Label(winddisplay)
        label8.config(text="TAXES",width=20,bg='ivory1',fg='royalblue',padx=5)
        label8.place(x=500,y=475)

        text8=Label(winddisplay)
        text8.config(text="18% OF INCOME",width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text8.place(x=650,y=475)

        label9=Label(winddisplay)
        label9.config(text="INSURANCE",width=20,bg='ivory1',fg='royalblue',padx=5)
        label9.place(x=500,y=500)

        text9=Label(winddisplay)
        text9.config(text="15% OF INCOME",width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text9.place(x=650,y=500)

        label10=Label(winddisplay)
        label10.config(text="SAVING",width=20,bg='ivory1',fg='royalblue',padx=5)
        label10.place(x=500,y=525)

        text10=Label(winddisplay)
        text10.config(text="17% OF INCOME",width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text10.place(x=650,y=525)

        label11=Label(winddisplay)
        label11.config(text="LIVING",width=20,bg='ivory1',fg='royalblue',padx=5)
        label11.place(x=500,y=550)

        text11=Label(winddisplay)
        text11.config(text="40% OF INCOME",width=40,bg='lavenderblush',fg='hotpink',padx=5)
        text11.place(x=650,y=550)

        winddisplay.mainloop()
#-------------------------------------------------------------------------------------------------
   
exp=Expenditure()    

