def show_menu():
    print("\n==== SRE Diagnostic and Azure Deployment Tool ====")
    print("1. Run SRE Diagnostic")
    print("2. Parse Log file")
    print("3. Deploy Azure VM")
    print("4. Exit")


def main():

        while True:

            show_menu()
            choice = input("\nEnter your choice:")

            if choice == '1':
                print("\nDiagnostics feature coming soon...")

            elif choice == '2':
                print("\nLog parsing feature coming soon...")
                
            elif choice == '3':
                    print("\nAzure VM deployment feature coming soon...")

            elif choice == '4':
                 print("\nGoodbye!")

                 break
            else: print("Invalid choice. Try again.")


if __name__ == "__main__":
     main()