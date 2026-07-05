import subprocess
import json
import os
from datetime import datetime


REPORT_DIR = "reports"
HISTORY_FILE = "reports/metrics_history.json"


RESOURCE_GROUP = "rg-project0-sre"
VM_NAME = "project0-vm"
LOCATION = "canadaeast"
VM_SIZE = "Standard_B2ats_v2"
ADMIN_USERNAME = "azureuser"



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


     report = {
        "timestamp": str(datetime.now()),
        "cpu_info": cpu_info,
        "memory_info": memory_info,
        "disk_info": disk_info,
        "network_info": network_info
    }

     save_report(report)




def save_report(report):
    os.makedirs(REPORT_DIR, exist_ok=True)

    history =[]

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as file:
                
            try:
                     history = json.load(file)

            except json.JSONDecodeError:
                     history = []

        history.append(report)
     
        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

        print("\nReport saved succesfully.")


def parse_log_file():
     log_path = input("\nEnter the log file path")

     if not os.path.exists(log_path):
          print("\nLog file not found.")
          return
     
     total_lines = 0
     error_count = 0
     status_counts = {}


     with open(log_path, "r") as file:
          for line in file:
               total_lines += 1
               parts = line.split()

               if len(parts) >= 9:
                    status_code = parts[8]

                    status_counts[status_code] = status_counts.get(status_code, 0) + 1

                    if status_code.startswith("4") or status_code.startswith("5"):
                         error_count += 1


     print("\n ==== LOG ANALYSIS REPORT ====")
     print(f"Log file: {log_path}")
     print(f"Total lines analyzed: {total_lines}")
     print(f"Total error responses: {error_count}")

     print("\n --- Status Code Frequencies ---")
     for code, count in status_counts.items():
          print(f"{code}: {count}")




def check_azure_login():
     print("\nChecking Azure login status...")

     output = run_command("az account show")

     if output.startswith("ERROR"):
          print("\nYou are not logged in to Azure.")
          print("Run this command first:")
          print("az login")
          return False
     
     print("Azure login verified")
     return True


def deploy_azure_vm():
    print("\nWARNING: This will create Azure cloud resources.")
    confirmation = input("Type YES to continue deployment: ")

    if confirmation != "YES":
        print("Deployment cancelled.")
        return

    if not check_azure_login():
        return

    print("\nCreating Azure resource group...")
    group_command = (
        f"az group create "
        f"--name {RESOURCE_GROUP} "
        f"--location {LOCATION}"
    )
    group_output = run_command(group_command)
    print(group_output)

    if group_output.startswith("ERROR"):
        print("Resource group creation failed. Stopping deployment.")
        return

    print("\nCreating Azure VM with Standard_B2ats_v2 and Standard HDD...")
    vm_command = (
        f"az vm create "
        f"--resource-group {RESOURCE_GROUP} "
        f"--name {VM_NAME} "
        f"--image Ubuntu2204 "
        f"--size {VM_SIZE} "
        f"--admin-username {ADMIN_USERNAME} "
        f"--generate-ssh-keys "
        f"--storage-sku Standard_LRS "
        f"--public-ip-sku Standard"
    )
    vm_output = run_command(vm_command)
    print(vm_output)

    if vm_output.startswith("ERROR"):
        print("VM creation failed. Stopping deployment.")
        return

    print("\nConfiguring auto-shutdown for 18:00...")
    shutdown_command = (
        f"az vm auto-shutdown "
        f"--resource-group {RESOURCE_GROUP} "
        f"--name {VM_NAME} "
        f"--time 1800"
    )
    shutdown_output = run_command(shutdown_command)
    print(shutdown_output)

    if shutdown_output.startswith("ERROR"):
        print("Auto-shutdown configuration failed.")
        return

    print("\nAzure VM deployment finished.")
    print("When you are done, run ./teardown.sh to delete the resources.")



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
               parse_log_file()
                
            elif choice == '3':
                    deploy_azure_vm()

            elif choice == '4':
                 print("\nGoodbye!")

                 break
            else: print("Invalid choice. Try again.")
if __name__ == "__main__":
     main()