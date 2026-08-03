




import pandas as pd

print("""
           ╔══════════════════════════════════╗
           ║        CSV CLEANER TOOL          ║
           ╚══════════════════════════════════╝

**********************************************************

        Check missing values             Enter  →  1
        Remove duplicates                Enter  →  2
        Clean the data                   Enter  →  3
        Close                            Enter  →  4

***********************************************************

Type 'close' anytime at the file prompt to exit.
""")

while True:
    data1 = input("Enter file name: ").strip()

    if data1.lower() == "close":
        print("✅ Closed!")
        break

    try:
        df = pd.read_csv(data1, encoding="utf-8-sig")
        print(df)

        while True:
            option = input("Choose: ")

            if option == "1":
                print("\n=== Missing Values ===")
                print(df.isnull().sum())

            elif option == "2":
                dup_count = df.duplicated().sum()
                if dup_count == 0:
                    print("✅ No duplicates found!")
                else:
                    df = df.drop_duplicates()
                    print(f"✅ {dup_count} duplicate row(s) removed!")
                    save = input("Save file name: ").strip()
                    if save:
                        df.to_csv(save, index=False)
                        print(f"✅ {save} saved!")
                    else:
                        print("⚠️  Not saved — changes only apply to this session.")

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
                    print("✅ Filled with average! (non-numeric columns left unchanged)")
                else:
                    print("❌ Invalid option!")

                if clean in ["1", "2", "3"]:
                    save = input("Save file name: ").strip()
                    if save:
                        df.to_csv(save, index=False)
                        print(f"✅ {save} saved!")
                    else:
                        print("⚠️  Not saved — changes only apply to this session.")

            elif option == "4":
                print("✅ Closed!")
                break

            else:
                print("❌ Invalid option!")

    except FileNotFoundError:
        print("❌ File not found!")
    except Exception as e:
        print(f"❌ Error reading file: {e}")

    else:
        break

