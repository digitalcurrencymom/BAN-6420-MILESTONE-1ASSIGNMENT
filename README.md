# BAN-6420-MILESTONE-1ASSIGNMENT
# Policy Management System for an Insurance Company

##  Project Overview
This project is a modular Python-based system designed to help an insurance company manage its core operations related to policyholders, insurance products, and payment processing. It allows policy managers to:
- Register, suspend, and reactivate policyholders
- Create, update, and suspend insurance products
- Process payments, send reminders, and apply penalties
- View detailed account summaries for each policyholder

The system demonstrates object-oriented programming principles and is structured for scalability and clarity.

##  Setup Instructions

### Requirements
- Python 3.7 or higher
- No external libraries required

### Installation
1. **Clone the repository** (if using GitHub):
   https://github.com/digitalcurrencymom/BAN-6420-MILESTONE-1ASSIGNMENT/tree/main

Extract the contents to a folder named policy_management

## How to Run the Demo
Open a terminal or command prompt

Navigate to the project directory:

cd policy_management
Run the main script:

python main.py
This will:

Create two policyholders

Assign them insurance products

Process payments

Display their account details

## File Descriptions
File Name	Description
policyholder.py	Defines the Policyholder class with methods to manage registration, status, products, and payments
product.py	Defines the Product class with methods to create, update, suspend, and remove products
payment.py	Defines the Payment class with methods to process payments, send reminders, and apply penalties
main.py	Demonstrates the system by creating sample data and displaying account summaries
README.md	Documentation for setup, usage, and project structure

## Assumptions and Limitations
## Assumptions
Each policyholder can have multiple products and payments

Payments are assumed to be successful once processed

Dates are manually entered as strings for simplicity

No database or persistent storage is used; all data is in-memory

## Limitations
No user interface (CLI or GUI); interactions are hardcoded in main.py

No error handling for invalid inputs or duplicate IDs

Not integrated with external payment gateways or APIs

Designed for demonstration purposes only, not production use

## Author
Kendra Onah
Developed as part of BAN-6420 Milestone Assignment 1
