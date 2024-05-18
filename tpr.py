from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
       self.root=root
       self.root.geometry("900x500+200+50")
       self.root.title("QR Generator | Developed by Abhinav")
       self.root.resizable(False,False)

       title=Label(self.root,text="   QR Code Generator",font=("times new roman",40),bg='#053246',fg='white',anchor='w' ).place(x=0,y=0,relwidth=1)

       #====Details window=======
       #====Variables=====
       self.var_student_code=StringVar()
       self.var_name=StringVar()
       self.var_fathername=StringVar()
       self.var_course=StringVar()
       self.var_DOB=StringVar()
      
       student_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
       student_Frame.place(x=50,y=100,width=500,height=380)

       student_title=Label(student_Frame,text="   Student Details",font=("goudy old style",20),bg='#043256',fg='white',anchor='w' ).place(x=0,y=0,relwidth=1)

       lbl_student_code=Label(student_Frame,text="STUDENT ID",font=("times new roman",15,'bold'),bg='white',anchor='w' ).place(x=20,y=60)
       lbl_name=Label(student_Frame,text="STUDENT NAME",font=("times new roman",15,'bold'),bg='white',anchor='w' ).place(x=20,y=100)
       lbl_fathername=Label(student_Frame,text="FATHER'S NAME",font=("times new roman",15,'bold'),bg='white',anchor='w' ).place(x=20,y=140)
       lbl_course=Label(student_Frame,text="COURSE",font=("times new roman",15,'bold'),bg='white',anchor='w' ).place(x=20,y=180)
       lbl_DOB=Label(student_Frame,text="DATE OF BIRTH",font=("times new roman",15,'bold'),bg='white',anchor='w' ).place(x=20,y=220)

       txt_student_code=Entry(student_Frame,font=("times new roman",15),textvariable=self.var_student_code,bg='lightyellow').place(x=200,y=60)
       txt_name_code=Entry(student_Frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=100)
       txt_fathername_code=Entry(student_Frame,font=("times new roman",15),textvariable=self.var_fathername,bg='lightyellow').place(x=200,y=140)
       txt_course_code=Entry(student_Frame,font=("times new roman",15),textvariable=self.var_course,bg='lightyellow').place(x=200,y=180)
       txt_DOB_code=Entry(student_Frame,font=("times new roman",15),textvariable=self.var_DOB,bg='lightyellow').place(x=200,y=220)

       btn_generate=Button(student_Frame,text='QR Generate',command=self.generate,font=("times new roman",18,'bold'),bg='#2196f3',fg='white').place(x=90,y=280,width=180,height=30)
       btn_clear=Button(student_Frame,text='Clear',command=self.clear,font=("times new roman",18,'bold'),bg='#607d8b',fg='white').place(x=282,y=280,width=120,height=30)
       
       self.msg=''
       self.lbl_msg=Label(student_Frame,text=self.msg,font=("times new roman",20),bg='white',fg='green')
       self.lbl_msg.place(x=0,y=330,relwidth=1)

       #====QR Code window=======
       qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
       qr_Frame.place(x=600,y=100,width=250,height=380)

       Student_title=Label(qr_Frame,text="   Student QR Code",font=("goudy old style",20),bg='#043256',fg='white',anchor='w' ).place(x=0,y=0,relwidth=1)

       self.qr_code=Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white')
       self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_student_code.set('')
        self.var_name.set('')
        self.var_fathername.set('')
        self.var_course.set('')
        self.var_DOB.set('')
        self.msg=''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
           if self.var_course.get()=='' or self.var_DOB.get()=='' or self.var_fathername.get()=='' or self.var_name.get()=='' or self.var_student_code.get()=='':
              self.msg='All Fields are Required!!!'
              self.lbl_msg.config(text=self.msg,fg='red')
           else:
              qr_data=(f"Student ID: {self.var_student_code.get()}\nStudent Name: {self.var_name.get()}\nCourse: {self.var_course.get()}\nFathername: {self.var_fathername.get()}\nDOB: {self.var_DOB.get()}")
              qr_code=qrcode.make(qr_data)
              # print(qr_code) 
              qr_code=resizeimage.resize_cover(qr_code,[180,180])
              qr_code.save("QR_GENERATOR"+str(self.var_student_code.get())+'.png')
              #======QR Code Image Update========
              self.im=ImageTk.PhotoImage(file="QR_GENERATOR"+str(self.var_student_code.get())+'.png')
              self.qr_code.config(image=self.im)
              #======updating Notification=======
              self.msg='QR Generated Successfully!!!'
              self.lbl_msg.config(text=self.msg,fg='green')

root=Tk()
obj =Qr_Generator(root)
root.mainloop()
