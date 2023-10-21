####
#STUDENT NAME: MUHAMMED ABED, MD NURUL AMIN BHUIYAN
#STUDENT NUMBER: 361222, 358037
#GROUP 62
####
'''Tax Calculated according to the tables in ATO Website
Investment interests are added every 4 weeks. No interest applicable if period is less than 4.
Example: If a person invests for 18 weeks, interest applicable every 4 weeks, upto week 16.
Interest not applicable for week 17 and 18'''
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

no_of_clients = 0
clients =[]   #list to store Client objects

class Client():
    def __init__(self, name = "", gross_salary=0, net_salary=0, residence=False,
                 tax=0, medicare=0, no_of_accounts = 0, accounts = []):
        self.name = name
        self.gross_salary = gross_salary
        self.net_salary = net_salary
        self.residence = residence
        self.tax = tax
        self.medicare = medicare
        self.no_of_accounts = no_of_accounts
        self.accounts = accounts        #stores list of Accounts
        

    def getName(self):
        return self.name
    def setName(self, input_name):
        self.name = input_name
        
    def getGrossSalary(self):
        return self.gross_salary
    def setGrossSalary(self, input_gross_salary):
        self.gross_salary = input_gross_salary
    
    def getNetSalary(self):
        self.net_salary = self.calcNetSalary()
        return self.net_salary
    
    def getResidence(self):
        return self.residence
    def setResidence(self, input_residence):
        self.residence = input_residence
    
    def getTax(self):
        self.tax = self.calcTax()
        return self.tax
    
    def getMedicare(self):
        self.medicare = self.calcMedicare()
        return self.medicare

    def getNumAccounts(self):
        return self.no_of_accounts
    
    def getAccounts(self):
        return self.no_of_accounts
    
    #Annual Tax calculated
    def calcTax(self):
        if self.residence:
            if self.gross_salary>=0 and self.gross_salary<= 18200:
                tax = 0
            elif self.gross_salary >= 18201 and self.gross_salary <= 45000:
                tax = (self.gross_salary-18200)*0.19
            elif (self.gross_salary >= 45001 and self.gross_salary <= 120000):
                tax = 5092 + ((self.gross_salary-45000)*0.325)
            elif self.gross_salary >= 120001 and self.gross_salary <= 180000:
                tax = 29467 + ((self.gross_salary-120000)*0.37)
            else:
                tax = 51667 + ((self.gross_salary-180000)*0.45)
        
        else:
            if self.gross_salary >= 0 and self.gross_salary <= 120000:
                tax = self.gross_salary*0.325
            
            elif self.gross_salary >= 120001 and self.gross_salary <= 180000:
                tax = 39000 + ((self.gross_salary-120000)*0.37)
            else:
                tax = 61200 + ((self.gross_salary-180000)*0.45)
        return tax
    
    def calcNetSalary(self):
        net_salary = self.getGrossSalary()-self.getTax()-self.getMedicare()
        return net_salary
    
    #Medicare calculated as 2% of Annual Gross Salary for residents only
    def calcMedicare(self):
        if self.residence and self.gross_salary>29032:
            medicare  = (self.gross_salary*0.02)
        else:
            medicare = 0.00
        return medicare
    
    #Calls method from Account class to make an account for current client
    def setAccount(self,account_num, amount, rate, weeks):
        self.accounts.append(Account())
        self.accounts[self.no_of_accounts].setAccount(int(account_num),
                                                      float(amount), float(rate), int(weeks))
        self.no_of_accounts+=1
        
    
    def deleteAccount(self, account_pos):
        for i in range (account_pos, self.no_of_accounts-1):
            self.accounts[i] = self.accounts[i+1]
        self.accounts.pop()
        self.no_of_accounts -=1
    
    
    #following methods call method from Account Class to get data
    def getAccountNo(self, input):
        return self.accounts[input].getAccountNum()
    
    def getRate(self, input):
        return self.accounts[input].getRate()
    
    def getAmount(self, input):
        return self.accounts[input].getAmount()
    
    def getWeeks(self,  input):
        return self.accounts[input].getWeeks()
    
    def investment(self, input):
        investment_list =  self.accounts[input].calcInvestment()
        return investment_list


class Account(Client):
    def __init__(self, account_number = 0,  amount = 0, rate = 0, number_of_weeks = 0):
        self.account_number = account_number
        self.amount = amount
        self.rate = rate
        self.number_of_weeks = number_of_weeks
        
    
    def setAccount(self, input_account_num, input_amount, input_rate, input_weeks):
        self.account_num = input_account_num
        self.amount = input_amount
        self.rate = input_rate
        self.number_of_weeks = input_weeks
    
    def getAccountNum(self):
        return self.account_num
    
    def getRate(self):
        return self.rate
    
    def getWeeks(self):
        return self.number_of_weeks
    
    def getAmount(self):
        return self.amount
    
    
    def calcInvestment(self):
        counter = 0
        balance = 0.00
        investment_return = []
        while (counter<self.number_of_weeks):
            if (self.number_of_weeks-counter >= 4):
                counter+=4
                period_rate = (self.rate/13)
                balance = (balance+(self.amount*4))*(1+(period_rate/100.00))
                investment_return.append(((counter, "${:.2f}".format(balance))))
                
            else: 
                balance = round((balance+(self.amount*(self.number_of_weeks-counter))), 2)
                investment_return.append(((self.number_of_weeks, "${:.2f}".format(balance))))
                counter = self.number_of_weeks+1
        
        return investment_return                 

class GUI(object):
    def __init__(self,root):
        self.root = root
        self.createGUI()
    
    def createGUI(self):
        self.createLabelFrame()
        self.createTreeView()
        self.createScrollbar()
        if no_of_clients>0:
            self.viewClients()
        self.messageArea()
        self.createButtons()
    
    #methods to setup widgets for a GUI     
    def createButtons(self):
        Button(text='Delete Account',command=self.deleteButtonClicked,
               bg='red',fg='white').grid(row=8,column=0,sticky=W,pady=15,padx=10)
        Button(text='Add Account',command=self.addAccountClicked,
               bg='purple',fg='white').grid(row=8,column=2,sticky=E)

    def createTreeView(self):
        columns = ('name', 'residence', 'gross_salary', 'tax','net_salary', 'medicare')
        self.tree = ttk.Treeview(columns=columns, show='headings', style='Treeview')
        self.tree.grid(row=6,column=0,columnspan=3)
        self.tree.heading('name',text='Name',anchor=W)
        self.tree.heading('residence',text='Resident',anchor=W)
        self.tree.heading('gross_salary',text='Gross Salary',anchor=W)
        self.tree.heading('tax',text='Tax',anchor=W)
        self.tree.heading('net_salary',text='Net Salary',anchor=W)
        self.tree.heading('medicare',text='Medicare',anchor=W)

        self.tree.column('name', stretch = False, width=200, minwidth= 200)
        self.tree.column('residence', stretch = False, width=100, minwidth=100)
        self.tree.column('gross_salary', stretch = False, width=120, minwidth=100)
        self.tree.column('tax', stretch = False, width=120, minwidth= 100)
        self.tree.column('net_salary', stretch = False, width=120, minwidth=100)
        self.tree.column('medicare', stretch = False, width=100, minwidth=100)

    def createScrollbar(self):
        self.scrollbar = Scrollbar(orient = 'vertical', command = self.tree.yview)
        self.scrollbar.grid(row = 4, column = 7, columnspan = 5, rowspan=4, sticky = "sn" )

    def messageArea(self):
        self.message = Label(text='',fg='red')
        self.message.grid(row=3,column=0,sticky=W)
        
    def createLabelFrame(self) :
        label_frame = LabelFrame(self.root, text='ADD CLIENT', bg="cadetblue2", fg="midnightblue",
                                 font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Name : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold" ).grid(row=1, column=1, sticky=W, pady=2, padx=19)
        self.name_field = Entry(label_frame, width =30)            
        self.name_field.grid(row=1, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Resident : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=2, column=1, sticky=W, pady=2, padx=19)
        self.residence_field = Entry(label_frame,width =30)
        self.residence_field.grid(row=2, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Annual Gross Salary : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=19)
        self.gsalary_field = Entry(label_frame,width =30)
        self.gsalary_field.grid(row=3, column=2, sticky=W, padx=5,)
        
        Button(label_frame, text="Add Client", command=self.addClient, bg="midnightblue", fg="white",
               font="helvetica 9 bold").grid(row=4, column=2, sticky=E, padx=5, pady=5) 
    
    #end of first GUI window setup
    
    #methods for Validation
    def nameCheck(self):
        if self.name_field.get().replace(" ","").isalpha() and len(self.name_field.get())>0:
            return True
        else:
            return False
    def residenceCheck(self):
        if self.residence_field.get().capitalize() == "Yes" or  self.residence_field.get().capitalize() == "No":
            return True
        else:
            return False
        
    def gSalaryCheck(self):
        if self.gsalary_field.get().isnumeric() and int(self.gsalary_field.get())>0:
            return True
        else:
            return False

    #Methods take user input and creates clients
    def addClient(self):
        global no_of_clients
        if self.nameCheck() and self.residenceCheck() and self.gSalaryCheck():
            clients.append(Client())
            if (self.residence_field.get()).capitalize() == "Yes":
                residence = True
            else:
                residence = False
            clients[no_of_clients].setName(self.name_field.get().title())
            clients[no_of_clients].setGrossSalary(int(self.gsalary_field.get()))
            clients[no_of_clients].setResidence(residence)
            self.message['text'] = 'New client {} added'.format(self.name_field.get().title())
            no_of_clients += 1
            self.viewClients()
            self.name_field.delete(0, END)
            self.gsalary_field.delete(0, END)
            self.residence_field.delete(0, END)
        else:
            self.message['text'] = 'Name must only contain alphabets. Gross Salary must only be in numeric and grater than 0. Resident must be "Yes" or "No"'
    
    #obtains index number of client in the list  
    def matchClient(self, name):
        for i in range (0,no_of_clients):
            if clients[i].getName() == name:
                j = i
                return j
    
    #obtains index number of client's account number
    def matchAccount(self, client_no, accountnum):

        for i in range(0, clients[client_no].getAccounts()):
            if clients[client_no].getAccountNo(i) == int(accountnum):
                j=i
                return j

    def viewClients(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for i in range (0, no_of_clients):
            if clients[i].getResidence():
                residence = 'Yes'
            else:
                residence = 'No'
            self.tree.insert('', 0, values= ('{}'.format(clients[i].getName()), '{}'.format(residence),
                                            '${:.2f}'.format(clients[i].getGrossSalary()),'${:.2f}'.format(clients[i].getTax()),
                                            '${:.2f}'.format(clients[i].getNetSalary()),'${:.2f}'.format(clients[i].getMedicare())))
    
    def deleteClient(self):
        global no_of_clients
        self.message['text']=''
        name = self.tree.item(self.tree.selection())['values'][0]
        client_index = self.matchClient(name)
        for i in range(client_index,no_of_clients-1):
            clients[i] = clients[i+1]
                
        clients.pop()
        no_of_clients -= 1
        self.message['text']='Account for {} deleted'.format(name)
        self.viewClients()
    
    #ensures program doesnt crash, and function to delete client is called successfully
    def deleteButtonClicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No client selected to delete'
            return
        self.deleteClient()
    
    def addAccountClicked(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No client selected'
            return
        self.addAccountWindow()
    
    #new window(GUI) to add account to client
    def addAccountWindow(self):
        name = self.tree.item(self.tree.selection())['values'][0]
        self.root.destroy()
        self.window = Tk()
        self.window.title('Add Account')
        bg = PhotoImage(file = "bg_acc.png")            #Background added to window
        bg_label = Label(self.window, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        self.window.geometry("500x500")
        self.window.resizable(width=False, height = False)
        columns = ('account','amount','rate','weeks')
        
        label_frame = LabelFrame(self.window, text='{}'.format(name), bg="cadetblue2", fg ="midnightblue", font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Account Number: ', bg="cadetblue2", fg="midnightblue", font="helvetica 9 bold").grid(row=0, column=1, sticky=W, pady=2, padx=15)
        self.account_field = Entry(label_frame)
        self.account_field.grid(row=0, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Weekly Investment: ', bg="cadetblue2", fg="midnightblue",font="helvetica 9 bold").grid(row=1, column=1, sticky=W, pady=2, padx=15)
        self.amount_field = Entry(label_frame)
        self.amount_field.grid(row=1, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Annual Interest Rate : ', bg="cadetblue2", fg="midnightblue",font="helvetica 9 bold").grid(row=2, column=1, sticky=W, pady=2, padx=15)
        self.rate_field = Entry(label_frame)
        self.rate_field.grid(row=2, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Weeks : ', bg="cadetblue2", fg="midnightblue", font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=15)
        self.week_field = Entry(label_frame)
        self.week_field.grid(row=3, column=2, sticky=W, padx=5,)
        
        Button(label_frame, text='Add', command=lambda: self.addAccount(name,
            (self.account_field.get()), (self.amount_field.get()), (self.rate_field.get()),
            (self.week_field.get())), bg = "midnightblue",fg="white", font ="helvetica 9 bold").grid(row=4, column= 2, sticky=E)
        
        self.tree = ttk.Treeview(self.window, columns=columns,show='headings', style='Treeview')
        self.tree.grid(row=6, column = 0, columnspan = 1)
        
        self.tree.heading('account',text='Account', anchor=W)
        self.tree.heading('amount',text='Amount', anchor=W)
        self.tree.heading('rate',text='Rate', anchor=W)
        self.tree.heading('weeks',text='Weeks', anchor=W)
        
        self.tree.column('account', stretch = False, width=125, minwidth=100)
        self.tree.column('amount', stretch = False, width=120, minwidth=120)
        self.tree.column('rate', stretch = False, width=100, minwidth=100)
        self.tree.column('weeks', stretch = False, width=70, minwidth=70)
                   
        self.scrollbar = Scrollbar(master = self.window, orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=1,columnspan=3,rowspan=3,sticky='sn')
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        client_index = self.matchClient(name)
        
        #rows of table filled by every account of client
        for i in range (0,clients[client_index].getAccounts()):
            self.tree.insert('',0, text = '', values=(clients[client_index].getAccountNo(i),
                                                      '${:.2f}'.format(clients[client_index].getAmount(i)),
                                                      '{:.2f}%'.format( clients[client_index].getRate(i)), 
                                                       clients[client_index].getWeeks(i))) 
        
        Button(self.window,text='Delete Selected',command=lambda: self.deleteButtonClickedAcc(name),
               bg='red',fg='white', font ="helvetica 9 bold").grid(row=11,column=0, sticky=W, pady = 10) 
        Button(self.window,text='Show Return Table',command=lambda: self.showReturnClicked(name),bg='blue',fg='white', font ="helvetica 9 bold").grid(row=10,column=0 ,sticky=E, pady = 10)
        Button(self.window,text='Back',command=self.call_main,bg='orange',fg='Black', font ="helvetica 9 bold").grid(row=10,column=0,sticky=W, pady = 10)
        self.window.mainloop()
    
    def accountCheck(self):
        if self.account_field.get().isnumeric():
            return True
        else:
            return False
    
    def amountCheck(self):
        if self.amount_field.get().isnumeric():
            return True
        else:
            return False
    
    def rateCheck(self):
        if self.rate_field.get().replace(".","").isnumeric() and float(self.rate_field.get())>0 and float(self.rate_field.get()) <= 20:
            return True
        else:
            return False
    
    def weekCheck(self):
        if self.week_field.get().isnumeric():
            return True
        else:
            return False
         
    def addAccount(self,name, account, amount, rate, week):
        
        if self.accountCheck() and self.amountCheck() and self.rateCheck() and self.weekCheck():
            client_index = self.matchClient(name)
            clients[client_index].setAccount(account, amount, rate, week)
            self.viewAccounts(client_index)
            self.account_field.delete(0, END)
            self.amount_field.delete(0, END)
            self.rate_field.delete(0, END)
            self.week_field.delete(0, END)
        
        else:
            tkinter.messagebox.showwarning('Input Error', 'Please enter numeric values in all fields. Interest Rate must be between 1-20 percent')

    def deleteAccount(self, name):
        client_index = self.matchClient(name)
        account_number = int(self.tree.item(self.tree.selection())['values'][0])
        
        account_index = self.matchAccount(client_index, account_number)
        clients[client_index].deleteAccount(account_index)
        self.viewAccounts(client_index)
                
    
    def viewAccounts(self, client_no):

        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)

        for i in range (0,clients[client_no].getAccounts()):
            self.tree.insert('',0, text = '', values=(clients[client_no].getAccountNo(i),
                                                      '${:.2f}'.format(clients[client_no].getAmount(i)),
                                                      '{:.2f}%'.format( clients[client_no].getRate(i)), clients[client_no].getWeeks(i)))

    #views table of updated balance at the end of every period(4 weeks)
    def showReturn(self,name):
        client_index = self.matchClient(name)
        
        account_number = int(self.tree.item(self.tree.selection())['values'][0])
        account_index = self.matchAccount(client_index, account_number)

        self.win = Toplevel()
        self.win.title('{}'.format(account_number))
        self.window.resizable(width=False, height = False)

        columns = ('week', 'balance')
        invreturn = ttk.Treeview(self.win, columns=columns, show='headings',style='Treeview')
        invreturn.grid (row=1, column = 0, columnspan=4, sticky=W)
        invreturn.heading('week', text ='Week',anchor=W)
        invreturn.heading('balance', text ='Balance',anchor=W)        
        invreturn.column('week', stretch= False, width=70, minwidth=50)
        invreturn.column('balance', stretch= False, width=150, minwidth=100)

        self.scrollbar = Scrollbar(self.win, orient='vertical',command=invreturn.yview)
        self.scrollbar.grid(row=1,column=5,columnspan=3,rowspan=3,sticky='sn')
        
        items = invreturn.get_children()
        for item in items:
            invreturn.delete(item)            
        balance = clients[client_index].investment(account_index)
        for rows in balance:
            invreturn.insert('', END, values = rows )

        self.win.mainloop()
    
 
    def showReturnClicked(self,name):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No account selected.')

            return
        self.showReturn(name)

    def deleteButtonClickedAcc(self,name):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No account selected.')

            return
        self.deleteAccount(name)
        

    #method to return to main window
    def call_main(self):
        self.window.destroy()
        root = Tk()
        root.title('Tax and Investment Calculator')
        bg = PhotoImage(file = "app_bgmain.png")
        bg_label = Label(root, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        application = GUI(root)
        root.geometry("800x500")
        root.mainloop()

if __name__ == '__main__':
    root = Tk()
    root.title('Tax and Investment Calculator')
    bg = PhotoImage(file = "app_bgmain.png")
    bg_label = Label(root, image = bg)
    bg_label.place(x=0,y=0, relheight=1,relwidth=1)
    application = GUI(root)
    root.geometry("800x500")

    
    root.resizable(width=False, height=False)
    root.mainloop()
    

    
    
    