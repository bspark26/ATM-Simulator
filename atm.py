
from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
import datetime
import time

class atm:

    def __init__(self,root):
        self.root = root
        blank_space =" " 
        self.root.title(110*blank_space + "ATM Systems")
        self.root.geometry("774x760+280+0")
        self.root.configure(background ='gainsboro')        
        #====================================================================================================================
        MainFrame = Frame(self.root,bd=20,width=760,height=700,bg="gainsboro",relief=RIDGE)
        MainFrame.grid()
        
        TopFrame1 = Frame(MainFrame,bd=7,width=730,height=300,bg="gainsboro",relief=RIDGE)
        TopFrame1.grid(row = 2 ,column = 0,padx = 12)
        TopFrame2 = Frame(MainFrame,bd=7,width=730,height=300,bg="gainsboro",relief=RIDGE)
        TopFrame2.grid(row = 1 ,column = 0,padx = 8)

        TopFrame2Left = Frame(TopFrame2,bd=5,width=190,height=300,bg="gainsboro",relief=RIDGE)
        TopFrame2Left.grid(row = 1 ,column = 0)
        TopFrame2Mid = Frame(TopFrame2,bd=5,width=200,height=300,bg="gainsboro",relief=RIDGE)
        TopFrame2Mid.grid(row = 1 ,column = 1)
        TopFrame2Right = Frame(TopFrame2,bd=5,width=190,height=300,bg="gainsboro",relief=RIDGE)
        TopFrame2Right.grid(row = 1 ,column = 2)
        #==========================================Functions==========================================

            
        def Clear():


            self.btnArL1=Button(TopFrame2Left,width= 160,height=60,
            state = DISABLED, image=self.imgarrowL ).grid(row=0,column=0,pady = 2,padx = 4)

            self.btnArL2=Button(TopFrame2Left,width= 160,height=60,
            state = DISABLED, image=self.imgarrowL ).grid(row=1,column=0,pady = 2,padx = 4)

            self.btnArL3=Button(TopFrame2Left,width= 160,height=60,
            state = DISABLED, image=self.imgarrowL ).grid(row=2,column=0,pady = 2,padx = 4)

            self.btnArL4=Button(TopFrame2Left,width= 160,height=60,
            state = DISABLED, image=self.imgarrowL ).grid(row=3,column=0,pady = 2,padx = 4)

            self.btnArR1=Button(TopFrame2Right,width= 160,height=60,
            state = DISABLED, image=self.imgarrowR ).grid(row=0,column=0,pady = 2,padx = 4)

            self.btnArR2=Button(TopFrame2Right,width= 160,height=60,
            state = DISABLED, image=self.imgarrowR ).grid(row=1,column=0,pady = 2,padx = 4)

            self.btnArR3=Button(TopFrame2Right,width= 160,height=60,
            state = DISABLED, image=self.imgarrowR ).grid(row=2,column=0,pady = 2,padx = 4)

            self.btnArR4=Button(TopFrame2Right,width= 160,height=60,
            state = DISABLED, image=self.imgarrowR ).grid(row=3,column=0,pady = 2,padx = 4)
            self.txtReceipt.delete("1.0",END)

        def Pin():
##            self.btnArR1.configure(state="normal")

            pinNo = self.txtReceipt.get("1.0", "end-1c")
            if  ((pinNo == str("2123")) or (pinNo == str("4321")) or (pinNo == str("4323"))):
                self.txtReceipt.delete("1.0",END)

                self.txtReceipt.insert(END,'\t\t        ATM' + "\n\n")
                self.txtReceipt.insert(END,'Withdraw Cash \t\t\t Loan' +"\n\n\n\n")
                self.txtReceipt.insert(END,'Cash With Receipt \t\t\t Deposit' +"\n\n\n\n")
                self.txtReceipt.insert(END,'Balance \t\t\t Request new pin'+ "\n\n\n\n")
                self.txtReceipt.insert(END,'Mini Statement \t\t\t  Print Statement'+  "\n\n\n\n\n")

                self.btnArL1=Button(TopFrame2Left,width= 160,height=60, command=withdrawcash,
                state = NORMAL, image=self.imgarrowL ).grid(row=0,column=0,pady = 2,padx = 4)

                self.btnArL2=Button(TopFrame2Left,width= 160,height=60,command=cashwithReceipt,
                state = NORMAL, image=self.imgarrowL ).grid(row=1,column=0,pady = 2,padx = 4)

                self.btnArL3=Button(TopFrame2Left,width= 160,height=60,command=balance,
                state = NORMAL, image=self.imgarrowL ).grid(row=2,column=0,pady = 2,padx = 4)

                self.btnArL4=Button(TopFrame2Left,width= 160,height=60,command=statement,
                state = NORMAL, image=self.imgarrowL ).grid(row=3,column=0,pady = 2,padx = 4)

                
                self.btnArR1 = Button(TopFrame2Right, width= 160, height=60,state = NORMAL,
                image =self.imgarrowR,command=loan).grid(row =0,column=0,pady=2,padx = 4)

                self.btnArR2=Button(TopFrame2Right,width= 160,height=60, command=deposit,
                state = NORMAL, image=self.imgarrowR ).grid(row=1,column=0,pady = 2,padx = 4)

                self.btnArR3=Button(TopFrame2Right,width= 160,height=60,command=request_new_pin,
                state = NORMAL, image=self.imgarrowR ).grid(row=2,column=0,pady = 2,padx = 4)

                self.btnArR4=Button(TopFrame2Right,width= 160,height=60, command=statement,
                state = NORMAL, image=self.imgarrowR ).grid(row=3,column=0,pady = 2,padx = 4)

            else:
                self.txtReceipt.delete("1.0",END)
                self.txtReceipt.insert(END,'Invalid Pin Number' +"\n\n")

        def withdrawcash():
            Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def cashwithReceipt():
            Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()


        def loan():
            Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'Loan $ ')
            self.txtReceipt.focus_set()

        def deposit():
            Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.focus_set()

        def request_new_pin():
            Pin()
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\tWelcome to myATM\n')
            self.txtReceipt.insert(END,'New Pin will be sent to your home address\n')
            self.txtReceipt.insert(END,'\t\tThanks for using myATM\n')
            self.txtReceipt.insert(END,'Withdraw Cash \t\t\t Loan' +"\n\n\n")
            self.txtReceipt.insert(END,'Cash With Receipt \t\t\t Deposit' +"\n\n\n")
            self.txtReceipt.insert(END,'Balance \t\t\t Withdrawal'+ "\n\n\n")
            self.txtReceipt.insert(END,'Mini Statement \t\t\t  Print Statement'+  "\n\n\n\n\n")


        def balance():

            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\t\t\t\t\t\n\n    Account Balance' + "\t\t")
            self.txtReceipt.insert(END,'$1296' +"\n\n\n")
            self.txtReceipt.insert(END,'Withdraw Cash \t\t\t Loan' +"\n\n\n")
            self.txtReceipt.insert(END,'Cash With Receipt \t\t\t Deposit' +"\n\n\n")
            self.txtReceipt.insert(END,'Balance \t\t\t Withdrawal'+ "\n\n\n")
            self.txtReceipt.insert(END,'Mini Statement \t\t\t  Print Statement'+  "\n\n\n\n\n")


        def statement():
       

            pinNo1 = str(self.txtReceipt.get("1.0", "end-1c"))
            pinNo2 = str(pinNo1)
            pinNo3 = float(pinNo2)
            pinNo4 = float(1296 - (pinNo3 ))
            self.txtReceipt.delete("1.0",END)
            self.txtReceipt.insert(END,'\n\t' + str(pinNo4) +   "\t\t")
            self.txtReceipt.insert(END,'\t\t\t\n\n    Account Balance $' + str(pinNo4)+ "\t\t\n\n")            
            self.txtReceipt.insert(END,'Rent \t\t\t\t $1200' +"\n\n")
            self.txtReceipt.insert(END,'Tesco \t\t\t\t $79.36'+ "\n\n")
            self.txtReceipt.insert(END,'Rent \t\t\t\t $1200' +"\n\n")
            self.txtReceipt.insert(END,'Sainsbury'+'s \t\t\t\t $53.87'+ "\n\n")
            self.txtReceipt.insert(END,'Student Loan \t\t\t\t $69.72' +"\n\n")
            self.txtReceipt.insert(END,'Dollarland \t\t\t\t $19.00'+ "\n\n")


            
        def Cancel():
            Cancel = tkinter.messagebox.askyesno("ATM", "Confirm if you want to cancel")
            if Cancel > 0:                
                self.root.destroy()     
                return

        def insert0():
            value0= 0
            self.txtReceipt.insert(END,value0)

        def insert1():
            value1= 1
            self.txtReceipt.insert(END,value1)

        def insert2():
            value2= 2
            self.txtReceipt.insert(END,value2)

        def insert3():
            value3= 3
            self.txtReceipt.insert(END,value3)

        def insert4():
            value4= 4
            self.txtReceipt.insert(END,value4)

        def insert5():
            value5= 5
            self.txtReceipt.insert(END,value5)

        def insert6():
            value6= 6
            self.txtReceipt.insert(END,value6)

        def insert7():
            value7= 7
            self.txtReceipt.insert(END,value7)

        def insert8():
            value8= 8
            self.txtReceipt.insert(END,value8)

        def insert9():
            value9= 9
            self.txtReceipt.insert(END,value9)



        #=============================================================================================
        self.txtReceipt = Text(TopFrame2Mid, height= 17, width=42, bd=12,font=('arial',9, 'bold'))
        self.txtReceipt .grid(row=0,column=0)
        self.txtReceipt.insert(END,'\t\t          ATM' + "\n\n")
        self.txtReceipt.insert(END,'Cash \t\t\t\t Loan' +"\n\n\n\n")
        self.txtReceipt.insert(END,'Cash With Receipt \t\t\t\t Deposit' +"\n\n\n\n")
        self.txtReceipt.insert(END,'Statement \t\t\t\t Withdrawal'+ "\n\n\n\n")
        self.txtReceipt.insert(END,'Mini Statement \t\t\t\t Statement'+  "\n\n\n\n\n")
        self.txtReceipt.delete("1.0",END)
        self.txtReceipt.focus_set()
        #==========================================xxxx================================================
        self.imgarrowL = PhotoImage(file="./ATM_Icon/lArrow.png")
        
        self.btnArL1=Button(TopFrame2Left,command= withdrawcash,width= 160, height=60, 
        state = DISABLED,image=self.imgarrowL).grid(row=0,column=0,pady = 2,padx = 4)

        self.btnArL2=Button(TopFrame2Left,command= cashwithReceipt,width= 160, height=60, 
        state = DISABLED,image=self.imgarrowL).grid(row=1,column=0,pady = 2,padx = 4)

        self.btnArL3=Button(TopFrame2Left,command= balance,width= 160, height=60,
        state = DISABLED, image=self.imgarrowL ).grid(row=2,column=0,pady = 2,padx = 4)

        self.btnArL4=Button(TopFrame2Left,command= statement,width= 160, height=60,
        state = DISABLED, image=self.imgarrowL ).grid(row=3,column=0,pady = 2,padx = 4)

        #=============================================================================================
        self.imgarrowR = PhotoImage(file ="./ATM_Icon/rArrow.png")

        self.btnArR1=Button(TopFrame2Right,width= 160,height=60, command=loan,
        state = DISABLED, image=self.imgarrowR ).grid(row=0,column=0,pady = 2,padx = 4)

        self.btnArR2=Button(TopFrame2Right,width= 160,height=60, command=deposit,
        state = DISABLED, image=self.imgarrowR ).grid(row=1,column=0,pady = 2,padx = 4)

        self.btnArR3=Button(TopFrame2Right,width= 160,height=60, command=request_new_pin,
        state = DISABLED, image=self.imgarrowR ).grid(row=2,column=0,pady = 2,padx = 4)

        self.btnArR4=Button(TopFrame2Right,width= 160,height=60, command=statement,
        state = DISABLED, image=self.imgarrowR ).grid(row=3,column=0,pady = 2,padx = 4)

        #=========================================================================================================

        self.img1 = PhotoImage(file="./ATM_Icon/one.png")
        self.btn1=Button(TopFrame1, command= insert1,width= 160, height=60,
        image  =self.img1 ).grid(row=2,column=0,pady = 4,padx = 4)

        self.img2 = PhotoImage(file="./ATM_Icon/two.png")
        self.btn2=Button(TopFrame1,command= insert2,width= 160, height=60,
        image = self.img2).grid(row=2,column=1,pady = 4,padx = 4)

        self.img3 = PhotoImage(file="./ATM_Icon/three.png")
        self.btn3=Button(TopFrame1,command= insert3,width= 160, height=60,
        image = self.img3).grid(row=2,column=2,pady = 4,padx = 4)

        #---------------------------------------------------------------------------------------------------------------
        self.img4 = PhotoImage(file="./ATM_Icon/four.png")
        self.btn4=Button(TopFrame1,command= insert4,width= 160, height=60,
        image = self.img4).grid(row=3,column=0,pady = 4,padx = 4)

        self.img5 = PhotoImage(file="./ATM_Icon/five.png")
        self.btn5=Button(TopFrame1,command= insert5,width= 160, height=60,
        image = self.img5).grid(row=3,column=1,pady = 4,padx = 4)

        self.img6 = PhotoImage(file="./ATM_Icon/six.png")
        self.btn6=Button(TopFrame1,command= insert6,width= 160, height=60,
        image = self.img6).grid(row=3,column=2,pady = 4,padx = 4)


        #---------------------------------------------------------------------------------------------------------------
        self.img7 = PhotoImage(file="./ATM_Icon/seven.png")
        self.btn7=Button(TopFrame1,command= insert7,width= 160, height=60,
        image = self.img7).grid(row=4,column=0,pady = 4,padx = 4)

        self.img8 = PhotoImage(file="./ATM_Icon/eight.png")
        self.btn8=Button(TopFrame1,command= insert8,width= 160, height=60,
        image = self.img8).grid(row=4,column=1,pady = 4,padx = 4)

        self.img9 = PhotoImage(file="./ATM_Icon/nine.png")
        self.btn9=Button(TopFrame1,command= insert9,width= 160, height=60,
        image = self.img9).grid(row=4,column=2,pady = 4,padx = 4)


        #=============================================x==============================================================
        self.imgSp1 = PhotoImage(file="./ATM_Icon/empty.png")
        self.btnSpace = Button(TopFrame1,width= 160, height=60,
        image = self.imgSp1).grid(row = 5, column = 0,pady = 4,padx = 4)

        self.imgCE = PhotoImage(file="./ATM_Icon/cancel.png")
        self.btnCancel = Button(TopFrame1, width= 160, height=60,
        image = self.imgCE, command=Cancel).grid(row = 2, column = 3,pady = 4,padx = 4)
        
        self.imgCl = PhotoImage(file="./ATM_Icon/clear.png")
        self.btnClear = Button(TopFrame1, width= 160, height=60,
        image = self.imgCl, command=Clear).grid(row = 3, column = 3,pady = 4,padx = 4)                

        self.imgEnter = PhotoImage(file="./ATM_Icon/enter.png")
        self.btnEnter = Button(TopFrame1,width= 160, height=60,
        image = self.imgEnter, command=Pin).grid(row = 4, column = 3,pady = 4,padx = 4)      

        self.img0 = PhotoImage(file="./ATM_Icon/zero.png")
        self.btnZero = Button(TopFrame1, command= insert0,width= 160, height=60,
        image = self.img0).grid(row = 5, column = 1,pady = 4,padx = 4)      

        self.imgSp2 = PhotoImage(file="./ATM_Icon/empty.png")
        self.btnSp2 = Button(TopFrame1,width= 160, height=60,
        image = self.imgSp2).grid(row = 5, column = 2,pady = 4,padx = 4)
 
        self.imgSp3 = PhotoImage(file="./ATM_Icon/empty.png")
        self.btnSp = Button(TopFrame1, width= 160, height=60,
        image =self.imgSp3).grid(row = 5, column = 3,pady = 4,padx = 4)
           



if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()