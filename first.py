from tkinter import *

root=Tk()
root.title("Calculator")

root.configure(bg='pink')

#Taking input
e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#palceholder
def btn(number):
  ct=e.get()
  e.delete(0,END)
  e.insert(0,str(ct) + str(number))
  
def btn_cl() :
  e.delete(0,END)

def btn_el() :
  sn=e.get()
  e.delete(0,END)
  if math == "addition":
    e.insert(0,f_num+ int(sn))
    
  if math == "substraction":
    e.insert(0,f_num - int(sn))
    
  if math == "multiplication":
    e.insert(0,f_num * int(sn))
    
  if math == "division":
    e.insert(0,f_num / int(sn))
      
  if math == "module":
    e.insert(0,f_num % int(sn))
      
def btn_add():
  fn=e.get()
  global f_num
  global math
  math="addition"
  f_num=int(fn)
  e.delete(0,END)
    
def btn_subl():
  fn=e.get()
  global f_num
  global math
  math="substraction"
  f_num=int(fn)
  e.delete(0,END)
  
def btn_mul() :
  fn=e.get()
  global f_num
  global math
  math="multiplication"
  f_num=int(fn)
  e.delete(0,END)
  
def btn_divide() :
  fn=e.get()
  global f_num
  global math
  math="division"
  f_num=int(fn)
  e.delete(0,END)
  
def btn_module() :
  fn=e.get()
  global f_num
  global math
  math="module"
  f_num=int(fn)
  e.delete(0,END)
  

b1=Button(root,text='1',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(1))

b2=Button(root,text='2',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(2))

b3=Button(root,text='3',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(3))

b4=Button(root,text='4',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(4))

b5=Button(root,text='5',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(5))

b6=Button(root,text='6',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(6))

b7=Button(root,text='7',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(7))

b8=Button(root,text='8',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(8))

b9=Button(root,text='9',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(9))

b0=Button(root,text='0',padx=20,pady=20,bg='black',fg='white',command=lambda:btn(0))

b_add=Button(root,text='+',padx=19,pady=20,bg='black',fg='green',command=btn_add)

b_el=Button(root,text='=',padx=40,pady=20,bg='orange',fg='white',command=btn_el)

b_cl=Button(root,text='AC',padx=20,pady=20,bg='black',fg='green',command=btn_cl)

b_subl=Button(root,text='-',padx=21,pady=20,bg='black',fg='green',command=btn_subl)

b_mul=Button(root,text='*',padx=20,pady=20,bg='black',fg='green',command=btn_mul)

b_divide=Button(root,text='/',padx=20,pady=20,bg='black',fg='green',command=btn_divide)

b_module=Button(root,text='%',padx=20,pady=20,bg='black',fg='green',command=btn_module)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)
b_cl.grid(row=4,column=1)
b_add.grid(row=5,column=0)
b_el.grid(row=5,column=1,columnspan=2)
b_module.grid(row=4,column=2)

b_subl.grid(row=6,column=0)
b_mul.grid(row=6,column=1)
b_divide.grid(row=6,column=2)

root.mainloop()