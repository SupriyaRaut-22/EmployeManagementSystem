from tkinter import *
from tkinter.messagebox import *
import tkinter as tk
from sqlite3 import *
from tkinter.scrolledtext import *
import matplotlib.pyplot as plt
from requests import *


def l():
    mw.deiconify()
    aw.withdraw()
    vw.withdraw()
    dw.withdraw()
    uw.withdraw()
    cw.withdraw()

def l1():
    aw.deiconify()
    mw.withdraw()
    vw.withdraw()
    dw.withdraw()
    uw.withdraw()
    cw.withdraw()

def l2():
    vw.deiconify()
    mw.withdraw()
    aw.withdraw()
    dw.withdraw()
    uw.withdraw()
    cw.withdraw()

def l3():
    uw.deiconify()
    mw.withdraw()
    aw.withdraw()
    vw.withdraw()
    dw.withdraw()
    cw.withdraw()

def l4():
    dw.deiconify()
    mw.withdraw()
    aw.withdraw()
    vw.withdraw()
    uw.withdraw()
    cw.withdraw()

def l5():
    cw.deiconify()
    mw.withdraw()
    aw.withdraw()
    dw.withdraw()
    uw.withdraw()
    vw.withdraw()

def graph():
    con = None
    try:
        con = connect("ms.db")
        cursor = con.cursor()
        sql = "SELECT name, salary FROM employee ORDER BY salary DESC LIMIT 5"
        cursor.execute(sql)
        data = cursor.fetchall()
        name = []
        salary = []
        for i in data:
            name.append(i[0])
            salary.append(i[1])
        plt.bar(name, salary)
        plt.xlabel("Names of Employee")
        plt.ylabel("Salary of Employee's")
        plt.title("Top 5 Highest Salaried Employee")
        plt.show()
    except Exception as e:
        showerror("issue ", e)
        con.rollback()
    finally:
        if con is not None:
            con.close()
    
def aw_save():
    con=None
    try:
        eid=ent1.get()
        if len(eid)==0:
            raise Exception("Employee ID cannot be Empty") 
        
        if eid.isspace():
            raise Exception("Employee ID cannot be only spaces")
        
        if eid.isalpha():
            raise Exception("Employee ID Should only contain Numbers")
        
        name=ent2.get()
        if len(name)==0:
            raise Exception("Name cannot be Empty") 
        
        if name.isspace():
            raise Exception("Name cannot be only spaces")
        
        if name.isdigit():
            raise Exception("Name Should be only Alphabets")
        
        salary=ent3.get()
        if len(salary)==0:
            raise Exception("Salary cannot be Empty") 
        
        if salary.isspace():
            raise Exception("Salary cannot be only spaces")
        
        if salary.isalpha():
            raise Exception("Salary Should only contain Numbers")
        
        con=connect("ms.db")
        cursor=con.cursor()
        cursor.execute('INSERT INTO employee(eid,name,salary)VALUES(?,?,?)',(eid,name,salary,))
        con.commit()
        showinfo("Success","Employee Record Created")
        ent1.delete(0,END)
        ent2.delete(0,END)
        ent3.delete(0,END)
        ent1.focus()
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()


def vw_data():
    vw.deiconify()
    mw.withdraw()
    aw.withdraw()
    dw.withdraw()
    uw.withdraw()
    cw.withdraw()
    vw_data_view.delete(1.0,END)
    con=None
    try:
        con=connect("ms.db")
        cursor=con.cursor()
        cursor.execute('Select * from employee')
        con.commit()
        data=cursor.fetchall()
        info=""
        for d in data:
            info=info+"Emp-id:"+ str(d[0])+"\n"+"Name:"+str(d[1])+","+"Salary:"+str(d[2])+"\n"+"\n"
        vw_data_view.insert(INSERT,info)

    except Exception as e:
        showerror("Issue",e)

    finally:
        if con is not None:
            con.close()
        
def dw_delete():
    if askyesno("Warning","DATA WILL NOT RECOVER AGAIN"):
        num=ent7.get()
        if len(num)==0:
            raise Exception("Emp-ID cannot be Empty") 
        
        if num.isspace():
            raise Exception("Emp-ID cannot be only spaces")
        
        if num.isalpha():
            raise Exception("Emp-ID Should only contain Numbers")
        
        con=None
        try:
            con=connect("ms.db")
            cursor=con.cursor()
            cursor.execute('Delete from employee where eid=?',(num,))
            con.commit()
            showinfo("Success","Employee Record Deleted")
            vw_data_view.delete(1.0,END)
            ent7.delete(0,END)
            ent7.focus()
        except Exception as e:
            showerror("Issue",e)
        finally:
            if con is not None:
                con.close()
def location():
    API_key="97535a80-5ec3-11ee-97a8-810bdd2f060f"
    url = "https://geolocation-db.com/json/97535a80-5ec3-11ee-97a8-810bdd2f060f"
    res = get(url)
    data = res.json()
    locate=data['city']
    lab10.configure(text="Loaction: "+locate)
    #print(data)

def temperature():
    API_key="da7ddd8898b3b3abf865e4243cc3c716"
    url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name="Mumbai"
    comp_url = url + "lat=19.218&lon=72.9780" + "&appid=" + API_key
    res = get(comp_url)
    data = res.json()
    #print(data)
    temp=data['main']['temp']
    cel=temp-273.5
    #print(cel)
    #print(temp)
    lab11.configure(text="Temperature: "+str(round(cel,2))+" Celsius")
   
    

def uw_save():
    con=None
    try: 
        eeid=ent4.get()
        if len(eeid)==0:
            raise Exception("Employee-ID cannot be Empty") 
            
        if eeid.isspace():
            raise Exception("Employee-ID cannot be only spaces")
        
        if eeid.isalpha():
            raise Exception("Employee-ID Should only contain Numbers")
        
        ename=ent5.get()
        if len(ename)==0:
            raise Exception("Name cannot be Empty") 
        
        if ename.isspace():
            raise Exception("Name cannot be only spaces")
        
        if ename.isdigit():
            raise Exception("Name Should be only Alphabets")
        
        esalary=ent6.get()
        if len(esalary)==0:
            raise Exception("Salary cannot be Empty") 
        
        if esalary.isspace():
            raise Exception("Salary cannot be only spaces")
        
        if esalary.isalpha():
            raise Exception("Salary Should only contain Numbers")
           
        con=connect("ms.db")
        cursor=con.cursor()
        cursor.execute("Update employee SET name='%s',salary='%s' WHERE eid='%s'"%(ename,esalary,eeid))
        con.commit()
        showinfo("Success","Employee Record Updated")
        ent4.delete(0,END)
        ent5.delete(0,END)
        ent6.delete(0,END)
        ent4.focus()
    except Exception as e:
        showerror("Issue",e)
    finally:
        if con is not None:
            con.close()

#main window configuration

mw=Tk()
mw.title("Employee Management System")
mw.geometry("800x700+100+100")
mw.configure(bg="#09A3BA")
f=("Comic Sans-Serif",30,"bold")

btn=Button(mw,text="Add",font=f,background="lightgrey",foreground="black",width=15,command=l1)
btn.pack(pady=20)

btn1=Button(mw,text="View",font=f,background="lightgrey",foreground="black",width=15,command=vw_data)
btn1.pack(pady=10)

btn2=Button(mw,text="Update",font=f,background="lightgrey",foreground="black",width=15,command=l3)
btn2.pack(pady=10)

btn3=Button(mw,text="Delete",font=f,background="lightgrey",foreground="black",width=15,command=l4)
btn3.pack(pady=10)

btn4=Button(mw,text="Charts",font=f,background="lightgrey",foreground="black",width=15,command=l5)
btn4.pack(pady=10)

lab10=Label(mw,text="Location: ",font=f,background="#09A3BA")
lab10.pack(pady=10)
location()

lab11=Label(mw,text="Temperature: ",font=f,background="#09A3BA")
lab11.pack(pady=10)
temperature()


#add window configuration

aw=Tk()
aw.title("Window-->Add Employee")
aw.geometry("800x700+100+100")
aw.configure(bg="#09A3BA")
f=("Comic Sans Serif",30,"bold")
aw.withdraw()

lab1=Label(aw,text="Enter Emp-id:",font=f,background="#09A3BA")
ent1=Entry(aw,font=f)
lab1.pack(pady=10)
ent1.pack(pady=10)

lab2=Label(aw,text="Enter Name:",font=f,background="#09A3BA")
ent2=Entry(aw,font=f)
lab2.pack(pady=10)
ent2.pack(pady=10)

lab3=Label(aw,text="Enter Salary:",font=f,background="#09A3BA")
ent3=Entry(aw,font=f)
lab3.pack(pady=10)
ent3.pack(pady=10)

btn5=Button(aw,text="Save",font=f,background="black",foreground="white",width=10,command=aw_save)
btn5.pack(pady=20)

btn6=Button(aw,text="Back",font=f,background="lightgrey",foreground="black",width=10,command=l)
btn6.pack(pady=10)


#View Window Configuration
vw=Tk()
vw.title("Window-->View Employee")
vw.geometry("800x700+100+100")
vw.configure(bg="#09A3BA")
f=("Comic Sans Serif",25,"bold")
vw.withdraw()

vw_data_view=ScrolledText(vw,width=40,height=15,font=f)
vw_data_view.pack(pady=10)

btn7=Button(vw,text="Back",font=f,background="black",foreground="white",width=10,command=l)
btn7.pack(pady=10)


#Update Window Configuration
uw=Tk()
uw.title("Window-->Update Employee")
uw.geometry("800x700+100+100")
uw.configure(bg="#09A3BA")
f=("Comic Sans Serif",30,"bold")
uw.withdraw()

lab6=Label(uw,text="Enter Emp-id:",font=f,background="#09A3BA")
ent4=Entry(uw,font=f)
lab6.pack(pady=10)
ent4.pack(pady=10)

lab7=Label(uw,text="Enter Name:",font=f,background="#09A3BA")
ent5=Entry(uw,font=f)
lab7.pack(pady=10)
ent5.pack(pady=10)

lab8=Label(uw,text="Enter Salary:",font=f,background="#09A3BA")
ent6=Entry(uw,font=f)
lab8.pack(pady=10)
ent6.pack(pady=10)

btn8=Button(uw,text="Save",font=f,background="black",foreground="white",width=10,command=uw_save)
btn8.pack(pady=20)

btn9=Button(uw,text="Back",font=f,background="lightgrey",foreground="black",width=10,command=l)
btn9.pack(pady=10)


#Delete Window Configuration
dw=Tk()
dw.title("Window-->Delete Employee")
dw.geometry("800x700+100+100")
dw.configure(bg="#09A3BA")
f=("Comic Sans Serif",30,"bold")
dw.withdraw()

lab9=Label(dw,text="Enter Emp-id:",font=f,background="#09A3BA")
ent7=Entry(dw,font=f)
lab9.pack(pady=10)
ent7.pack(pady=10)

btn10=Button(dw,text="Save",font=f,background="black",foreground="white",width=10,command=dw_delete)
btn10.pack(pady=20)

btn11=Button(dw,text="Back",font=f,background="lightgrey",foreground="black",width=10,command=l)
btn11.pack(pady=10)


#chart window configuration
cw=Tk()
cw.title("Window-->Charts Result")
cw.geometry("800x700+100+100")
cw.configure(bg="#09A3BA")
f=("Comic Sans Serif",30,"bold")
cw.withdraw()

btn12=Button(cw,text="Show Graph",font=f,background="lightgrey",foreground="black",width=10,command=graph)
btn12.pack(pady=10)

btn13=Button(cw,text="Back",font=f,background="lightgrey",foreground="black",width=10,command=l)
btn13.pack(pady=10)

def on_closing():
    if askokcancel("Quit","Do you want to quit?"):
        mw.destroy()
        aw.destroy()
        vw.destroy()
        uw.destroy()
        dw.destroy()
        cw.destroy()

mw.protocol("WM_DELETE_WINDOW",on_closing)
aw.protocol("WM_DELETE_WINDOW",on_closing)
vw.protocol("WM_DELETE_WINDOW",on_closing)
uw.protocol("WM_DELETE_WINDOW",on_closing)
dw.protocol("WM_DELETE_WINDOW",on_closing)
cw.protocol("WM_DELETE_WINDOW",on_closing)


mw.mainloop()
