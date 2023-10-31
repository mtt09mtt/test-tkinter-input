import streamlit as st
import tkinter as tk
from tkinter import filedialog # Tkinter version 8.6 on the local


# Page configuration
st.set_page_config(page_title="Test tkinter Input", page_icon=":camel:", layout='wide', initial_sidebar_state='expanded')
st.title("Test tkinter Input")

# tkinter full file name picker
def file_picker(button_label, button_holder, filetypes):
    # Set up tkinter
    root = tk.Tk()
    root.withdraw()    
    # Make file picker dialog appears on top of other windows
    root.wm_attributes('-topmost', 1)
    
    try:
        clicked = button_holder.button(button_label)           
        if clicked: 
            full_path_fileName = filedialog.askopenfilename(master=root, filetypes=filetypes) 
    except:
        pass
    return full_path_fileName
       
def main_entry():   
    try:
        # Put the button on the sidebar
        button_holder = st.sidebar.empty()    
        # Define file types
        filetypes = [("ESRI shapefile", "*.shp *.SHP")]  
        full_fileName = file_picker(button_label="Please select a shapefile", button_holder=button_holder, filetypes=filetypes)
        # Write out picked file name
        st.write(full_fileName) 
    except:
        pass

    
if __name__ == "__main__":
    main_entry()
      