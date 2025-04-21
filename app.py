import streamlit as st

# Initialize global data using session state
if "luxury_room" not in st.session_state:
    st.session_state.luxury_room = {f"Room.no {i}": "Vacant" for i in range(1, 6)}

if "normal_room" not in st.session_state:
    st.session_state.normal_room = {f"Room.no {i}": "Vacant" for i in range(1, 6)}

if "restaurant" not in st.session_state:
    st.session_state.restaurant = {f"Table.no {i}": "Vacant" for i in range(1, 6)}

menu = {"Pizza": 500, "Burger": 300, "Pasta": 400}

# Title
st.title("🏨 Hotel Management System")

# Input customer name
name_cus = st.text_input("👤 Enter customer name:")

# Main operation selection
recep = st.selectbox("Choose a service:", ["Select", "Book Room", "Check Out", "Restaurant"])

# --- Room Booking ---
def book_room():
    room_type = st.selectbox("Select room type:", ["Luxury", "Normal"])
    if st.button("Book Room"):
        room_dict = st.session_state.luxury_room if room_type == "Luxury" else st.session_state.normal_room
        for room, status in room_dict.items():
            if status == "Vacant":
                room_dict[room] = f"Booked by {name_cus}"
                st.success(f"{room} is now booked by {name_cus}")
                break
        else:
            st.error(f"No {room_type} rooms are vacant.")

# --- Room Check-Out ---
def check_out():
    room_type = st.selectbox("Select room type:", ["Luxury", "Normal"])
    days_booked = st.number_input("Enter number of days booked:", min_value=1, step=1)
    if st.button("Check Out"):
        cost = 3000 if room_type == "Luxury" else 1000
        room_dict = st.session_state.luxury_room if room_type == "Luxury" else st.session_state.normal_room
        for room, status in room_dict.items():
            if status == f"Booked by {name_cus}":
                bill = days_booked * cost
                st.success(f"{room} checkout successful. Total bill: ₹{bill}")
                room_dict[room] = "Vacant"
                break
        else:
            st.error(f"No booking found under {name_cus} in {room_type} rooms.")

# --- Restaurant Booking and Order ---
def restaurant_service():
    if st.button("Book Table"):
        for table, status in st.session_state.restaurant.items():
            if status == "Vacant":
                st.session_state.restaurant[table] = f"Booked by {name_cus}"
                st.success(f"{table} is now booked by {name_cus}")
                break
        else:
            st.error("No tables available.")

    st.subheader("🍽️ Menu")
    for dish, price in menu.items():
        st.write(f"{dish}: ₹{price}")

    st.subheader("🧾 Place Your Order")
    order_count = st.number_input("Number of dishes:", min_value=1, max_value=10, step=1)
    total_bill = 0
    selected_dishes = []

    for i in range(order_count):
        dish = st.selectbox(f"Select Dish {i+1}:", list(menu.keys()), key=f"dish_{i}")
        selected_dishes.append(dish)
        total_bill += menu[dish]

    if st.button("Calculate Bill"):
        st.success(f"Total bill: ₹{total_bill}")
        st.write("You ordered:")
        for dish in selected_dishes:
            st.write(f"- {dish}: ₹{menu[dish]}")

# --- Show Status ---
def show_status():
    st.subheader("📊 Current Room and Table Status")
    st.write("🛏️ Luxury Rooms")
    for room, status in st.session_state.luxury_room.items():
        st.write(f"{room}: {status}")
    
    st.write("🛏️ Normal Rooms")
    for room, status in st.session_state.normal_room.items():
        st.write(f"{room}: {status}")

    st.write("🍴 Restaurant Tables")
    for table, status in st.session_state.restaurant.items():
        st.write(f"{table}: {status}")

    if st.button("Clear All Bookings"):
        for d in [st.session_state.luxury_room, st.session_state.normal_room, st.session_state.restaurant]:
            for key in d:
                d[key] = "Vacant"
        st.success("All bookings cleared!")

# Run section based on selection
if recep == "Book Room":
    if name_cus:
        book_room()
    else:
        st.warning("Please enter customer name.")
elif recep == "Check Out":
    if name_cus:
        check_out()
    else:
        st.warning("Please enter customer name.")
elif recep == "Restaurant":
    if name_cus:
        restaurant_service()
        
    else:
        st.warning("Please enter customer name.")

with st.expander("📊 View Current Room & Table Status"):
    show_status()
