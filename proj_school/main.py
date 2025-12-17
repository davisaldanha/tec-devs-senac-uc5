from app.database.repositories import student as st

def main():
    
    
    for i in st.find_all_students():
        print(i)



if __name__ == "__main__":
    main()