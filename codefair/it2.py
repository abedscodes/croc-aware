from tkinter import *
from tkinter import ttk
import tkinter.messagebox

no_of_locations = 0
locations = []
sonars =[]
admins=[]
riverSystem = {}

class Sonar():
    def __init__(self, id ='', name='', locations = [], safety=True):
        self.id = id
        self.name = name
        self.safety = safety
        self.locations = locations
    
    def obj_check(self, loc):
        for obj in self.locations:
            if obj.name == loc:
                return True
        return False
    
    def add_locationNew(self, loc):
        
        if not self.obj_check(loc):
            self.locations.append(Location(name = loc, safety = self.safety ))
            if loc not in riverSystem:
                riverSystem[loc] = []
            if self not in riverSystem[loc]:
                riverSystem[loc].append(self)
    
    def delete_location(self, loc):
        for i in range(loc, len(self.locations)-1):
            self.locations[i]=self.locations[i+1]
        self.locations.pop()


    
class Location(Sonar):
    def __init__(self, name='', safety = True):
        self.name = name
        self.safety = safety

class Admin():
    def __init__(self, name='', username='', password =''):
        self.name = name
        self.username = username
        self.password = password



admins.append(Admin(username='admin', password= 'admin'))
class GUI(object):
    def __init__(self,root):
        self.root = root
        self.createGUI()
    
    def createGUI(self):
        self.createLabelFrame()
        self.createTreeView()
        self.createScrollbar()
        if no_of_locations>0:
            self.viewLocations()
        self.messageArea()
        #self.createButtons()
    
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

        self.tree.column('location', stretch = False, width=200, minwidth= 200)
        self.tree.column('safety', stretch = False, width=100, minwidth=100)

    def createScrollbar(self):
        self.scrollbar = Scrollbar(orient = 'vertical', command = self.tree.yview)
        self.scrollbar.grid(row = 4, column = 7, columnspan = 5, rowspan=4, sticky = "sn" )

    def messageArea(self):
        self.message = Label(text='',fg='red')
        self.message.grid(row=3,column=0,sticky=W)
        
    def createLabelFrame(self) :
        label_frame = LabelFrame(self.root, text='Log In', bg="cadetblue2", fg="midnightblue",
                                 font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Username : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold" ).grid(row=1, column=1, sticky=W, pady=2, padx=19)
        self.username_field = Entry(label_frame, width =30)            
        self.username_field.grid(row=1, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Password : ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=2, column=1, sticky=W, pady=2, padx=19)
        self.password_field = Entry(label_frame,show='*',width =30)
        self.password_field.grid(row=2, column=2, sticky=W, padx=5,)
        # Label(label_frame, text='Annual Gross Salary : ', bg="cadetblue2", fg="midnightblue",
        #       font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=19)
        # self.gsalary_field = Entry(label_frame,width =30)
        # self.gsalary_field.grid(row=3, column=2, sticky=W, padx=5,)
        
        Button(label_frame, text="Log In", command=self.login, bg="midnightblue", fg="white",
               font="helvetica 9 bold").grid(row=4, column=2, sticky=E, padx=5, pady=5) 
    
    #end of first GUI window setup
    def login_check(self):
        for i in range(0,len(admins)):

            if (admins[i].username == self.username_field.get()) and (admins[i].password == self.password_field.get()):
                return True
        return False
    
    def login(self):
        if self.login_check():
            self.message['text'] ='Logged in'
            self.admin_window()

        else:
            self.message['text'] ='wroong'
   

    def admin_window(self):
        self.root.destroy()
        self.window = Tk()
        self.window.title('Sonar Locations')
        bg = PhotoImage(file = "bg_acc.png")            #Background added to window
        bg_label = Label(self.window, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        self.window.geometry("500x500")
        self.window.resizable(width=False, height = False)
        columns = ('id','location','safety')

        label_frame = LabelFrame(self.window, text='Admin', bg="cadetblue2", 
                                 fg ="midnightblue", font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Sonar ID: ', bg="cadetblue2", fg="midnightblue", 
              font="helvetica 9 bold").grid(row=0, column=1, sticky=W, pady=2, padx=15)
        self.id_field = Entry(label_frame)
        self.id_field.grid(row=0, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Sonar Location: ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=1, column=1, sticky=W, pady=2, padx=15)
        self.slocation_field = Entry(label_frame)
        self.slocation_field.grid(row=1, column=2, sticky=W, padx=5,)
        Label(label_frame, text='Safety: ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=15)
        self.safety_field = Entry(label_frame,width =30)
        self.safety_field.grid(row=3, column=2, sticky=W, padx=5,)        
        
        Button(label_frame, text='Add', command=lambda: self.add_sonar(), 
               bg = "midnightblue",fg="white", font ="helvetica 9 bold").grid(row=4, column= 2, sticky=E)
        
        self.messageArea()
        
        self.tree = ttk.Treeview(self.window, columns=columns,show='headings', style='Treeview')
        self.tree.grid(row=6, column = 0, columnspan = 1)
        self.tree.heading('id',text='Sonar ID', anchor=W)
        self.tree.heading('location',text='Location', anchor=W)
        self.tree.heading('safety',text='Safety', anchor=W)

        self.tree.column('id', stretch = False, width=125, minwidth=100)
        self.tree.column('location', stretch = False, width=120, minwidth=120)
        self.tree.column('safety', stretch = False, width=100, minwidth=100)


        self.scrollbar = Scrollbar(master = self.window, orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=1,columnspan=3,rowspan=3,sticky='sn')
        
        self.view_sonars()

        Button(text='Delete Sonar',command=self.deleteButtonClicked,
               bg='red',fg='white').grid(row=8,column=0,sticky=W,pady=15,padx=10)
        Button(text='Add Location',command=self.addLocationClicked,
               bg='purple',fg='white').grid(row=8,column=2,sticky=E)
        Button(self.window,text='Back',command=self.call_main,
               bg='orange',fg='Black', font="helvetica 9 bold").grid(row=9,column=0,sticky=W, pady=8, padx = 10)
        self.window.mainloop()
    
    def sid_check(self):
        if self.id_field.get().isnumeric() and len(self.id_field.get())>0:
            return True
        else:
            return False
    def slocation_check(self):
        if self.slocation_field.get().replace(" ","").isalpha() and len(self.slocation_field.get())>0:
            return True
        else:
            return False
    def safety_check(self):
        if self.safety_field.get().capitalize() == "Yes" or  self.safety_field.get().capitalize() == "No":
            return True
        else:
            return False
        


    #methods for Validation
    def add_sonar(self):
        if self.sid_check() and self.slocation_check() and self.safety_check():
            if (self.safety_field.get()).capitalize() == "Yes":
                safety = True
            else:
                safety = False
            sonar = Sonar()
            sonar.id = self.id_field.get()
            sonar.name = self.slocation_field.get().title()
            sonar.safety = self.safety_field.get().capitalize()
            sonars.append(sonar)

            self.message['text'] = 'New Sonar ID {} added'.format(self.id_field.get())
            self.view_sonars()
            self.id_field.delete(0, END)
            self.slocation_field.delete(0, END)
            self.safety_field.delete(0, END)
        else:
            tkinter.messagebox.showwarning('Input Error', 'ID must be numeric only. Sonar Location must only contain alphabets. Safety must be "Yes" or "No"')
    
    #Methods take user input and creates locations
    # def addLocation(self):
    #     global no_of_locations
    #     if self.locationCheck() and self.safetyCheck():
    #         locations.append(Location())
    #         if (self.safety_field.get()).capitalize() == "Yes":
    #             safety = True
    #         else:
    #             safety = False
    #         locations[no_of_locations].name = self.location_field.get().title()
    #         locations[no_of_locations].safety = self.safety_field.get()
    #         self.message['text'] = 'New location {} added'.format(self.location_field.get().title())
    #         no_of_locations += 1
    #         self.viewLocations()
    #         self.location_field.delete(0, END)
    #         self.safety_field.delete(0, END)
    #     else:
    #         self.message['text'] = 'Name must only contain alphabets. Safety must be "Yes" or "No"'
    

    #obtains index number of spot in the list  
    def match_sonar(self, search_id):
        for i in range (0,len(sonars)):
            if int(sonars[i].id) == search_id:
                return i
    
    #obtains index number of spot's account number
    def match_location(self, sonar_no, location):
        for i in range(0, len(sonars[sonar_no].locations)):
            if sonars[sonar_no].locations[i] == location:
                return i

    def view_sonars(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for i in range (0, len(sonars)):
            # if sonars[i].safety():
            #     safety = 'Yes'
            # else:
            #     safety = 'No'
            self.tree.insert('', 0, values= ('{}'.format(sonars[i].id), '{}'.format(sonars[i].name),
                                            '{}'.format(sonars[i].safety)))

    def delete_sonar(self):
        self.message['text']=''
        id = self.tree.item(self.tree.selection())['values'][0]
        sonar_index = self.match_sonar(id)
        if sonar_index>0:    
            for i in range(sonar_index,len(sonars)):
                sonars[i] = sonars[i+1]
        sonars.pop()
        self.message['text']='Sonar ID {} deleted'.format(id)
        self.view_sonars()
    
    #ensures program doesnt crash, and function to delete spot is called successfully
    def deleteButtonClicked(self):
        self.message['text'] = ''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No account selected.')
            return
        self.delete_sonar()
    
    def addLocationClicked(self):
        self.message['text']=''
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No Sonar selected.')
            return
        self.location_window()
    
    def viewLocationsmain(self):
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for i in range (0, no_of_locations):
            if locations[i].safety:
                safety = 'Safe'
            else:
                safety = 'Unsafe'
            self.tree.insert('', 0, values= ('{}'.format(locations[i].name), '{}'.format(safety)))
    

    # new window(GUI) to edit locations with sonar
    def location_window(self):
        sonar = self.tree.item(self.tree.selection())['values'][0]
        self.root.destroy()
        self.window = Tk()
        self.window.title('Locations')
        bg = PhotoImage(file = "bg_acc.png")            #Background added to window
        bg_label = Label(self.window, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        self.window.geometry("500x500")
        self.window.resizable(width=False, height = False)
        columns = ('locations')

        label_frame = LabelFrame(self.window, text='{}'.format(sonar), bg="cadetblue2", 
                                 fg ="midnightblue", font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Location Name: ', bg="cadetblue2", fg="midnightblue", 
              font="helvetica 9 bold").grid(row=0, column=1, sticky=W, pady=2, padx=15)
        self.loc_field = Entry(label_frame)
               
        Button(label_frame, text='Add', command= self.add_location(sonar, self.loc_field.get()), 
               bg = "midnightblue",fg="white", font ="helvetica 9 bold").grid(row=4, column= 2, sticky=E)
        
        #hereee


        self.tree = ttk.Treeview(self.window, columns=columns,show='headings', style='Treeview')
        self.tree.grid(row=6, column = 0, columnspan = 1)
        
        self.tree.heading('location',text='Location', anchor=W)
        self.tree.column('location', stretch = False, width=125, minwidth=100)   
        self.scrollbar = Scrollbar(master = self.window, orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=1,columnspan=3,rowspan=3,sticky='sn')
        
        
        
        sonar_index = self.match_sonar(sonar)
        
        self.viewLocations(sonar_index)
        #rows of table filled by every location of sonar
        Button(self.window,text='Delete Selected',command=lambda: self.deleteButtonClickedAcc(sonar),
               bg='red',fg='white', font ="helvetica 9 bold").grid(row=10,column=0 ,sticky=E, pady = 10) 
        Button(self.window,text='Back',command=self.admin_window,bg='orange',fg='Black', font ="helvetica 9 bold").grid(row=10,column=0,sticky=W, pady = 10)
        self.window.mainloop()
    
    

    def location_check(self):
        if self.loc_field.get().isalpha() and len(self.loc_field.get())>0:
            return True
        else:
            return False
    
    def add_location(self,sonar, name):
        #sonar = sonar number
        #name  = location 
        if self.location_check():
            sonar_index = self.match_sonar(sonar)
            sonars[sonar_index].locations.append(Location(name, sonars[sonar_index].safety))
            self.viewLocations(sonar_index)
            self.loc_field.delete(0, END)
        
        else:
            tkinter.messagebox.showwarning('Input Error', 'Name must only contain alphabets.')

    def delete_location(self, sonar):
        sonar_index = self.match_sonar(sonar)
        location = self.tree.item(self.tree.selection())['values'][0]
        location_index = self.match_location(sonar_index, location)
        sonars[sonar_index].delete_location(location_index)
        self.viewLocations(sonar_index)
                
    
    def viewLocations(self, sonar_idx):

        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for i in range (0,len(sonars[sonar_idx].locations)-1):
            self.tree.insert('',0, text = '', values=(sonars[sonar_idx].locations[i].name))

    #views table of updated balance at the end of every period(4 weeks)
    

    def deleteButtonClickedLoc(self,sonar):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No location selected.')
            return
        self.delete_location(sonar)
        
    # def logInGui():
    #     label_frame = LabelFrame(self.root, text='ADD LOCATION', bg="cadetblue2", fg="midnightblue",
    #                              font="helvetica 11 bold")
    #     label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
    #     Label(label_frame, text='Location : ', bg="cadetblue2", fg="midnightblue",
    #           font="helvetica 9 bold" ).grid(row=1, column=1, sticky=W, pady=2, padx=19)
    #     self.location_field = Entry(label_frame, width =30)            
    #     self.location_field.grid(row=1, column=2, sticky=W, padx=5,)
    #     Label(label_frame, text='Safety : ', bg="cadetblue2", fg="midnightblue",
    #           font="helvetica 9 bold").grid(row=2, column=1, sticky=W, pady=2, padx=19)
    #     self.safety_field = Entry(label_frame,width =30)
    #     self.safety_field.grid(row=2, column=2, sticky=W, padx=5,)
    #     # Label(label_frame, text='Annual Gross Salary : ', bg="cadetblue2", fg="midnightblue",
    #     #       font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=19)
    #     # self.gsalary_field = Entry(label_frame,width =30)
    #     # self.gsalary_field.grid(row=3, column=2, sticky=W, padx=5,)
        
    #     Button(label_frame, text="Log In", command=self.addLocation, bg="midnightblue", fg="white",
    #            font="helvetica 9 bold").grid(row=4, column=2, sticky=E, padx=5, pady=5) 
   

    
    #method to return to main window
    def call_main(self):
        self.window.destroy()
        root = Tk()
        root.title('Croc-Aware')
        bg = PhotoImage(file = "app_bgmain.png")
        bg_label = Label(root, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        application = GUI(root)
        root.geometry("800x500")
        root.mainloop()

    

if __name__ == '__main__':
    root = Tk()
    root.title('Croc-aware')
    bg = PhotoImage(file = "app_bgmain.png")
    bg_label = Label(root, image = bg)
    bg_label.place(x=0,y=0, relheight=1,relwidth=1)
    application = GUI(root)
    root.geometry("800x500")

    
    root.resizable(width=False, height=False)
    root.mainloop()