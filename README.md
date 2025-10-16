## Policy Management System for an Insurance Company
##  Project Overview
This Python-based system helps an insurance company manage its core operations involving policyholders, insurance products, and payments. It is designed to demonstrate object-oriented programming principles and modular architecture.

Key Features:

Register, suspend, and reactivate policyholders

Create, update, and suspend insurance products

Process payments, send reminders, and apply penalties

Display detailed account summaries for each policyholder

## Setup Instructions
Requirements
Python 3.7 or higher

No external libraries required

## Installation
Clone the repository:

git clone https://github.com/digitalcurrencymom/BAN-6420-MILESTONE-1ASSIGNMENT.git
Extract or navigate to the folder named policy_management

## How to Run the Demo
Open a terminal or command prompt

Navigate to the project directory:

cd policy_management
Run the main script:


python main.py
Demo Actions:

Creates two policyholders

Assigns them insurance products

Processes payments

Displays their account details

## File Descriptions
File Name	Description
policyholder.py	Manages policyholder registration, status changes, product assignments, and payment history
product.py	Handles creation, updates, suspension, and removal of insurance products
payment.py	Processes payments, sends reminders, and applies penalties
main.py	Demonstrates system functionality with sample data
README.md	Documentation for setup, usage, and project structure

##  Assumptions and Limitations
## Assumptions
Each policyholder can hold multiple products and make multiple payments

Payments are assumed successful once processed

Dates are manually entered as strings for simplicity

All data is stored in-memory (no database integration)

## Limitations
No user interface (CLI or GUI); interactions are hardcoded in main.py

No error handling for invalid inputs or duplicate IDs

Not integrated with external payment gateways or APIs

Intended for demonstration purposes only, not production use

## Author
Kendra Onah
Developed as part of BAN-6420 Milestone Assignment 1
