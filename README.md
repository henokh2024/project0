# Project 0: SRE Diagnostic and Automated VM Deployment Tool

## Overview

This is a python-based SRE tool that performs two main tasks:

1. Runs local Linux system diagnostics.
2. Automates Azure virtual machine deployment using Azure CLI.

The goal of the project is to practice python automation, Linux diagnostics, Git version control, azur CLI provisoning, cloud resource cleanup.


#Features

### 1. Local System Diagnostics

The tool collects local system information using Linux commands:

-CPU usage using `ps`
-memory usage using `free`
-Disk usage using `df`
Network connections using `ss`

The diagnostic ressults are displayed in the terminal and saved to a JSON history file.

### 2. Log File parsing

The tool can read a log file and calculate:

_Tlotal lines analyzed
-HTTP status code frequencies
-Total error responses
-4xx client errors
-5xx server errors

### 3. Azure VM Deployment

-verify Azure login
-create an Azure resource group
-Deploy an Ubuntu virtual machine
-use Standard HDD storage
-Configure auto-shutdown at 18:00

### 4. Teardown Routine

The project includes a Bash script called teardown.sh that deletes the Azure resource group using: 
```bash
az group delete
