from tkinter import *
from tkinter import ttk
import tkinter.messagebox

class Admin():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.privileges = []


    def describe_user(self):
        """Display a summary of the user's information."""
        print("\n" + self.first_name + " " + self.last_name)
        print("  Username: " + self.username)
        print("  Email: " + self.email)
        print("  Location: " + self.location)

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print("\nWelcome back, " + self.username + "!")


    def show_privileges(self):
        """Display the privileges this administrator has."""
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

class Location():

    def __init__(self, name, crocs=False):
        self.name = name.title()
        self.crocs = crocs

class Account(spot):
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
no_of_spots=0
spots = []
class GUI(object):
    def __init__(self,root):
        self.root = root
        self.createGUI()
    
    def createGUI(self):
        self.createLabelFrame()
        self.createTreeView()
        self.createScrollbar()
        if no_of_spots>0:
            self.viewspots()
        self.messageArea()
        self.createButtons()
    
    #methods to setup widgets for a GUI     
    def createButtons(self):
        Button(text='Delete Location',command=self.deleteButtonClicked,
               bg='red',fg='white').grid(row=8,column=0,sticky=W,pady=15,padx=10)
        Button(text='Add Location',command=self.addLocationClicked,
               bg='purple',fg='white').grid(row=8,column=2,sticky=E)

    def createTreeView(self):
        columns = ('location', 'safety')
        self.tree = ttk.Treeview(columns=columns, show='headings', style='Treeview')
        self.tree.grid(row=6,column=0,columnspan=3)
        self.tree.heading('location',text='Location',anchor=W)
        self.tree.heading('safety',text='Safety',anchor=W)
        # self.tree.heading('gross_salary',text='Gross Salary',anchor=W)
        # self.tree.heading('tax',text='Tax',anchor=W)
        # self.tree.heading('net_salary',text='Net Salary',anchor=W)
        # self.tree.heading('medicare',text='Medicare',anchor=W)

        self.tree.column('location', stretch = False, width=200, minwidth= 200)
        self.tree.column('safety', stretch = False, width=100, minwidth=100)
        # self.tree.column('gross_salary', stretch = False, width=120, minwidth=100)
        # self.tree.column('tax', stretch = False, width=120, minwidth= 100)
        # self.tree.column('net_salary', stretch = False, width=120, minwidth=100)
        # self.tree.column('medicare', stretch = False, width=100, minwidth=100)

    def createScrollbar(self):
        self.scrollbar = Scrollbar(orient = 'vertical', command = self.tree.yview)
        self.scrollbar.grid(row = 4, column = 7, columnspan = 5, rowspan=4, sticky = "sn" )

    def messageArea(self):
        self.message = Label(text='',fg='red')
        self.message.grid(row=3,column=0,sticky=W)
        
    def createLabelFrame(self) :
        label_frame = LabelFrame(self.root, text='ADD LOCATION', bg="cadetblue2", fg="midnightblue",
                                 font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Location : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold" ).grid(row=1, column=1, sticky=W, pady=2, padx=19)
        self.location_field = Entry(label_frame, width =30)            
        self.location_field.grid(row=1, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Safety : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=2, column=1, sticky=W, pady=2, padx=19)
        self.safety_field = Entry(label_frame,width =30)
        self.safety_field.grid(row=2, column=2, sticky=W, padx=5,)
        # Label(label_frame, text='Annual Gross Salary : ', bg="cadetblue2", fg="midnightblue",
        #       font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=19)
        # self.gsalary_field = Entry(label_frame,width =30)
        # self.gsalary_field.grid(row=3, column=2, sticky=W, padx=5,)
        
        Button(label_frame, text="Add Location", command=self.addLocation, bg="midnightblue", fg="white",
               font="helvetica 9 bold").grid(row=4, column=2, sticky=E, padx=5, pady=5) 
    
    #end of first GUI window setup
    
    #methods for Validation
    def locationCheck(self):
        if self.location_field.get().replace(" ","").isalpha() and len(self.location_field.get())>0:
            return True
        else:
            return False
    def safetyCheck(self):
        if self.safety_field.get().capitalize() == "Yes" or  self.safety_field.get().capitalize() == "No":
            return True
        else:
            return False
        
    # def gSalaryCheck(self):
    #     if self.gsalary_field.get().isnumeric() and int(self.gsalary_field.get())>0:
    #         return True
    #     else:
    #         return False

    #Methods take user input and creates spots
    def addLocation(self):
        global no_of_spots
        if self.locationCheck() and self.safetyCheck():
            spots.append(Location())
            if (self.safety_field.get()).capitalize() == "Yes":
                residence = True
            else:
                residence = False
            spots[no_of_spots].name = self.name_field.get().title()
            spots[no_of_spots].setGrossSalary(int(self.gsalary_field.get()))
            spots[no_of_spots].setResidence(residence)
            self.message['text'] = 'New spot {} added'.format(self.name_field.get().title())
            no_of_spots += 1
            self.viewspots()
            self.name_field.delete(0, END)
            self.gsalary_field.delete(0, END)
            self.residence_field.delete(0, END)
        else:
            self.message['text'] = 'Name must only contain alphabets. Gross Salary must only be in numeric and grater than 0. Resident must be "Yes" or "No"'
    
    #obtains index number of spot in the list  
    def matchspot(self, name):
        for i in range (0,no_of_spots):
            if spots[i].getName() == name:
                j = i
                return j
    
    #obtains index number of spot's account number
    def matchAccount(self, spot_no, accountnum):

        for i in range(0, spots[spot_no].getAccounts()):
            if spots[spot_no].getAccountNo(i) == int(accountnum):
                j=i
                return j

    def viewspots(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for i in range (0, no_of_spots):
            if spots[i].getResidence():
                residence = 'Yes'
            else:
                residence = 'No'
            self.tree.insert('', 0, values= ('{}'.format(spots[i].getName()), '{}'.format(residence),
                                            '${:.2f}'.format(spots[i].getGrossSalary()),'${:.2f}'.format(spots[i].getTax()),
                                            '${:.2f}'.format(spots[i].getNetSalary()),'${:.2f}'.format(spots[i].getMedicare())))
    
    def deletespot(self):
        global no_of_spots
        self.message['text']=''
        name = self.tree.item(self.tree.selection())['values'][0]
        spot_index = self.matchspot(name)
        for i in range(spot_index,no_of_spots-1):
            spots[i] = spots[i+1]
                
        spots.pop()
        no_of_spots -= 1
        self.message['text']='Account for {} deleted'.format(name)
        self.viewspots()
    
    #ensures program doesnt crash, and function to delete spot is called successfully
    def deleteButtonClicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No spot selected to delete'
            return
        self.deletespot()
    
    def addLocationClicked(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            self.message['text'] = 'No spot selected'
            return
        self.addAccountWindow()
    
    #new window(GUI) to add account to spot
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
        spot_index = self.matchspot(name)
        
        #rows of table filled by every account of spot
        for i in range (0,spots[spot_index].getAccounts()):
            self.tree.insert('',0, text = '', values=(spots[spot_index].getAccountNo(i),
                                                      '${:.2f}'.format(spots[spot_index].getAmount(i)),
                                                      '{:.2f}%'.format( spots[spot_index].getRate(i)), 
                                                       spots[spot_index].getWeeks(i))) 
        
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
            spot_index = self.matchspot(name)
            spots[spot_index].setAccount(account, amount, rate, week)
            self.viewAccounts(spot_index)
            self.account_field.delete(0, END)
            self.amount_field.delete(0, END)
            self.rate_field.delete(0, END)
            self.week_field.delete(0, END)
        
        else:
            tkinter.messagebox.showwarning('Input Error', 'Please enter numeric values in all fields. Interest Rate must be between 1-20 percent')

    def deleteAccount(self, name):
        spot_index = self.matchspot(name)
        account_number = int(self.tree.item(self.tree.selection())['values'][0])
        
        account_index = self.matchAccount(spot_index, account_number)
        spots[spot_index].deleteAccount(account_index)
        self.viewAccounts(spot_index)
                
    
    def viewAccounts(self, spot_no):

        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)

        for i in range (0,spots[spot_no].getAccounts()):
            self.tree.insert('',0, text = '', values=(spots[spot_no].getAccountNo(i),
                                                      '${:.2f}'.format(spots[spot_no].getAmount(i)),
                                                      '{:.2f}%'.format( spots[spot_no].getRate(i)), spots[spot_no].getWeeks(i)))

    #views table of updated balance at the end of every period(4 weeks)
    def showReturn(self,name):
        spot_index = self.matchspot(name)
        
        account_number = int(self.tree.item(self.tree.selection())['values'][0])
        account_index = self.matchAccount(spot_index, account_number)

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
        balance = spots[spot_index].investment(account_index)
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



eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]

eric.show_privileges()

