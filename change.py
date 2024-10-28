
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


locations_dict = {}
sonars =[]
admins=[]        #list to store admins of system

class Sonar():
    def __init__(self, id ='', name='', locations = [], safety=True):
        self.id = id
        self.name = name
        self.safety = safety
        self.locations = locations
    
    #add location object to list of locations
    def add_location(self, item):
        self.locations.append(item)
    
    def delete_location(self, loc):
        if int(loc)<len(self.locations)-1:    
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


#create a default admin
admins.append(Admin(username='admin', password= 'admin'))

class GUI(object):
    def __init__(self,root):
        self.root = root
        self.createGUI()
    
    def createGUI(self):
        self.createLabelFrame()
        self.createTreeView()
        self.createScrollbar()
        if len(locations_dict)>0:
            self.viewLocationsMain()
        
    
    #methods to setup widgets for a GUI     
    def createButtons(self):
        Button(text='Delete Location',command=self.deleteButtonClicked,
               bg='red',fg='white').grid(row=8,column=0,sticky=W,pady=15,padx=10)
        Button(text='Edit Location',command=self.addLocationClicked,
               bg='purple',fg='white').grid(row=8,column=2,sticky=E)

    def createTreeView(self):
        columns = ('location', 'safety')
        self.tree = ttk.Treeview(columns=columns, show='headings', style='Treeview')
        self.tree.grid(row=5,column=0, columnspan=1, pady=20, sticky='e')
        self.tree.heading('location',text='Location',anchor=W)
        self.tree.heading('safety',text='Safety',anchor=W)

        self.tree.column('location', stretch = False, width=200)
        self.tree.column('safety', stretch = False, width=100)

    def createScrollbar(self):
        self.scrollbar = Scrollbar(orient = 'vertical', command = self.tree.yview)
        self.scrollbar.grid(row = 5, column =1, padx=0, pady=20, sticky = "sn")

    def messageArea(self):
        self.message = Label(text='',fg='red')
        self.message.grid(row=3,column=0,sticky=W, padx= 10)
        
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
        
        Button(label_frame, text="Log In", command=self.login, bg="midnightblue", fg="white",
               font="helvetica 9 bold").grid(row=4, column=2, sticky=E, padx=5, pady=5) 
    
    def viewLocationsMain(self):

        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for place in locations_dict:
            if place.safety:
                output = 'Safe'
            else:
                output = 'Unsafe'                
            self.tree.insert('', 0, values= (place.name, output))

    #end of first GUI window setup
    def login_check(self):
        for i in range(0,len(admins)):

            if (admins[i].username == self.username_field.get()) and (admins[i].password == self.password_field.get()):
                return True
        return False
    
    def login(self):
        if self.login_check():
            self.admin_window()
        else:
            tkinter.messagebox.showwarning('Invalid Login','Username and password combination incorrect')


    def admin_window(self):
        self.root.destroy()
        self.windowad = Tk()
        self.windowad.title('Sonar Locations')
        bg = PhotoImage(file = "croc-aware-main\croc-aware-main\croc.png")            #Background added to window
        bg_label = Label(self.windowad, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        self.windowad.geometry("500x500")
        self.windowad.resizable(width=False, height = False)
        columns = ('id','location','safety')
        label_frame = LabelFrame(self.windowad, text='Admin', bg="cadetblue2", 
                                 fg ="midnightblue", font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Sonar ID: ', bg="cadetblue2", fg="midnightblue", 
              font="helvetica 9 bold").grid(row=0, column=1, sticky=W, pady=2, padx=15)
        self.id_field = Entry(label_frame,width =30)
        self.id_field.grid(row=0, column=2, sticky=W, padx=5)
        Label(label_frame, text='Sonar Location: ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=1, column=1, sticky=W, pady=2, padx=15)
        self.slocation_field = Entry(label_frame, width =30)
        self.slocation_field.grid(row=1, column=2, sticky=W, padx=5)
        Label(label_frame, text='Safety: ', bg="cadetblue2", fg="midnightblue",
              font="helvetica 9 bold").grid(row=3, column=1, sticky=W, pady=2, padx=15)
        self.safety_field = Entry(label_frame,width =30)
        self.safety_field.grid(row=3, column=2, sticky=W, padx=5)        
        
        Button(label_frame, text='Add', command=lambda: self.add_sonar(), 
               bg = "midnightblue",fg="white", font ="helvetica 9 bold").grid(row=4, column= 2, sticky=E)
        self.messageArea()
        
        self.tree = ttk.Treeview(self.windowad, columns=columns,show='headings', style='Treeview')
        self.tree.grid(row=6, column = 0, columnspan = 2, sticky='e')
        self.tree.heading('id',text='ID', anchor=W)
        self.tree.heading('location',text='Location', anchor=W)
        self.tree.heading('safety',text='Safety', anchor=W)

        self.tree.column('id', stretch = False, width=125, minwidth=100)
        self.tree.column('location', stretch = False, width=120, minwidth=120)
        self.tree.column('safety', stretch = False, width=100, minwidth=100)


        self.scrollbar = Scrollbar(master = self.windowad, orient='vertical',command=self.tree.yview)
        self.scrollbar.grid(row=6,column=1,sticky='sn')
        
        self.view_sonars()

        Button(text='Delete Sonar',command=lambda:self.deleteButtonClicked(),
               bg='red',fg='white', font ="helvetica 9 bold").grid(row=8,column=0,sticky=W,pady=15,padx=10)
        Button(text='Edit Locations',command=lambda:self.addLocationClicked(),
               bg='green',fg='white', font ="helvetica 9 bold").grid(row=8,column=0, columnspan=2, sticky=E)
        Button(text='Back',command=self.call_main,bg='black',fg='white', 
               font ="helvetica 9 bold").grid(row=9,column=0,sticky=W, pady = 10, padx=10)
        self.windowad.mainloop()
    
    #Functions to validate input

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

    #Ensures no copy of sonars created    
    def sonar_id_exists(self, search_id):
        for sonar in sonars:
            if int(sonar.id) == int(search_id):
                return True
        return False
    


    #methods for adding a sonar to list of sonars
    def add_sonar(self):
        if self.sid_check() and self.slocation_check() and self.safety_check():
            if not self.sonar_id_exists(self.id_field.get()):
                sonar = Sonar(locations=[])
                sonar.id = self.id_field.get()
                sonar.name = self.slocation_field.get().title()
                if self.safety_field.get().capitalize()=='Yes':
                    sonar.safety = True
                else:
                    sonar.safety = False
                sonars.append(sonar)

                self.message['text'] = 'New Sonar ID {} added'.format(self.id_field.get())
                self.view_sonars()
                self.id_field.delete(0, END)
                self.slocation_field.delete(0, END)
                self.safety_field.delete(0, END)
            else:
                tkinter.messagebox.showwarning('Sonar Exists','Sonar ID already exists. Please add a different one')
        else:
            tkinter.messagebox.showwarning('Input Error', 'ID must be numeric only. Sonar Location must only contain alphabets. Safety must be "Yes" or "No"')
    
    #obtains index number of sonar in the list 'sonars'  
    def match_sonar(self, search_id):
        for i in range (0,len(sonars)):
            if int(sonars[i].id) == int(search_id):
                return i
    
    #obtains index number of location number in sonar's list of locations
    def match_location(self, sonar_no, location):
        for i in range(0, len(sonars[sonar_no].locations)):
            if sonars[sonar_no].locations[i].name == location:
                return i

    #sonar list viewed in admin_window
    def view_sonars(self): 
        items = self.tree.get_children()
        for item in items:
            self.tree.delete(item)
        for i in range (0, len(sonars)):
            if sonars[i].safety:
                safety = 'Safe'
            else:
                safety = 'Unsafe'
            self.tree.insert('', 0, values= ('{}'.format(sonars[i].id),
                                             '{}'.format(sonars[i].name), safety))

    #function deletes sonar from list of sonars, unlinks to the locations.
    def delete_sonar(self):
        self.message['text']=''
        id = self.tree.item(self.tree.selection())['values'][0]
        sonar_index = self.match_sonar(id)
        for location in locations_dict:
            for i in range(len(locations_dict[location])):
                if i < len(locations_dict[location]):
                    if locations_dict[location][i] == sonars[sonar_index]:
                        if i<(len(locations_dict[location]))-1:
                            for j in range (i, len(locations_dict[location])-1):
                                locations_dict[location][j]=locations_dict[location][j+1]
                        locations_dict[location].pop()
                        self.location_safety(location)
                        len(locations_dict[location])
       
         
        self.empty_locations()
        if sonar_index<len(sonars)-1:
            for i in range(sonar_index,len(sonars)-1):
                sonars[i] = sonars[i+1]
        sonars.pop()
        self.message['text']='Sonar ID {} deleted'.format(id)
        self.view_sonars()
    
    # If location has no more connected sonars, it is 
    # deleted from the locations dictionary 
    def empty_locations(self):
        empty_locs = []
        for loc in locations_dict:    
            if len(locations_dict[loc]) == 0:
                empty_locs.append(loc)
        for loc in empty_locs:
            locations_dict.pop(loc)
                
    #functions ensure program doesnt crash, and functions are called successfully
    def deleteButtonClicked(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No sonar selected.')
            return
        self.delete_sonar()
    
    def addLocationClicked(self):
        try:
            self.tree.item(self.tree.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No sonar selected.')
            return
        self.location_window()


    # new window(GUI) to edit locations in each sonar
    def location_window(self):
        sonar = self.tree.item(self.tree.selection())['values'][0]
        title = self.tree.item(self.tree.selection())['values'][1]
        self.windowloc = Toplevel()
        self.windowloc.title(title)
        bgloc = PhotoImage(file = "croc-aware-main\loc.png")            #Background added to window
        bg_label = Label(self.windowloc, image= bgloc)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        self.windowloc.geometry("400x500")
        self.windowloc.resizable(width=False, height = False)
        columns = ('locations')

        label_frame = LabelFrame(self.windowloc, text='{}'.format(sonar), bg="cadetblue2", 
                                 fg ="midnightblue", font="helvetica 11 bold")
        label_frame.grid(row=0, column=0, padx=8, pady=8, sticky=W)
        Label(label_frame, text='Location Name: ', bg="cadetblue2", fg="midnightblue", 
              font="helvetica 9 bold").grid(row=0, column=1, sticky=W, pady=2, padx=15)
        self.loc_field = Entry(label_frame)
        self.loc_field.grid(row=0, column=2, sticky=W, padx=5)       
        Button(label_frame, text='Add', command=lambda: self.add_location(sonar, self.loc_field.get()), 
               bg = "midnightblue",fg="white", font ="helvetica 9 bold").grid(row=4, column= 2, sticky=E)
        

        self.treeloc = ttk.Treeview(self.windowloc, columns=columns,show='headings', style='Treeview')
        self.treeloc.grid(row=6, column = 0, columnspan = 1, sticky='e')
        
        self.treeloc.heading('locations',text='Location', anchor=W)
        self.treeloc.column('locations', stretch = False, width=250) 
        self.scrollbar = Scrollbar(master = self.windowloc, orient='vertical',command=self.treeloc.yview)
        self.scrollbar.grid(row=6,column=1,sticky='ns')
        
        sonar_index = self.match_sonar(sonar)
        
        self.viewLocations(sonar_index)
        #rows of table filled by every location of sonar
        Button(self.windowloc,text='Delete Selected',command=lambda: self.deleteButtonClickedLoc(sonar),
               bg='red',fg='white', font ="helvetica 9 bold").grid(row=10,column=0 ,sticky=E, pady = 10)
        self.windowloc.mainloop()
    
    

    def location_check(self):
        if self.loc_field.get().replace(" ","").isalpha() and len(self.loc_field.get())>0:
            return True
        else:
            return False
    
    #checks if same location object exists, 
    # returns the object if exists, else 0
    def location_object(self, loc_name):
        for place in locations_dict:
            if place.name == loc_name:
                return place
        return 0

    #Updates safety status of location according 
    # to the sonars they are dependent on.
    def location_safety(self, location_obj):
        safe = True
        for sonar in locations_dict[location_obj]:
            sonar_index = self.match_sonar(sonar.id)
            if sonars[sonar_index].safety == False:
                location_obj.safety = False
                safe = False
            if safe == True:
                location_obj.safety = True


    def add_location(self,sonar,name):
        if self.location_check():
            sonar_index = int(self.match_sonar(sonar)) #finds index number of sonar id in list of sonars
            if self.location_object(name) == 0: #make new location object
                new_loc=Location(name)
                locations_dict[new_loc] = []
            else:
                obj = self.location_object(name) # use existing location object if exists
                new_loc = obj

            if new_loc not in sonars[sonar_index].locations:

                sonars[sonar_index].add_location(new_loc)
                locations_dict[new_loc].append(sonars[sonar_index])   
            else:                
                tkinter.messagebox.showwarning('Error', 'Location already exists.')   
                              
            self.location_safety(new_loc)
            self.viewLocations(sonar_index)
            self.loc_field.delete(0, END)
        else:
            tkinter.messagebox.showwarning('Input Error', 'Name must only contain alphabets.')
            return
            

    def sonar_idx(self, sonar_id, loc):
        for i in range (0,len(locations_dict[loc])):
            if int(locations_dict[loc][i].id) == int(sonar_id):
                return i
    
    def delete_location(self, sonar):
        sonar_index = self.match_sonar(sonar)
        location = self.treeloc.item(self.treeloc.selection())['values'][0]
        location_index = self.match_location(sonar_index, location)
        sonars[sonar_index].delete_location(location_index)
        loc_obj = self.location_object(location)
        sonar_idx_locations= self.sonar_idx(sonar, loc_obj)
        if int(sonar_idx_locations)<len(locations_dict[loc_obj])-1:
            for i in range(sonar_idx_locations, len(locations_dict[loc_obj])-1):
                locations_dict[loc_obj][i] = locations_dict[loc_obj][i+1]
        locations_dict[loc_obj].pop()
        self.location_safety(loc_obj)
        self.empty_locations()
        self.viewLocations(sonar_index)              
    

    def viewLocations(self, sonar_idx):
        items = self.treeloc.get_children()
        for item in items:
            self.treeloc.delete(item)

        sonar = sonars[sonar_idx]
        for location in sonar.locations:
            self.treeloc.insert('', 'end', values=(location.name,))

    # def viewLocations(self, sonar_idx):
    #     items = self.treeloc.get_children()
    #     for item in items:
    #         self.treeloc.delete(item)
    #     for i in range (0,len(sonars[sonar_idx].locations)):
    #         location = sonars[sonar_idx].locations[i].name
    #         self.treeloc.insert('', 0, values= ('{}'.format(location)))

   

    def deleteButtonClickedLoc(self,sonar):
        try:
            self.treeloc.item(self.treeloc.selection())['values'][0]
        except IndexError as e:
            tkinter.messagebox.showwarning('Selection Error', 'No location selected.')
            return
        self.delete_location(sonar)
        
 
    #method to return to main window
    def call_main(self):
        self.windowad.destroy()
        root = Tk()
        root.title('Croc-Aware')
        bg = PhotoImage(file = "croc-aware-main\croc-aware-main\croc.png")
        bg_label = Label(root, image = bg)
        bg_label.place(x=0,y=0, relheight=1,relwidth=1)
        application = GUI(root)
        # root.attributes('-fullscreen', True)
        root.geometry("500x500")
        root.mainloop()

    

if __name__ == '__main__':
    root = Tk()
    root.title('Croc-aware')
    bg = PhotoImage(file = "croc-aware-main\croc-aware-main\croc.png")
    bg_label = Label(root, image = bg)
    bg_label.place(x=0,y=0, relheight=1,relwidth=1)
    application = GUI(root)
    # root.attributes('-fullscreen', True)
    root.geometry("500x500")

    
    root.resizable(width=False, height=False)
    root.mainloop()
