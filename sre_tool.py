import subprocess


def run_command(command):
    try: 
        result = subprocess.run(
          command,
          shell=True,
          text=True,
          capture_output=True,
          check=True
     )
          
        return result.stdout.strip()

    except subprocess.CalledProcessError as error:
        return f"ERROR: {error.stderr.strip()}"


def run_diagnostic():
     print("\nRunning local system diagnostic...")
     
     cpu_info = run_command("ps aux --sort=-%cpu | head -n 6")
     memory_info = run_command("free -h")
     disk_info = run_command("df -h")
     network_info = run_command("ss -tuln")

     print(" ==== LOCAL SYSTEM DIAGNOSTIC REPORT ====")

     print("\n--- Top CPU Processes ---")
     print(cpu_info)

     print("\n--- Memory Usage ---")
     print(memory_info)

     print("\n--- Disk Usage ---")
     print(disk_info)

     print("\n--- Active Network Connections ---")
     print(network_info)


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
                run_diagnostic()

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