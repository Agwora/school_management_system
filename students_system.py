from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from tkinter import messagebox as mb
import time
import mysql.connector
import mysql.connector as connector
from PIL import ImageTk
from tkinter import filedialog
import pandas
count=0
# text=[]

def system():
    def toplevel(title,button_text,command):
        global screen,fname_entry,sname_entry,suname_entry,age_uname_entry,gender_name_entry,form_name_entry,D_name_entry,UPI_name_entry,adm_name_entry,religion_name_entry,disability_name_entry,parent_name_entry,phone_name_entry,address_name_entry,occupation_name_entry,city_name_entry
        screen=Toplevel()
        screen.geometry('550x650+140+34')
        screen.title(title)
        screen['background']='white'
        screen.resizable(False,False)
        screen.grab_set()


        title_label=Label(screen,text='STUDENTS DETAILS',bg='white',font=('calibri 15 bold'))
        title_label.place(x=190,y=10)


        first_name_label=Label(screen,text='First name:',bg='white',font=('calibri 11'))
        first_name_label.place(x=20,y=70)

        fname_entry=Entry(screen,width=10,font=('calibri 15 bold'))
        fname_entry.place(x=97,y=70)

        sname_entry=Entry(screen,width=10,font=('calibri 15 bold'))
        sname_entry.place(x=267,y=70)

        suname_entry=Entry(screen,width=10,font=('calibri 15 bold'))
        suname_entry.place(x=407,y=70)


        second_name_label=Label(screen,text='Second name:',bg='white',font=('calibri 11'))
        second_name_label.place(x=170,y=70)

        first_name_label=Label(screen,text='Surname:',bg='white',font=('calibri 11'))
        first_name_label.place(x=340,y=70)


        age_label=Label(screen,text='Age:',bg='white',font=('calibri 11'))
        age_label.place(x=20,y=130)

        age_uname_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        age_uname_entry.place(x=60,y=130)

        gender_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        gender_name_entry.place(x=217,y=130)

        form_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        form_name_entry.place(x=367,y=130)


        gender_label=Label(screen,text='Gender:',bg='white',font=('calibri 11'))
        gender_label.place(x=160,y=130)

        form_label=Label(screen,text='form:',bg='white',font=('calibri 11'))
        form_label.place(x=320,y=130)

        adm_label=Label(screen,text='Admision number:',bg='white',font=('calibri 11'))
        adm_label.place(x=310,y=180)

        D_label=Label(screen,text='D.O.B:',bg='white',font=('calibri 11'))
        D_label.place(x=10,y=180)

        D_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        D_name_entry.place(x=55,y=180)


        UPI_label=Label(screen,text='UPI number:',bg='white',font=('calibri 11'))
        UPI_label.place(x=130,y=180)

        UPI_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        UPI_name_entry.place(x=215,y=180)

        adm_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        adm_name_entry.place(x=433,y=180)

        religion_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        religion_name_entry.place(x=245,y=250)

        disability_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        disability_name_entry.place(x=427,y=250)


        religion_label=Label(screen,text='Religion:',bg='white',font=('calibri 11'))
        religion_label.place(x=180,y=250)

        disability_label=Label(screen,text='Disability:',bg='white',font=('calibri 11'))
        disability_label.place(x=350,y=250)

        other_label=Label(screen,text='OTHER DETAILS',bg='white',font=('calibri 15 bold'))
        other_label.place(x=190,y=300)

        parent_name_label=Label(screen,text='Gurdian/parent name:',bg='white',font=('calibri 11'))
        parent_name_label.place(x=20,y=350)

        parent_name_entry=Entry(screen,width=30,font=('calibri 15 bold'))
        parent_name_entry.place(x=165,y=350)

        phone_name_entry=Entry(screen,width=17,font=('calibri 15 bold'))
        phone_name_entry.place(x=125,y=400)

        address_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        address_name_entry.place(x=320,y=400)

        occupation_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        occupation_name_entry.place(x=100,y=450)

        city_name_entry=Entry(screen,width=13,font=('calibri 15 bold'))
        city_name_entry.place(x=330,y=450)

        phone_label=Label(screen,text='Phone number:',bg='white',font=('calibri 11'))
        phone_label.place(x=20,y=400)

        adr_name_label=Label(screen,text='Address:',bg='white',font=('calibri 11'))
        adr_name_label.place(x=260,y=400)

        occ_name_label=Label(screen,text='Occupation:',bg='white',font=('calibri 11'))
        occ_name_label.place(x=20,y=450)

        city_name_label=Label(screen,text='town/city:',bg='white',font=('calibri 11'))
        city_name_label.place(x=260,y=450)


        savebtn=Button(screen,bd=7,text=button_text,bg='coral',activebackground='coral',activeforeground='black',width=15,height=1,font=('Batang 11'),command=command)
        savebtn.place(x=190,y=500)

        footer_name_label=Label(screen,text='@2023,All right reserved\n\nPowered by sci_AGWORA',bg='white',font=('calibri 11 bold'))
        footer_name_label.place(x=180,y=570)

        if title == 'Update Students':
            indexing=tree.focus()
            content=tree.item(indexing)
            listdata=content['values']
            fname_entry.insert(0,listdata[1])
            sname_entry.insert(0,listdata[2])
            suname_entry.insert(0,listdata[3])
            age_uname_entry.insert(0,listdata[4])
            gender_name_entry.insert(0,listdata[5])
            form_name_entry.insert(0,listdata[6])
            D_name_entry.insert(0,listdata[7])
            UPI_name_entry.insert(0,listdata[8])
            adm_name_entry.insert(0,listdata[9])
            religion_name_entry.insert(0,listdata[10])
            disability_name_entry.insert(0,listdata[11])
            parent_name_entry.insert(0,listdata[12])
            phone_name_entry.insert(0,listdata[13])
            address_name_entry.insert(0,listdata[14])
            occupation_name_entry.insert(0,listdata[15])
            city_name_entry.insert(0,listdata[16])


        screen.mainloop()

    def delete_student():
        try:
            mydb2=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='students_detail')
            mycursor2=mydb2.cursor()
            indexing=tree.focus()
            # print(indexing)
            content=tree.item(indexing)
            content_id=content['values'][0]
            content_id1=content['values'][1]
            quary='use students_detail'
            mycursor2.execute(quary)
            quary='delete from students_data where Id=%s'
            mycursor2.execute(quary,(content_id,))
            mydb2.commit()
            confirm=messagebox.askyesno('confirm',f'are you sure you want to delete the data for ({content_id1})?')
            if confirm:
                messagebox.showinfo('Deleted',f'Id number {content_id} is deleted successfully')
                quary='select * from  students_data'
                mycursor2.execute(quary)
                row=mycursor2.fetchall()
                tree.delete(*tree.get_children())
                for data in row:
                    tree.insert('',END,values=data)
        except:
            messagebox.showerror('Error','Nothing to be deleted, Please select at least one student.')


    def update_details():
        mydb2=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='students_detail')
        mycursor2=mydb2.cursor()
        quary='use students_detail'
        mycursor2.execute(quary)
        query="update students_data set first_name=%s,second_name=%s,surname=%s,age=%s,gender=%s,form=%s,Date_of_birth=%s,Upi_number=%s,Adm_number=%s,Religion=%s,Disability=%s,parent_name=%s,phone_number=%s,Address=%s,Occupation=%s,Town_city=%s,Added_date=%s,Added_time=%s where Adm_number=%s"
        mycursor2.execute(query,(fname_entry.get(),sname_entry.get(),suname_entry.get(),age_uname_entry.get(),gender_name_entry.get(),form_name_entry.get(),D_name_entry.get(),UPI_name_entry.get(),adm_name_entry.get(),religion_name_entry.get(),disability_name_entry.get(),parent_name_entry.get(),phone_name_entry.get(),address_name_entry.get(),occupation_name_entry.get(),city_name_entry.get(),date,current_time,adm_name_entry.get()))
        mydb2.commit()
        messagebox.showinfo('Succcess',f'Data for adm_number {adm_name_entry.get()} is successfully updated.')
        screen.destroy()
        show_st()


    def search_data():
        global mycursor,mydb

        global mydb2,mycursor2
        # if  s_fname_entry.get()=='':

        # elif s_sname_entry.get()=='' or s_gender_name_entry.get()=='' or s_form_name_entry.get()=='' or s_adm_name_entry.get()=='' or s_phone_name_entry.get()=='':
        #     messagebox.showerror('Error','Search by entering some details.....name,addmision number or phone number') 
        # else:
        try:
            mydb2=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='students_detail')
            mycursor2=mydb2.cursor()
        except:
            messagebox.showerror('Error','Database issue,,please try again',parent=screen)
            return
        quary='select * from students_data where first_name=%s or second_name=%s or gender=%s or form=%s or Adm_number=%s or phone_number=%s'
        mycursor2.execute(quary,(fname_entry.get(),sname_entry.get(),suname_entry.get(),form_name_entry.get(),adm_name_entry.get(),phone_name_entry.get()))
        row=mycursor2.fetchall()
        tree.delete(*tree.get_children())
        for data in row:
            tree.insert('',END,values=data)
            

            # messagebox.showerror('Error','Details not found',parent=search)
    
    def register1():
        global mycursor,mydb
        def clear():
            fname_entry.delete(0,END)
            sname_entry.delete(0,END)
            suname_entry.delete(0,END)
            age_uname_entry.delete(0,END)
            gender_name_entry.delete(0,END)
            form_name_entry.delete(0,END)
            D_name_entry.delete(0,END)
            UPI_name_entry.delete(0,END)
            adm_name_entry.delete(0,END)
            religion_name_entry.delete(0,END)
            disability_name_entry.delete(0,END)
            parent_name_entry.delete(0,END)
            phone_name_entry.delete(0,END)
            address_name_entry.delete(0,END)
            occupation_name_entry.delete(0,END)
            city_name_entry.delete(0,END)
            # ADDED_name_entry.delete(0,END)
        if fname_entry.get()=='' or age_uname_entry.get()=='' or phone_name_entry.get()=='':
            messagebox.showerror('Error','Please enter at least your name age and phone number to proceed',parent=screen)
        else:
            try:
                mydb=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023')
                mycursor=mydb.cursor()

            except:
                messagebox.showerror('Error','Database connection issue, Please try again',parent=screen)
                return
            try:
                quary='create database students_detail'
                mycursor.execute(quary)

                quary='use students_detail'
                mycursor.execute(quary)

                quary='create table students_data(Id int auto_increment primary key not null,first_name varchar(50) not null,second_name varchar(50),surname varchar(30),age int not null,gender varchar(20),form varchar(10),Date_of_birth varchar(50),Upi_number varchar(50),Adm_number varchar(50),Religion varchar(50),Disability varchar(20),parent_name varchar(50),phone_number int,Address varchar(30),Occupation varchar(50),Town_city varchar(50),Added_date varchar(50),Added_time varchar(50))'
                mycursor.execute(quary)

            except:
                mycursor.execute('use students_detail')
            try:
                
                query="insert into students_data(first_name,second_name,surname,age,gender,form,Date_of_birth,Upi_number,Adm_number,Religion,Disability,parent_name,phone_number,Address,Occupation,Town_city,Added_date,Added_time) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query,(fname_entry.get(),sname_entry.get(),suname_entry.get(),age_uname_entry.get(),gender_name_entry.get(),form_name_entry.get(),D_name_entry.get(),UPI_name_entry.get(),adm_name_entry.get(),religion_name_entry.get(),disability_name_entry.get(),parent_name_entry.get(),phone_name_entry.get(),address_name_entry.get(),occupation_name_entry.get(),city_name_entry.get(),date,current_time))
                mydb.commit()
                answer=messagebox.askyesno('Confirm','Registration successful. Do you need to clear the form?',parent=screen)
                if answer:
                    clear()


                quary='select * from students_data'
                mycursor.execute(quary)
                row=mycursor.fetchall()
                tree.delete(*tree.get_children())
                for data in row:
                    tree.insert('',END,values=data)
            except:
                messagebox.showerror('Error','Something went wrong please try again',parent=screen)
    def pin_window():
        global database_window,user1_name_entry,confirm_pin_name_entry,pin_name_entry
        database_window=Tk()
        database_window.title('Connect pin set')
        database_window.grab_set()
        database_window.geometry('400x300+400+200')
        database_window.resizable(False,False)
        host=StringVar()
        host.set('Localhost')


        _label=Label(database_window,text='Memorize the pin clearly, It will be needed in the system to activate the buttons*\nmemorize it clearly',font=('calibri 10 bold'))
        _label.place(x=10,y=5)

        host_label=Label(database_window,text='Host name:',font=('calibri 14 bold'))
        host_label.place(x=10,y=50)

        host_name_entry=Entry(database_window,textvariable=host,font=('calibri 14 bold'))
        host_name_entry.place(x=120,y=50)

        user1_name_entry=Entry(database_window,font=('calibri 14 bold'))
        user1_name_entry.place(x=120,y=100)

        pin_name_entry=Entry(database_window,font=('calibri 14 bold'))
        pin_name_entry.place(x=120,y=160)



        Username_label=Label(database_window,text='Username:',font=('calibri 14 bold'))
        Username_label.place(x=10,y=100)

        pin_label=Label(database_window,text='Pin:',font=('calibri 14 bold'))
        pin_label.place(x=10,y=160)

        confirm_pin_label=Label(database_window,text='Confirm Pin:',font=('calibri 14 bold'))
        confirm_pin_label.place(x=10,y=190)

        confirm_pin_name_entry=Entry(database_window,font=('calibri 14 bold'))
        confirm_pin_name_entry.place(x=120,y=190)

        connection_btn=Button(database_window,text='Set',bg='coral',activebackground='coral',activeforeground='black',width=15,height=1,font=('Batang 11'),command=connect1)
        connection_btn.place(x=100,y=250)

        database_window.mainloop()
    def connect1():
        if user1_name_entry.get()=='' or  pin_name_entry.get()=='' or confirm_pin_name_entry.get()=='':
            mb.showerror("Error",'All entries are required',parent=database_window)

        elif pin_name_entry.get()!=confirm_pin_name_entry.get():
            mb.showerror('Error','Pin must be the same',parent=database_window)
        else:
            try:
                database=connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='userdata')
                mycursor=database.cursor()
            except:
                mb.showerror('Error','Database connection issues, try again later')
            try:
                quary='create table connect_pin(id int auto_increment primary key,username varchar(50),pin varchar(20))'
                mycursor.execute(quary)
            except:
                mycursor.execute('use userdata')
            quary='insert into connect_pin(username,pin) values(%s,%s)'
            mycursor.execute(quary,(user1_name_entry.get(),confirm_pin_name_entry.get()))
            mb.showinfo('success','Pin set successful\nNow the program will be automatically closed you only need to reopen again. Thank you.',parent=database_window)

            user1_name_entry.delete(0,END)
            pin_name_entry.delete(0,END)
            confirm_pin_name_entry.delete(0,END)
            database.commit()
            database.close()
            database_window.destroy()
            # welcome()
        

    def connect():
        global count
        def clear():
            host_name_entry.delete(0,END)
            user_name_entry.delete(0,END)
            password_name_entry.delete(0,END)
        try:
            if user_name_entry.get()=='' or password_name_entry.get()=='':
                messagebox.showerror('Error','Enter your details first',parent=database1)
            else:
                try:
                    mydb=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='userdata')
                    mycursor=mydb.cursor()
                except:
                    messagebox.showerror('Error','Database connection issue please try again later',parent=database1)
                quary='use userdata'
                mycursor.execute(quary)
                quary='select * from connect_pin where username=%s and pin=%s'
                mycursor.execute(quary,(user_name_entry.get(),password_name_entry.get(),))
            

                row=mycursor.fetchone()

            

                if row==None:
                    if count==0:
                        messagebox.showerror('Error','Too many attempts,System blocked.\nTo unlock,you must provide the three garantees unique numbers',parent=database1)
                        # connection_btn.config(text='unblock')
                        database1.destroy()
                        root.destroy()
                        def unlock():
                            if lbl1_entry.get()!='' or lbl2_entry.get()!='' or lbl3_entry.get()!='':
                                block_window.destroy()
                                pin_window()
                            else:
                                messagebox.showerror('Error','All the three unique numbers are required',parent=block_window)
                        block_window=Tk()
                        block_window.title('System Blocked')
                        block_window.geometry('1350x723+10+10')
                        block_window.resizable(False,False)

                        lbl1=Label(block_window,text='Unlock the system by filling the form below*',font=('arial 15 bold'),fg='red')
                        lbl1.place(x=400,y=15)

                        lbl1_=Label(block_window,text='Gurantor 1*',font=('arial 15 bold'),fg='blue')
                        lbl1_.place(x=150,y=40)

                        lbl1_entry=Entry(block_window,font=('arial 18 bold'),width=20)
                        lbl1_entry.place(x=150,y=100)

                        lbl2=Label(block_window,text='Gurantor 2*',font=('arial 15 bold'),fg='blue')
                        lbl2.place(x=150,y=180)

                        lbl2_entry=Entry(block_window,font=('arial 18 bold'),width=20)
                        lbl2_entry.place(x=150,y=240)

                        lbl3=Label(block_window,text='Gurantor 3*',font=('arial 15 bold'),fg='blue')
                        lbl3.place(x=150,y=340)

                        lbl3_entry=Entry(block_window,font=('arial 18 bold'),width=20)
                        lbl3_entry.place(x=150,y=440)

                        unlock_btn=Button(block_window,text='UNLOCK',font=('arial 20 bold'),bg='lime green',fg='black',command=unlock)
                        unlock_btn.place(x=500,y=600)


                        block_window.mainloop()
                    else:
                        count-=1
                        messagebox.showerror('Error','Incorrect username/pin',parent=database1)
                        # database1.configure(title='System blocked')
                        # database1.configure(geometry='1350x723+10+10')
                   
                    
                        
                else:
                    messagebox.showinfo('Welcome','Login is successful',parent=database1)
                    addbtn.config(state=ACTIVE,bg='light coral')
                    updatebtn.config(state=ACTIVE,bg='lime green')
                    searchbtn.config(state=ACTIVE,bg='gold')
                    deletebtn.config(state=ACTIVE,bg='red')
                    show_stbtn.config(state=ACTIVE,bg='yellow')
                    export_databtn.config(state=ACTIVE,bg='blue')
                    clear()
                    database1.destroy()
        except Exception as e:
            messagebox.showerror('Error',f'{e} error occured during the proccess',parent=database1)


    def database_connect():
        global database1,connection_btn,user_name_entry,password_name_entry,host_name_entry,count
        
        database1=Toplevel()
        database1.title('connect to database')
        database1.geometry('350x280+800+130')
        database1['background']='white'
        database1.resizable(False,False)
        count=5
        #         messagebox.showerror('error','Something went wrong.. please try again')
        host_label=Label(database1,text='Host name:',bg='white',font=('calibri 14 bold'))
        host_label.place(x=10,y=40)

        host_name_entry=Entry(database1,font=('calibri 14 bold'))
        host_name_entry.place(x=120,y=40)

        user_name_entry=Entry(database1,font=('calibri 14 bold'))
        user_name_entry.place(x=120,y=100)

        password_name_entry=Entry(database1,font=('calibri 14 bold'))
        password_name_entry.place(x=120,y=160)



        Username_label=Label(database1,text='Username:',bg='white',font=('calibri 14 bold'))
        Username_label.place(x=10,y=100)

        password_label=Label(database1,text='Password:',bg='white',font=('calibri 14 bold'))
        password_label.place(x=10,y=160)

        connection_btn=Button(database1,text='Connect',bg='coral',activebackground='coral',activeforeground='black',width=15,height=1,font=('Batang 11'),command=connect)
        connection_btn.place(x=100,y=230)

        database1.mainloop()

    def database_logout():
    
        ans=messagebox.askyesno('confirmation','Database logout?')
        if ans:
            addbtn.config(state=DISABLED)
            updatebtn.config(state=DISABLED)
            searchbtn.config(state=DISABLED)
            deletebtn.config(state=DISABLED)
            show_stbtn.config(state=DISABLED)
            export_databtn.config(state=DISABLED)
            messagebox.showinfo('success','Database connection terminated')
            tree.delete(*tree.get_children())

    def show_st():
        mydb2=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='students_detail')
        mycursor2=mydb2.cursor()
        quary='select * from students_data'
        mycursor2.execute(quary)
        rows=mycursor2.fetchall()
        tree.delete(*tree.get_children())
        for data in rows:
            tree.insert('',END,values=data)
    def export_st():
        url=filedialog.asksaveasfilename(defaultextension='.csv')
        indexing=tree.get_children()
        newlist=[]
        for data in indexing:
            content=tree.item(data)
            datalist=content['values']
            # print(datalist)
            newlist.append(datalist)
        # print(newlist)
        table=pandas.DataFrame(newlist,columns=['Id','first_name','second_name','surname','age','gender','form','D.O.B','UPI_number','ADM_number','religion','disability','parent/gurdian_name',
            'phone_number','address','occupation','city','ADDED DATE','TIME STAMP'])
        table.to_csv(url,index=False,sep='\t')
        messagebox.showinfo("Success",'Data is saved succeffully')

    def exit1():
        ans=messagebox.askyesno('confirmation','Do you want quit?')
        if ans:
            root.destroy()

    def cur_time():
        global date,current_time
        date=time.strftime('%d/%m/%Y')
        current_time=time.strftime('%H:%M:%S')
        datelabel.config(bg='dark olive green',text=f'   Date:{date}\nTime:{current_time}')
        datelabel.after(1000,cur_time)
    # def slider():
    def slider(text,n=0):
        if n < len(text)-1:
            stdlabel.after(300,slider,text,n+1)
        else:
            slider(text,n=0)
        stdlabel['text']=text[:n+1]

        # root.after(1000,animate_label,txt)
    root=Tk()
    root.geometry('1350x723+10+10')
    root.resizable(False,False)
    root['background']='dark olive green'
    root.title('school system')
    #

    titl1='Students Management System'
    columns=('Id','first_name','second_name','surname','age','gender','form','D.O.B','UPI_number','ADM_number','religion','disability','parent/gurdian_name',
            'phone_number','address','occupation','city','ADDED DATE','TIME STAMP')
    # 
    titleframe=Frame(root,width=1200,height=100,bg='dark olive green')
    titleframe.pack(side=TOP)

    datelabel=Label(titleframe,font=('aerial 19 bold'))
    datelabel.place(y=3,x=2)
    cur_time()

    stdlabel=Label(titleframe,text=titl1,width=30,bg='hot pink',font=('aerial 26 italic bold'))
    stdlabel.place(x=290,y=20)
    slider('Students Management System')

    connectbtn=Button(titleframe,bd=7,text='Connect to database',bg='olive drab',activebackground='coral',activeforeground='black',width=16,height=1,font=('Batang 11 bold'),command=database_connect)
    connectbtn.place(x=1040,y=61)


    btnframe=Frame(root,width=340,height=700,bg='white',bd=7)
    btnframe.pack(side=LEFT,fill=X)

    img=ImageTk.PhotoImage(file='pupil.jpg')
    label=Label(btnframe,image=img,bg='white')
    label.place(x=120,y=50)

    addbtn=Button(btnframe,bd=7,text='Add student',state=DISABLED,bg='coral',cursor='hand2',width=25,height=1,font=('Batang 11 bold'),command=lambda:toplevel('Add Students','Add',register1))
    addbtn.place(x=40,y=140)

    searchbtn=Button(btnframe,bd=7,text='Search student',state=DISABLED,cursor='hand2',bg='coral',width=25,height=1,font=('Batang 11 bold'),command=lambda:toplevel('Search Students','Search',search_data))
    searchbtn.place(x=40,y=210)

    updatebtn=Button(btnframe,bd=7,text='Update details',state=DISABLED,cursor='hand2',bg='coral',width=25,height=1,font=('Batang 11 bold'),command=lambda:toplevel('Update Students','Update',update_details))
    updatebtn.place(x=40,y=290)

    show_stbtn=Button(btnframe,bd=7,text='Show students',state=DISABLED,cursor='hand2',bg='coral',width=25,height=1,font=('Batang 11 bold'),command=show_st)
    show_stbtn.place(x=40,y=360)

    export_databtn=Button(btnframe,bd=7,text='Export data',state=DISABLED,cursor='hand2',bg='coral',width=25,height=1,font=('Batang 11 bold'),command=export_st)
    export_databtn.place(x=40,y=415)

    deletebtn=Button(btnframe,bd=7,text='Delete student',state=DISABLED,cursor='hand2',bg='coral',width=25,height=1,font=('Batang 11 bold'),command=delete_student)
    deletebtn.place(x=40,y=475)

    exitbtn=Button(btnframe,bd=7,text='Exit',bg='coral',cursor='hand2',width=25,height=1,font=('Batang 11 bold'),command=exit1)
    exitbtn.place(x=40,y=540)

    connectbtn=Button(btnframe,bd=0,text='Database log_out',bg='white',fg='blue',width=15,height=1,font=('Batang 11 bold underline'),command=database_logout)
    connectbtn.place(x=2,y=2)

    # boxframe=Frame(root,width=850,height=590)
    # boxframe.place(x=340,y=100)
    horizontal_scroll=Scrollbar(root,orient=HORIZONTAL)
    horizontal_scroll.pack(side=BOTTOM,fill=X)#place(x=1180,y=100)
    vertical_scroll=Scrollbar(root,orient=VERTICAL)
    vertical_scroll.pack(side=RIGHT,fill=Y)#place(x=1180,y=100)


    style=ttk.Style()
    style.theme_use('clam')
    style.configure('tree',background='black',fieldbackground='black',foreground='white')
    style.configure('tree.Headings',background='PowerBlue')
    style.configure('tree.Headings',font=('arial',18,'bold'))
    style.configure('TreeView',rowheight=60,font=('arial',16,'bold'))

    tree=ttk.Treeview(root,columns=columns,show='headings',height=100,
                    xscrollcommand=horizontal_scroll.set,yscrollcommand=vertical_scroll.set)
    tree.pack(fill=BOTH,expand=1)
    vertical_scroll.config(command=tree.yview)
    horizontal_scroll.config(command=tree.xview)
    # textbox.place(x=250,y=100)

    tree.heading('Id',text='ID')
    tree.heading('first_name',text='FIRST_NAME')
    tree.heading('second_name',text='SECOND_NAME')
    tree.heading('surname',text='SURNAME')
    tree.heading('age',text='AGE')
    tree.heading('gender',text='GENDER')
    tree.heading('form',text='FORM')
    tree.heading('D.O.B',text='D.O.B')
    tree.heading('UPI_number',text='UPI_NUMBER')
    tree.heading('ADM_number',text='ADM_NUMBER')
    tree.heading('religion',text='RELIGION')
    tree.heading('disability',text='DISABILITY')
    tree.heading('parent/gurdian_name',text='PARENT/GURDIAN NAME')
    tree.heading('phone_number',text='PHONE_NUMBER')
    tree.heading('address',text='ADDRESS')
    tree.heading('occupation',text='OCCUPATION')
    tree.heading('city',text='TOWN/CITY')
    tree.heading('ADDED DATE',text='ADDED DATE')
    tree.heading('TIME STAMP',text='TIME STAMP')

    tree.column('Id',width=50,anchor=CENTER)
    tree.column('first_name',width=200,anchor=CENTER)
    tree.column('second_name',width=200,anchor=CENTER)
    tree.column('surname',width=150,anchor=CENTER)
    tree.column('age',width=50,anchor=CENTER)
    tree.column('gender',width=100,anchor=CENTER)
    tree.column('form',width=50,anchor=CENTER)
    tree.column('D.O.B',width=150,anchor=CENTER)
    tree.column('UPI_number',width=150,anchor=CENTER)
    tree.column('ADM_number',width=150,anchor=CENTER)
    tree.column('religion',width=150,anchor=CENTER)
    tree.column('disability',width=150,anchor=CENTER)
    tree.column('parent/gurdian_name',width=250,anchor=CENTER)
    tree.column('phone_number',width=150,anchor=CENTER)
    tree.column('address',width=100,anchor=CENTER)
    tree.column('occupation',width=150,anchor=CENTER)
    tree.column('city',width=100,anchor=CENTER)
    tree.column('ADDED DATE',width=150,anchor=CENTER)
    tree.column('TIME STAMP',width=150,anchor=CENTER)

    style=ttk.Style()
    style.configure('Treeview',rowheight=30,font=('arial',11,'bold'),background='brown',foreground='white',fieldbackground='coral')
    style.configure('Treeview.Heading',font=('Cooper Black',10,'bold'),foreground='medium blue')



    root.mainloop()

def welcome():
    welcoming_page.destroy()     

    login_window=Tk()
    login_window.geometry('1350x723+0+0')
    login_window.resizable(False,False)
    login_window.title('Login form')


    def createnew():

            
        createacc=Toplevel()
        createacc.title('Create new account')
        createacc.geometry('1350x723+0+0')
        createacc.minsize(width=800,height=438)
        createacc.resizable(0,0)
        # login_window.destroy()
        # createacc.after(1000,login_window.destroy)


        img=ImageTk.PhotoImage(file='bgg3.jpg')
        label=Label(createacc,image=img)
        label.place(x=0,y=0)
        check=IntVar()
        def clear():
            emailentry.delete(0,END)
            usernameentry.delete(0,END)
            passwordentry33.delete(0,END)
            confirmpasswordentry.delete(0,END)
            check.set(0)
        def backto_login():
            createacc.destroy()
        def database(): 
            ##if else statments##
            if emailentry.get()=='' or emailentry.get()=='Email' or userentry.get()=='' or userentry.get()=='Username' or passwordentry33.get()=='' or passwordentry33.get()=='Password' or confirmpasswordentry.get()=='' or confirmpasswordentry.get()=='Confirm password':

                messagebox.showerror('Error','All fields are required',parent=createacc)
            elif passwordentry33.get()!= confirmpasswordentry.get():
                messagebox.showerror('Error','Password mismatch',parent=createacc)

            elif check.get()==0:
                messagebox.showerror('Error','Please accept to our terms & conditions',parent=createacc)
            else:
                try:
                    mydb=mysql.connector.connect(host='localhost',username='agwora',password='@brayo2884.2023')
                    mycursor=mydb.cursor()
                except:
                    messagebox.showerror('Error','Database connection issues, Please try again',parent=createacc)
                    return
                try:
                    quary='create database userdata'
                    mycursor.execute(quary)

                    quary='use userdata'
                    mycursor.execute(quary)


                    quary='create table login_data1(Id int auto_increment primary key not null,email_address varchar(50) not null,username varchar(30) not null,password varchar(30) not null)'
                    mycursor.execute(quary)
                except:
                    mycursor.execute('use userdata')
                    
                quary='select * from login_data1 where username=%s'
                mycursor.execute(quary,(usernameentry.get(),))

                row=mycursor.fetchone()
                if row !=None:
                    messagebox.showerror('Error','username Already exists',parent=createacc)
                else:
                    # mycursor.execute(quary)
                    quary='insert into login_data1(email_address,username,password) values(%s,%s,%s)'
                    mycursor.execute(quary,(emailentry.get(),usernameentry.get(),passwordentry33.get()))
                    mydb.commit()
                    mydb.close()

                    messagebox.showinfo('success','account is created successful',parent=createacc)
                    clear()

                    def connect():
                        if user_name_entry.get()=='' or  pin_name_entry.get()=='' or confirm_pin_name_entry.get()=='':
                            mb.showerror("Error",'All entries are required',parent=database_window)

                        elif pin_name_entry.get()!=confirm_pin_name_entry.get():
                            mb.showerror('Error','Pin must be the same',parent=database_window)
                        else:
                            try:
                                database=connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='userdata')
                                mycursor=database.cursor()
                            except:
                                mb.showerror('Error','Database connection issues, try again later')
                            try:
                                quary='create table connect_pin(id int auto_increment primary key,username varchar(50),pin varchar(20))'
                                mycursor.execute(quary)
                            except:
                                mycursor.execute('use userdata')
                            quary='insert into connect_pin(username,pin) values(%s,%s)'
                            mycursor.execute(quary,(user_name_entry.get(),confirm_pin_name_entry.get()))
                            mb.showinfo('success','Pin set successful',parent=database_window)
                            user_name_entry.delete(0,END)
                            pin_name_entry.delete(0,END)
                            confirm_pin_name_entry.delete(0,END)
                            database.commit()
                            database.close()
                            database_window.destroy()
                            createacc.destroy()
                    # def pin_window():
                    global database_window,confirm_pin_label,confirm_pin_name_entry,pin_name_entry
                    database_window=Toplevel()
                    database_window.title('Connect pin set')
                    database_window.grab_set()
                    database_window.geometry('400x300+400+200')
                    database_window.resizable(False,False)
                    host=StringVar()
                    host.set('Localhost')


                    _label=Label(database_window,text='The pin will be used to activate the buttons in the system*\nmemorize it clearly',font=('calibri 10 bold'))
                    _label.place(x=10,y=5)

                    host_label=Label(database_window,text='Host name:',font=('calibri 14 bold'))
                    host_label.place(x=10,y=50)

                    host_name_entry=Entry(database_window,textvariable=host,font=('calibri 14 bold'))
                    host_name_entry.place(x=120,y=50)

                    user_name_entry=Entry(database_window,font=('calibri 14 bold'))
                    user_name_entry.place(x=120,y=100)

                    pin_name_entry=Entry(database_window,font=('calibri 14 bold'))
                    pin_name_entry.place(x=120,y=160)



                    Username_label=Label(database_window,text='Username:',font=('calibri 14 bold'))
                    Username_label.place(x=10,y=100)

                    pin_label=Label(database_window,text='Pin:',font=('calibri 14 bold'))
                    pin_label.place(x=10,y=160)

                    confirm_pin_label=Label(database_window,text='Confirm Pin:',font=('calibri 14 bold'))
                    confirm_pin_label.place(x=10,y=190)

                    confirm_pin_name_entry=Entry(database_window,font=('calibri 14 bold'))
                    confirm_pin_name_entry.place(x=120,y=190)

                    connection_btn=Button(database_window,text='Set',bg='coral',activebackground='coral',activeforeground='black',width=15,height=1,font=('Batang 11'),command=connect)
                    connection_btn.place(x=100,y=250)

                    database_window.mainloop()
                    
                    Username_label=Label(database_window,text='Username:',bg='white',font=('calibri 14 bold'))
                    Username_label.place(x=10,y=100)

                    pin_label=Label(database_window,text='Pin:',bg='white',font=('calibri 14 bold'))
                    pin_label.place(x=10,y=160)

                    connection_btn=Button(database_window,text='Connect',bg='coral',activebackground='coral',activeforeground='black',width=15,height=1,font=('Batang 11'),command=connect)
                    connection_btn.place(x=100,y=230)

                    database_window.mainloop()
                    createacc.destroy()
            


        def delete_email1(event):
            if emailentry.get()=="Email":
                emailentry.delete(0,END)
        def delete_username1(event):
            if usernameentry.get()=="Username":
                usernameentry.delete(0,END)
        def delete_password1(event):
            if passwordentry33.get()=="Password":
                passwordentry33.delete(0,END)
        def delete_confirmpassword1(event):
            if confirmpasswordentry.get()=="Confirm password":
                confirmpasswordentry.delete(0,END)


        # createacc=Tk()
        # createacc.withdraw()


        frame1=Frame(createacc,bg='white',width=350,height=428,pady=20)
        crtlbl=Label(frame1,text='Create acccount',bg='white',fg='firebrick1',font=("Calibri 26 bold"))
        crtlbl.place(x=60,y=5)

        emailentry=Entry(frame1,bd=0,font=("Calibri 16"))
        emailentry.place(x=40,y=60)
        emailframe=Frame(frame1,width=200,height=2,bg="firebrick1")
        emailframe.place(x=40,y=90)
        emailentry.insert(0,'Email')
        emailentry.bind('<FocusIn>',delete_email1)

        usernameentry=Entry(frame1,bd=0,font=("Calibri 16"))
        usernameentry.place(x=40,y=120)
        usernameframe=Frame(frame1,width=200,height=2,bg="firebrick1")
        usernameframe.place(x=40,y=150)
        usernameentry.insert(0,'Username')
        usernameentry.bind('<FocusIn>',delete_username1)



        passwordentry33=Entry(frame1,bd=0,font=("Calibri 16"))
        passwordentry33.place(x=40,y=180)
        passwordframe=Frame(frame1,width=200,height=2,bg="firebrick1")
        passwordframe.place(x=40,y=210)
        passwordentry33.insert(0,'Password')
        passwordentry33.bind('<FocusIn>',delete_password1)



        confirmpasswordentry=Entry(frame1,bd=0,font=("Calibri 16"))
        confirmpasswordentry.place(x=40,y=240)
        confirmpasswordframe=Frame(frame1,width=200,height=2,bg="firebrick1")
        confirmpasswordframe.place(x=40,y=270)
        confirmpasswordentry.insert(0,'Confirm password')
        confirmpasswordentry.bind('<FocusIn>',delete_confirmpassword1)

        checkbox=Checkbutton(frame1,
                            variable=check, fg='blue',bg='white',font=('Calibri 12 bold underline'))
        checkbox.place(x=60,y=285)

        checkboxlbl=Label(frame1, text='I agree to terms and conditions..'
        ,bg='white',fg='firebrick1',font=("Calibri 11"))
        checkboxlbl.place(x=80,y=285)


        btnn=Button(frame1,text='SUBMIT',width=25,height=1,bg='lightblue',fg='green',activebackground='lightblue',activeforeground='green',bd=0,font=('Calibri 14 bold'),command=database)
        btnn.place(x=60,y=315)

        acclbl=Label(frame1,text='Do you have an account?',bg='white',fg='firebrick1',font=("Calibri 11"))
        acclbl.place(x=40,y=360)

        btnn2=Button(frame1,text='Log in',width=7,height=1,bg='white',fg='blue',activebackground='white',activeforeground='blue',bd=0,font=('Calibri 12 bold underline'),command=backto_login)
        btnn2.place(x=200,y=360)


        # btn2.config()
        frame1.place(x=550,y=70)
        createacc.mainloop()




    def forgot_pass():
        def reset():
            def clear():
                username_entry.delete(0,END)
                passwordentry.delete(0,END)
                passwordentry1.delete(0,END)
            if username_entry.get()=='' or passwordentry.get()=='' or passwordentry1.get()=='':
                messagebox.showerror('Error','All fields are required',parent=reset1)
            elif passwordentry.get()!= passwordentry1.get():
                messagebox.showerror('Error','Password missmatch',parent=reset1)
            else:
                ##database connection for reset##
                try:
                    mydb2=mysql.connector.connect(host='localhost',username='agwora',password='@brayo2884.2023',database='userdata')
                    mycursor2=mydb2.cursor()
                except:
                    messagebox.showerror('Error','database connection issue...Please try again',parent=reset1)
                    return
                quary='use userdata'
                mycursor2.execute(quary)
                quary='select * from login_data1 where username=%s'
                mycursor2.execute(quary,(username_entry.get(),))
                row=mycursor2.fetchone()
                if row==None:
                    messagebox.showerror('Error','Wrong username',parent=reset1)
                else:
                    quary='update login_data1 set password=%s where username=%s'
                    mycursor2.execute(quary,(passwordentry1.get(),username_entry.get()))
                    mydb2.commit()
                    mydb2.close()
                    messagebox.showinfo('success','Password is successfully reset',parent=reset1)
                    clear()
                    reset1.destroy()
                


                
            
        reset1=Toplevel()
        reset1.title('Reset password')
        reset1.geometry('1350x723+0+0')
        reset1.resizable(False,False)

        img3=ImageTk.PhotoImage(file='bgg2.jpg')
        labelll=Label(reset1,image=img3)
        labelll.place(x=0,y=0)

        frame2=Frame(reset1,bg='white',width=350,height=450,pady=20)

        label1=Label(frame2,text='Reset password',bg='white',fg='firebrick1',font=("calibri",28,"bold"))
        label1.place(x=40,y=0)

        label1=Label(frame2,text='Username',bg='white',fg='firebrick1',font=("calibri",16))
        label1.place(x=40,y=40)

        username_entry=Entry(frame2,bd=1,font=("Aerial 14 "))
        username_entry.place(x=40,y=70)

        label1=Label(frame2,text='New password',bg='white',fg='firebrick1',font=("calibri",16))
        label1.place(x=40,y=110)

        passwordentry=Entry(frame2,bd=1,font=("Aerial 14 "))
        passwordentry.place(x=40,y=140)

        label1=Label(frame2,text='confirm password',bg='white',fg='firebrick1',font=("calibri",16))
        label1.place(x=40,y=180)

        passwordentry1=Entry(frame2,bd=1,font=("Aerial 14 "))
        passwordentry1.place(x=40,y=210)

        bttn=Button(frame2,text='Reset',width=20,activebackground='firebrick1',activeforeground='white',bg='firebrick1',fg='white',font=("Calibri 18 bold"),command=reset)
        bttn.place(x=50,y=300)
        frame2.place(x=450,y=70)

        reset1.mainloop()


    def Pass():

        def clear():
            userentry.delete(0,END)
            Passwordentry44.delete(0,END)
        

        
        if userentry.get()=='username' or userentry.get()=='' or Passwordentry44.get=='password' or Passwordentry44.get()=='':
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                mydb1=mysql.connector.connect(host='localhost',user='agwora',password='@brayo2884.2023',database='userdata')
                mycursor1=mydb1.cursor()
            except:
                messagebox.showerror('Error','Database connection issue,,Please try again')
                return
            quary='use userdata'
            mycursor1.execute(quary)
            quary='select * from login_data1 where username=%s and password=%s'
            mycursor1.execute(quary,(userentry.get(),Passwordentry44.get()))
            row=mycursor1.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect username/password')
            else:
                messagebox.showinfo('Welcome','Login is successful')
                clear()
                login_window.destroy()
                system()


            #
                


    def delete_user(event):
        if userentry.get()=="username":
            userentry.delete(0,END)

    def delete_Password(event):
        if Passwordentry44.get()=="password":
            Passwordentry44.delete(0,END)




    imgg2=ImageTk.PhotoImage(file='closedeye.jpg')
    imgg1=ImageTk.PhotoImage(file='openeye.jpg')
    def hide():
        def open():
            Passwordentry44.config(show='')
            openbtn.config(image=imgg1,command=hide)

        Passwordentry44.config(show="*")
        openbtn.config(image=imgg2,command=open)
        



    # ge(x=0,y=0)

    
    imgg3=ImageTk.PhotoImage(file='login_pic.jpg')
    openbtn=Button(login_window,image=imgg3,bd=0,bg='white',command=hide)
    openbtn.place(x=0,y=0)

    frame0=Frame(login_window,bg='white',width=350,height=400)
    label1=Label(frame0,text='User login',bg='white',fg='firebrick1',font=("calibri",28,"bold"))
    label1.place(x=70,y=20)

    userentry=Entry(frame0,fg='firebrick1',bd=0,font=("calibri",16),width=25,cursor='hand2')
    userentry.place(x=50,y=80)

    userentry.insert(0,'username')#,font=("calibri",11))
    userentry.bind('<FocusIn>',delete_user)#,font=("calibri",11),fg='firebrick1')

    Passwordentry44=Entry(frame0,bd=0,fg='firebrick1',font=("calibri",16),cursor='hand2',width=25)
    Passwordentry44.place(x=50,y=130)

    imgg=ImageTk.PhotoImage(file='openeye.jpg')
    openbtn=Button(frame0,image=imgg,bd=0,bg='white',command=hide)
    openbtn.place(x=250,y=125)

    Passwordentry44.insert(0,'password' )#,font=("calibri",11))
    Passwordentry44.bind('<FocusIn>',delete_Password)#,font=("calibri",11),fg='firebrick1')

    frame=Frame(frame0,width=200,height=3,bg='firebrick1')
    frame.place(x=50,y=105)

    frame1=Frame(frame0,width=200,height=3,bg='firebrick1')
    frame1.place(x=50,y=155)

    btnn2=Button(frame0,text='Forgot Password?',bd=0,bg='white',fg='blue',activebackground='white',activeforeground='blue',font=("calibri",11),command=forgot_pass)
    btnn2.place(x=160,y=165)

    btn=Button(frame0,text='Login',activebackground='firebrick1',activeforeground='white',bg='firebrick1',fg='white',width=23,height=1,font=("calibri 16 bold"),command=Pass)
    btn.place(x=48,y=200)

    label2=Label(frame0,text='-----------OR-----------',bg='white',fg='firebrick1',font=("calibri",18,"bold"))
    label2.place(x=78,y=250)

    twiterimg=ImageTk.PhotoImage(file='twiter.jpg')
    twiterlbl=Button(frame0,activebackground='white',image=twiterimg,bg='white',bd=0)
    twiterlbl.place(x=48,y=285)

    fbimg=ImageTk.PhotoImage(file='fb.jpg')
    fblbl=Button(frame0,activebackground='white',image=fbimg,bg='white',bd=0)
    fblbl.place(x=124,y=285)

    instaimg=ImageTk.PhotoImage(file='insta.jpg')
    instalbl=Button(frame0,activebackground='white',image=instaimg,bg='white',bd=0)
    instalbl.place(x=204,y=285)

    label1=Label(frame0,text="Don't have an account?",bg='white',fg='firebrick1',font=("calibri",13))
    label1.place(x=48,y=350)

    btn1=Button(frame0,text='create new',activebackground='white',bd=0,activeforeground='blue',bg='white',fg='blue',width=10,height=1,font=("calibri" ,13, "underline"),command=createnew)
    btn1.place(x=220,y=350)


    frame0.place(x=550,y=100)
    login_window.mainloop()

from tkinter import *
import tkinter.ttk as ttk
from time import time


def func():
    pass
def slider(text,n=0):
    if n < len(text)-1:
        labe.after(150,slider,text,n+1)
    else:
        slider(text,n=0)
    labe['text']=text[:n+1]

def welcome2():
    global welcoming_page
    root.destroy()
    welcoming_page=Tk()
    welcoming_page.title('Welcome To our School System')
    welcoming_page.geometry('1350x723+0+0')
    welcoming_page.resizable(False,False)


    # icon_img=BitmapImage(file='graduates_icon.png')
    # Label(welcoming_page,image=icon_img).place()


    canvas=Canvas(welcoming_page,height=723,width=1350)
    canvas.pack()

    # image1=ImageTk.PhotoImage(file='welcome.jpg')
    # label11=canvas.create_image((680,300),image=image1)

    label12=canvas.create_text((600,250),text='Welcome To Our School System..\n\n\n         Empowering knowledge',font=('Helvetica',44,'bold'),fill='blue')
    label13=canvas.create_text((200,650),text='Powered by: AOB\nYear: @2023',font=("Helvetica",24,'bold'),fill='green')

    button1=Button(welcoming_page,text='Continue',font=('Helvetica',24,'bold'),fg='green',activebackground='green',command=welcome)
    button1.place(x=1000,y=610)

    welcoming_page.mainloop()

root=Tk()
root.geometry('1350x723+10+10')
root.resizable(0,0)
# root.overrideredirect=True
root.title(' System Loading...')
text='...'
text2='Loading'
root.grab_set()

# img2023=ImageTk.PhotoImage(file='loading.png')
# load_img=Label(root,image=img2023)
# load_img.place(x=0,y=0)


labe=Label(root,text=text2+text,width=15,bg='gold',fg='olivedrab',font='colosal 44 bold')
labe.pack()
label=Label(root,text='Please wait a minute',fg='orchid',bg='black',font='colosal 26')
label.pack(side='bottom')
slider('.....')

pb=ttk.Progressbar(root,maximum=7.001)
pb.pack(padx=50,pady=50)
pb.start(1000)


root.after(7000,func=welcome2)
root.mainloop()

