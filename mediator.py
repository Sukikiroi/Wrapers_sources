# this one gona excute the view

def show_available_views():
    print("Available views:")
    print("1. View 1  date et nom de offre")
    print("2. View 2")
    # Add more views as needed


def Interface():
     # Show available views
     show_available_views()
     # Get user input for CSV file path
     Select_view = input("Select view you want: ")
     return 1

def mediator(view):
    
    Interface()
    # request sql  conter mysql db
    data = []

    return data








#   user insert view


#   decision choose wraper


#   wraper insert data in db


#  mediator  excute the view and return data from database


