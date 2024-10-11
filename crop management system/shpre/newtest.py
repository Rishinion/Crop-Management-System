from tkinter import *
import tkinter as ttk
import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk
from tkinter.ttk import Combobox
# Function to get data from entry boxes
def get_data():
    # Retrieve data from entry boxes
    User_ID = int(entry_user_id.get())
    Product_ID = int(entry_product_id.get())
    Gender = int(entry_gender.get())
    Age = int(entry_age.get())
    Occupation = int(entry_occupation.get())
    City_Category = int(entry_city_category.get())
    Stay_In_Current_City_Years = int(entry_stay_in_current_city_years.get())
    Marital_Status = int(entry_marital_status.get())
    Product_Category_1 = int(entry_product_category_1.get())
    Product_Category_2 = int(entry_product_category_2.get())
    Product_Category_3 = int(entry_product_category_3.get())
    
    # Do something with the data
    
    print("User ID:", User_ID)
    print("Product ID:", Product_ID)
    print("Gender:", Gender)
    print("Age:", Age)
    print("Occupation:", Occupation)
    print("City Category:", City_Category)
    print("Stay in Current City Years:", Stay_In_Current_City_Years)
    print("Marital Status:", Marital_Status)
    print("Product Category 1:", Product_Category_1)
    print("Product Category 2:", Product_Category_2)
    print("Product Category 3:", Product_Category_3)

   # features = [[User_ID, Product_ID, Gender, Age, Occupation, City_Category, Stay_In_Current_City_Years, Marital_Status, Product_Category_1, Product_Category_2, Product_Category_3]]

    # Use your model directly
   # predicted_sales = model_prediction(features, rr_R)

   # print(f'The black friday sales is {predicted_sales}')
    
    
    
   #sales.insert(0,f'Rs:{predicted_sales}')
    
# Create the main window
window = tk.Tk()
window.title("My Window")
window.geometry("1000x600")
"""background_image = Image.open("img.jpg")  # Replace "example_background_image.png" with your image file path
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)"""

# Create a frame
frame = tk.Frame(window, width=400, height=400, bg="lightgray")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


"""cropped_image = background_image.crop((300, 150, 700, 700))# Adjust the crop area as needed
frame_image = ImageTk.PhotoImage(cropped_image)
frame_label = tk.Label(frame, image=frame_image)
frame_label.place(x=0, y=0, relwidth=1, relheight=1)"""

# Create entry boxes
tk.Label(frame, text="User ID:",font = ('Helvetica', 12), bg="lightgray").grid(row=0, column=0, padx=5, pady=5)
entry_user_id = tk.Entry(frame,font = ('Helvetica', 12))
entry_user_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Product ID:",font = ('Helvetica', 12), bg="lightgray").grid(row=1, column=0, padx=5, pady=5)
entry_product_id = tk.Entry(frame,font = ('Helvetica', 12))
entry_product_id.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Gender:",font = ('Helvetica', 12), bg="lightgray").grid(row=2, column=0, padx=5, pady=5)
entry_gender = tk.Entry(frame,font = ('Helvetica', 12))
entry_gender.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Age:",font = ('Helvetica', 12), bg="lightgray").grid(row=3, column=0, padx=5, pady=5)
entry_age = tk.Entry(frame,font = ('Helvetica', 12))
entry_age.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame, text="Occupation:",font = ('Helvetica', 12), bg="lightgray").grid(row=4, column=0, padx=5, pady=5)
entry_occupation = tk.Entry(frame,font = ('Helvetica', 12))
entry_occupation.grid(row=4, column=1, padx=5, pady=5)

tk.Label(frame, text="City Category:",font = ('Helvetica', 12), bg="lightgray").grid(row=5, column=0, padx=5, pady=5)
entry_city_category = tk.Entry(frame,font = ('Helvetica', 12))
entry_city_category.grid(row=5, column=1, padx=5, pady=5)

tk.Label(frame, text="Stay in Current City Years:",font = ('Helvetica', 12), bg="lightgray").grid(row=6, column=0, padx=5, pady=5)
entry_stay_in_current_city_years = tk.Entry(frame,font = ('Helvetica', 12))
entry_stay_in_current_city_years.grid(row=6, column=1, padx=5, pady=5)

tk.Label(frame, text="Marital Status:",font = ('Helvetica', 12), bg="lightgray").grid(row=7, column=0, padx=5, pady=5)
entry_marital_status = tk.Entry(frame,font = ('Helvetica', 12))
entry_marital_status.grid(row=7, column=1, padx=5, pady=5)

tk.Label(frame, text="Product Category 1:",font = ('Helvetica', 12), bg="lightgray").grid(row=8, column=0, padx=5, pady=5)
entry_product_category_1 = tk.Entry(frame,font = ('Helvetica', 12))
entry_product_category_1.grid(row=8, column=1, padx=5, pady=5)

tk.Label(frame, text="Product Category 2:",font = ('Helvetica', 12), bg="lightgray").grid(row=9, column=0, padx=5, pady=5)
entry_product_category_2 = tk.Entry(frame,font = ('Helvetica', 12))
entry_product_category_2.grid(row=9, column=1, padx=5, pady=5)

tk.Label(frame, text="Product Category 3:",font = ('Helvetica', 12), bg="lightgray").grid(row=10, column=0, padx=5, pady=5)
entry_product_category_3 = tk.Entry(frame,font = ('Helvetica', 12))
entry_product_category_3.grid(row=10, column=1, padx=5, pady=5)





# Define the products
pro = ('Product-1', 'Product-2', 'Product-3', 'Product-4')
dis=('20%','30%','40%','50%')



# Define StringVars to hold the values of the selected items and set the default values
selected_product1 = tk.StringVar(value="Select Product")
selected_product2 = tk.StringVar(value="Select Discount")

# Create the first Combobox and associate it with the first StringVar
combo1 = ttk.Combobox(frame, values=pro, width=15, textvariable=selected_product1,state='readonly')
combo1.grid(row=11, column=0, padx=5, pady=5)

# Create the second Combobox and associate it with the second StringVar
combo2 = ttk.Combobox(frame, values=dis, width=15, textvariable=selected_product2,state='readonly')
combo2.grid(row=11, column=1, padx=5, pady=5)

# Define a function to get the value of the first Combobox selection
def on_combobox1_select(event):
    selected_value1 = selected_product1.get()
    print("Selected Product 1:", selected_value1)
    # You can also store this value in another variable if needed
    selected_value_variable1 = selected_value1
    return selected_value_variable1

# Define a function to get the value of the second Combobox selection
def on_combobox2_select(event):
    selected_value2 = selected_product2.get()
    int_value = int(selected_value2.strip('%'))
    print("Selected Product 2:", int_value)
    # You can also store this value in another variable if needed
    selected_value_variable2 = int_value
    return selected_value_variable2








# Create the submit button
submit_button = tk.Button(frame, text="Submit", command=get_data).grid(row=12,column=1,padx=5, pady=15)

tk.Label(frame, text="SALES OF:").grid(row=14, column=0,padx=10, pady=25)
sales = tk.Entry(frame)
sales.grid(row=14, column=1,padx=10, pady=25)

# Start the application
window.mainloop()