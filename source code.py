from tkinter import*
import math

def bnClick():
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def bnclearDisplay():
    global operator
    operator=""
    text_Input.set("")
def equalInput():
    global operator
    final=str(eval(operator=""))
    text_Input.set(final)
    operator=""
    

phyiscs= Tk()

phyiscs.title("Calculater")

operator =""

text_Input= StringVar()

txtdisplay = Entry(phyiscs,font= ('arial', 20,'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                bg="powder blue",justify='right').grid(columnspan=6)




bn7=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="7"),bg="powered blue",command=lambda:bnClick(7).grid(row=1,colunm=0)





bn8=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="8",bg="powered blue",command=lambda:bnClick(8).grid(row=1,colunm=1)




bn9=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="9",bg="powered blue",command=lambda:bnClick(9).grid(row=1,colunm=2)



plusbutton=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="+",bg="powered blue",command=lambda:bnClick(+).grid(row=1,colunm=3)





bn4=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="4",bg="powered blue",command=lambda:bnClick(4).grid(row=2,colunm=0)




bn5=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="5",bg="powered blue",command=lambda:bnClick(5).grid(row=2,colunm=1)




bn6=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="6",bg="powered blue",command=lambda:bnClick(6).grid(row=2,colunm=2)

            
minusbutton=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="-",bg="powered blue",command=lambda:bnClick(-).grid(row=2,colunm=3)
            




bn1=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="1",bg="powered blue",command=lambda:bnClick(1).grid(row=3,colunm=0)




bn2=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="2",bg="powered blue",command=lambda:bnClick(2).grid(row=3,colunm=1)




bn3=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="3",bg="powered blue",command=lambda:bnClick(3).grid(row=3,colunm=2)


multibutton=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="*",bg="powered blue",command=lambda:bnClick(*).grid(row=3,colunm=3)



bn0=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="0",bg="powered blue",command=lambda:bnClick(0).grid(row=4,colunm=0)



bnclear=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="C",bg="powered blue",commandbnclearDisplay).command=lambda:bnClick(C).grid(row=4,colunm=1)



equal=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="=",bg="powered blue",command=equalInput).bnClick(=).grid(row=4,colunm=2)



divide=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="/",bg="powered blue",command=lambda:bnClick(/).grid(row=4,colunm=3)



cos=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="cos",bg="powered blue",command=lambda:bnClick(cos).grid(row=5,colunm=0)



sin=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="sin",bg="powered blue",command=lambda:bnClick(sin).grid(row=5,colunm=1)


tan=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="tan",bg="powered blue",command=lambda:bnClick(tan).grid(row=5,colunm=2)


decimal=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text=".",bg="powered blue",command=lambda:bnClick(.).grid(row=5,colunm=3)


power=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="^",bg="powered blue",command=lambda:bnClick(^).grid(row=6,colunm=0)


pi=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="3.14",bg="powered blue",command=lambda:bnClick(3.14).grid(row=6,colunm=1)


sqaureroot=Button(phyiscs,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
            text="//",bg="powered blue",command=lambda:bnClick(//).grid(row=6,colunm=2)


cal.mainloop()
