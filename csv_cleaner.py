import pandas as pd

print("""
====================
    CSV Cleaner 
====================
    
    Check missing values      enter ---> 1
    Remove duplicates         enter ---> 2
    Clean the data            enter ---> 3
    Close                     enter ---> 4
      
-----------------------------------------------
""")

while True:
    data1 = input("Enter file name: ")
    
    if data1 == "close":
        print("✅ Closed!")
        break
    
    try:
        df = pd.read_csv(data1)
        print(df)
        
        while True:
            option = input("Choose: ")
            
            if option == "1":
                print("\n=== Missing Values ===")
                print(df.isnull().sum())

            elif option == "2":
                print("Duplicates:", df.duplicated().sum())
                df = df.drop_duplicates()
                print("✅ Duplicates removed!")

            elif option == "3":
                print("""
    1. Fill with 0s
    2. Delete rows
    3. Fill with the average
                """)
                clean = input("Choose: ")
                
                if clean == "1":
                    df = df.fillna(0)
                    print("✅ Filled with 0s!")
                elif clean == "2":
                    df = df.dropna()
                    print("✅ Rows deleted!")
                elif clean == "3":
                    df = df.fillna(df.mean(numeric_only=True))
                    print("✅ Filled with average!")
                else:
                    print("❌ Invalid option!")
                
                if clean in ["1", "2", "3"]:
                    save = input("Save file name: ")
                    df.to_csv(save, index=False)
                    print(f"✅ {save} saved!")

            elif option == "4":
                print("✅ Closed!")
                break
            
            else:
                print("❌ Invalid option!")
                
    except FileNotFoundError:
        print("❌ File not found!")
    
    else:
        break





