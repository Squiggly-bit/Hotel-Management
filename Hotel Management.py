#!/usr/bin/env python
# coding: utf-8

# In[1]:


luxury_room = {
    f"Room.no {1}":"Vacant",
    f"Room.no {2}":"Vacant",
    f"Room.no {3}":"Vacant",
    f"Room.no {4}":"Vacant"
}

normal_room = {
    f"Room.no {1}":"Vacant",
    f"Room.no {2}":"Vacant",
    f"Room.no {3}":"Vacant",
    f"Room.no {4}":"Vacant"
    
}

restaurant = {
    f"Table.no {1}":"Vacant",
    f"Table.no {2}":"Vacant",
    f"Table.no {3}":"Vacant",
    f"Table.no {4}":"Vacant"
}

menu = {
    "Pizza":250,
    "Burger":150,
    "Pasta": 200
}




# In[2]:


class hotel_2:
    
    def __init__ (self):
        self.name_cus = input("Enter customer name: ")
        self.recep = int(input("Enter (1-Book Room, 2-Check out, 3-Restaurant): "))
        self.bill = 0
        
    def manage_2(self):
        if self.recep == 1:
            room_type = int(input("Enter type of room (1-Luxury or 2-Normal): "))
            
            if room_type==1: 
                for i in range(1,len(luxury_room)+1):
                    if luxury_room[f"Room.no {i}"]=="Vacant":
                        luxury_room[f"Room.no {i}"] = f"Booked by {self.name_cus}"
                        print(f"Room.no {i} is now booked by {self.name_cus}")
                        break
                else:
                    print("No room is vacant")
            elif room_type==2:
                for i in range(1,len(normal_room)+1):
                    if normal_room[f"Room.no {i}"]=="Vacant":
                        normal_room[f"Room.no {i}"] = f"Booked by {self.name_cus}"
                        print(f"Room.no {i} is now booked by {self.name_cus}")
                        break
                else:
                    print("No room is vacant")
                    
                    
# 2                    
        elif self.recep == 2:
            room_type = int(input("Enter type of room (1-Luxury or 2-Normal): "))
            cost_luxury = 3000
            cost_normal = 1000
            bill_room = 1
            days_booked = int(input("Enter no. of days room was booked: "))
            
            if room_type==1:
                bill_room = days_booked * cost_luxury
                
                for i in range(1,len(luxury_room)+1):
                    if luxury_room[f"Room.no {i}"] == f"Booked by {self.name_cus}":
                        print(f"Total bill for Luxury room booked for {days_booked} days is {bill_room}")
                        luxury_room[f"Room.no {i}"] = "Vacant"
                        break
                else:
                    print(f"No customer by the name {self.name_cus}")
                bill_room = 0
                
            elif room_type == 2:
                bill_room = days_booked * cost_normal

                for i in range(1,len(normal_room)+1):
                    if normal_room[f"Room.no {i}"] == f"Booked by {self.name_cus}":
                        print(f"Total bill for Normal room booked for {days_booked} days is {bill_room}")
                        normal_room[f"Room.no {i}"] = "Vacant"
                        break
                else:
                    print(f"No customer by the name {self.name_cus}")
                bill_room = 0
                    
                    
# 3                
        elif self.recep == 3:
            bill = 0
            for i in range(1,len(restaurant)+1):
                if restaurant[f"Table.no {i}"]=="Vacant":
                    restaurant[f"Table.no {i}"] = f"Booked by {self.name_cus}"
                    print(f"Table.no {i} is now booked by {self.name_cus}")

                    
                    print(menu)
                    order = int(input("Enter no. of dishes you want: "))
                    for i in range(1,order+1):
                        order_2 = input("Enter Dish: ")
                        if order_2 == "Pizza":
                            bill += menu["Pizza"]
                        if order_2 == "Burger":
                            bill += menu["Burger"]
                        if order_2 == "Pasta":
                            bill += menu["Pasta"]

                    print(f"Total bill is {bill}")
                    break
            else:
                print("No table is vacant")
            bill = 0


# In[6]:


h = hotel_2()
h.manage_2()


# In[ ]:




