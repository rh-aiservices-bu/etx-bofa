NO_CONTENT_HERE
---
```
This manual contains proprietary and confidential information of Bank of America Merrill Lynch and was prepared by the staff of Bank of America Merrill Lynch. “Bank of America Merrill Lynch” is the marketing name for the global banking and global markets businesses of Bank of America Corporation.

This user guide may not be reproduced or disclosed to others in whole or in part without the written permission of Bank of America Merrill Lynch. Permitted reproductions shall bear this notice and the Bank of America copyright notice. The user of this user guide acknowledges the rights of Bank of America Merrill Lynch in the contents and agrees to maintain this user guide and its contents in confidence.

Bank of America – Member FDIC

©2018 Bank of America Corporation

All rights reserved. None of the enclosed material may be reproduced or published without permission of Bank of America.
```
---
# Contents

## Overview
- Storage and Destruction .................................................................................................................. 7
- Exception Items ............................................................................................................................... 8
- Remote Deposit Same Day Ledger Credit Cut-off Times ................................................................. 8

## Before You Begin .......................................................................................................................... 10
- Prerequisites .................................................................................................................................. 10
- Enroll in Web-Based Training ......................................................................................................... 10
- Confirm Workstation Requirements ............................................................................................... 10
- Confirm Remote Deposit Entitlement ............................................................................................ 11
- Review the Welcome Page ............................................................................................................. 11
- User Roles and Functions ............................................................................................................... 12

## Performing Administrative Functions ......................................................................................... 13

### Account Groups .......................................................................................................................... 14
- Modifying an Account Group .......................................................................................................... 17
- Deleting an Account Group ............................................................................................................ 18

### Users .......................................................................................................................................... 19
- Adding a New User ........................................................................................................................ 19
- Modifying an Existing User ............................................................................................................. 23
- Deleting an Existing User ................................................................................................................ 25

### Rules .......................................................................................................................................... 27
- Creating a Rule .............................................................................................................................. 28
- Creating a New Rule Account ......................................................................................................... 29
- Editing a Rule Account ................................................................................................................... 30
- Deleting a Rule Account ................................................................................................................. 31

### Custom Fields ............................................................................................................................ 32
- Creating a Custom Field ................................................................................................................. 33
- Creating an Auto-Complete Custom Field ...................................................................................... 34
- Assigning a Custom Field to a Depository Account ........................................................................ 36
- Editing Custom Fields .................................................................................................................... 39
- Deleting Custom Fields .................................................................................................................. 40

### Customer Preferences ............................................................................................................... 41
- Editing Lists .................................................................................................................................... 42
- Editing Optional Fields ................................................................................................................... 43
---
Editing Report Preferences .................................................................................................................. 43  
Virtual Endorsements .......................................................................................................................... 45  

Exiting the Remote Deposit Application ............................................................................................. 47  

CashPro Mobile Deposit ...................................................................................................................... 48  
Prerequisites ........................................................................................................................................ 48  
User Entitlement to CashPro Remote Deposit .................................................................................... 48  
User Entitlement to CashPro Mobile ................................................................................................... 48  
Downloading CashPro Mobile ............................................................................................................. 48  
Assigning User Roles for Mobile Access .............................................................................................. 48  

Support for Remote Deposit ................................................................................................................ 49  
User Guides .......................................................................................................................................... 49  
Help Tips ............................................................................................................................................... 49  
Technical Support ................................................................................................................................. 49  
Troubleshooting, Login, and Authentication Errors ............................................................................ 50  
Remote Deposit Frequently Asked Questions .................................................................................... 51  

Appendix .............................................................................................................................................. 54  
User Roles and Functions ..................................................................................................................... 54  
Custom Field Formats .......................................................................................................................... 56  
Deposit Status Types ............................................................................................................................ 57  
Icons ...................................................................................................................................................... 58  
Report Options ..................................................................................................................................... 59  
Research Options ................................................................................................................................. 61
---
# Overview

The purpose of this guide is to serve as a reference for Bank of America Merrill Lynch's CashPro® Remote Deposit application. This user guide focuses on the administration tab and functions. There are separate guides for the non-Administrator roles, functions, and Remittance processing. All screen shots are for illustrative purposes only and may vary based on your setup. Confidential data is intentionally masked herein.

CashPro® Remote Deposit is a Web-based application that enables companies to make electronic deposits from their desktops using a bank provided scanner. The CashPro Mobile app can also be used on an Apple® iOS or Android® device to deposit checks into Remote Deposit entitled accounts. (Note: CashPro Mobile is currently not available for Canadian clients). Remote Deposit users can scan and capture images and MICR data of:

- U.S. (USD) dollar items drawn on U.S. banks
- U.S. (USD) dollar items drawn on Canadian banks
- Canadian (CAD) dollar items drawn on Canadian banks

and transmit that data to Bank of America using a secure Internet connection. Items must be deposited to the appropriate CAD and/or USD account.

Clients using Bank of America's Remote Deposit application can:

- Scan and capture images and MICR data of U.S. dollar items, drawn on U.S. domiciled accounts; these include personal, business, cashier checks, traveler's checks, and money orders. Items that are drawn on a US domiciled accounts and MICR encoded with a valid eight or nine-digit routing and transit number can be deposited using the service.
- Scan and capture images and MICR data of U.S. and Canadian dollar items, drawn on Canadian domiciled accounts; these include personal, business, cashier cheques/certified cheques, and money orders. Items that are drawn on Canadian domiciled accounts and MICR encoded with a valid eight digit routing and transit number (5-3 format) can be deposited using the service. **Note:** Canadian drawn cheques with a MICR line containing a ‘45’ are considered to be USD funds.
- The following items can be included in the following deposit platforms/account types:

| Customer Type   | Account Type          | Items included in Deposit                                      |
|-----------------|-----------------------|----------------------------------------------------------------|
| U.S. Domiciled  | U.S. Domiciled account| U.S. (USD) dollar items drawn on U.S. banks                    |
|                 |                       | U.S. (USD) dollar items drawn on Canadian banks                |
---
# CashPro Remote Deposit Administrator Guide

| U.S. Domiciled | Canadian Domiciled Account (CAD Currency) | Canadian (CAD) dollar items drawn on Canadian banks |
|----------------|------------------------------------------|----------------------------------------------------|
| Canadian Domiciled | Canadian Domiciled Account (CAD Currency) | Canadian (CAD) dollar items drawn on Canadian banks |
| Canadian Domiciled | Canadian Domiciled Account (USD Currency) | U.S. (USD) dollar items drawn on Canadian banks<br>U.S. (USD) dollar items drawn on U.S. banks |

- Present items through the Image clearing networks.
- Configure settings based on business needs (for example; deposit limits, endorsements, column headings, custom fields, hot files, auto population and dual deposit approval.
- Deposit up to 500 items in a single check only deposit (including a virtual or paper deposit ticket), with no limit on the number of deposits that can be submitted during a business day¹.
- Transmit images and data to the bank via a secure Internet connection.
- Identify duplicate items within Remote Deposit with electronic duplicate detection.
- View the status of deposit transmissions to the bank and receive confirmation that the bank has received deposits.
- Receive credit to your Bank of America bank account and clear items electronically.
- Eliminate trips to the bank and the need for the original paper to be presented.  
  Note: After depositing items using Remote Deposit, the deposited items must be safeguarded and destroyed in accordance with the user manual.
- Export information containing item data and images. This can be used in accounting processes and some accounts receivable systems. Checks may include several different MICR line formats. Accordingly, the presentation of certain data elements included within the MICR line may vary.
- Modify item information and add check details prior to submitting deposits to the bank through 35 custom data fields.

¹ The declared amount (and the total amount of the deposit) cannot exceed the applicable business segment limit.
---
# CashPro Remote Deposit Administrator Guide

Bank of America offers Remote Deposit services in accordance with 1) the Check Clearing for the 21st Century Act (Check 21), which was signed into law by the Federal Reserve Board effective October 28, 2004 and 2) Canada’s The Bills of Exchange Act and applicable CPA Rules. This law and act permits banks to truncate original checks, process check information electronically, and deliver substitute checks to banks that want to continue receiving paper checks.

Remote Deposit is available for scanning items and transmitting deposits 24 hours a day, excluding normally scheduled weekly system maintenance and when we are enhancing the application. Advanced notices of these scheduled outages are placed in the Important System Messages section of CashPro® Online. By capturing and electronically submitting item images and MICR data to your account for deposit, daily runs to the banking centers may be eliminated.

If located in the U.S. or in Canada, deposit cut off times for same day credit are local to the person making the deposit. Outside of North America, the cut off time will be determined by the account opening location of the WBS (Wholesale Banking System) account number.

> **Note.** Deposits submitted after the current day cut-off times or during non-banking days[^2] will be processed the next banking day.

## Storage and Destruction

It is recommended that clients safeguard original items for 14 days using reasonable commercial standards for storage and in accordance with user documentation or local country restrictions, (if applicable). Reasonable standards include, but are not limited to storing the items in a secure location with limited access. Items should be destroyed using a cross cut shredder after 14 days or when all reasonable attempts to collect on the item have been made. The recommended timeframe for storage is subject to change without notice and failure to comply with safeguard and destruction measures that result in loss will be fully born by the client.

You agree to cooperate with us fully to facilitate our adherence to guidance provided by the Federal Financial Institutions Examination Council, including guidance concerning risk management of remote deposit capture. For this purpose, you agree that we may mandate specific internal controls at your locations audit your operations and/or request additional information. If a scanner is sent to your office in the U.S and/or Canada., it may not be shipped outside of the U.S. and/or Canada without express written approval by Bank of America.

[^2]: Non-banking days include U.S. and Canadian bank holidays and Saturday and Sunday. Bank of America observes U.S. bank holidays as set forth by the Federal Reserve Bank, and observes Canadian bank holidays as set forth by the Bank of America. To see the schedule, refer to http://www.federalreserve.gov/aboutthefed/k8.htm and https://www.bankofcanada.ca/about/contact-information/bank-of-canada-holiday-schedule/. Please note: Specific holiday processing timelines will also be made available through CashPro bulletins.
---
# Exception Items

Scanning of remotely created checks require prior approval by the bank for accounts held in the U.S., and are not permitted for accounts held in Canada. These checks are typically created when the holder of a checking account authorizes a payee to draw a check on that account but does not actually sign the check. In place of the signature of the account-holder, the remotely created check generally bears a statement that the customer authorized the check or bears the customer's printed or typed name. Remotely created checks are vulnerable to fraud because they do not bear a signature or other readily verifiable indication that payment has been authorized.

You must review items for negotiability. Incomplete checks (i.e. missing legal or courtesy amount, no signature, blank payee or no MICR line) may not be deposited.

Third Party checks require that you sign a Third Party Check Cashing Agreement and obtain prior approval by Bank of America for accounts held in the U.S. Third Party checks are not permitted for accounts held in Canada.

Faxed checks are strictly prohibited. Checks received via fax, email or a copy of a check (which is different than an Image Replacement Document (IRD) and a Clearing Replacement Document (CRD), a legal check substitute) cannot be scanned through Remote Deposit for the following reasons:

- Regulations require that an original item be scanned and truncated.
- There is a risk the original item will be deposited as paper.
- The client will not have the original and cannot abide by the storage and destruction guidelines set forth in this guide.
- Foreign items should be on a separate deposit ticket from image ineligibles.

Deposits of foreign items and ineligibles should be sent to the following address for processing:

Bank of America  
Atlanta Bank by Mail  
Southside Center  
Mail Code - GA4-004-01-52  
6000 Feldwood Rd.  
College Park, GA, 30349-3652  

# Remote Deposit Same Day Ledger Credit Cut-off Times

| U.S. Regions                  | Cut-off Times  |
|-------------------------------|---------------|
| U.S. Eastern Time Zone        | 10:00 PM EST  |
| U.S. Central Time Zone        | 10:00 PM CT   |
| U.S. Mountain Time Zone       | 9:00 PM MT    |
| U.S. Pacific Time Zone        | 9:00 PM PT    |

| Canada Regions                | Cut-off Times  |
|-------------------------------|---------------|
| Canadian Atlantic             | 4:30 PM AT    |
| Canadian Central              | 2:30 PM CT    |
| Canadian Central (Saskatchewan)| 1:30 PM CT   |
---
# CashPro Remote Deposit Administrator Guide

| Location                                                                 | Time         |
|--------------------------------------------------------------------------|--------------|
| Canadian Eastern                                                         | 3:30 PM ET   |
| Canadian Mountain                                                        | 1:30 PM MT   |
| Canadian Newfoundland                                                    | 5:00 PM NT   |
| Canadian Pacific                                                         | 12:30 PM PT  |
| Outside of North America. (International) based on first 4 digits of WBS account number | 12:30 PM PT  |
| # 1901 (Miami)                                                           | 10:00 PM ET  |
| # 6550 (New York)                                                        | 10:00 PM EST |
| # 6290 (California)                                                      | 9:00 PM PT   |
---
# Before You Begin

## Prerequisites

- Review the Administrator Guide.
- Enroll in Web-based training.
- Confirm your workstation meets the minimum application requirements (provided at setup).
- Confirm that the Remote Deposit application has been entitled to you and review the welcome screen.

## Enroll in Web-Based Training

Login to CashPro® Online and navigate to CashPro Assistant Support and Education. Go to the Training Center section and click on Training Webinars. Select Remote Deposit and click the Enroll Now button for the training module you desire.

## Confirm Workstation Requirements

Remote Deposit requires a scanner driver to be loaded onto a user's workstation. If the workstation does not meet the minimum system requirements, it may impact the overall performance of the service. Remote Deposit is an internet-based client-server application. A small client-side service runs on a workstation located within a Local or Wide Area Network (LAN/WAN).

It is imperative that you confirm the provided technical requirements are met for the performance and quality of your network connection through the LAN/WAN, and through the internet, and to the Bank of America Merrill Lynch server is sufficient to enable the Remote Deposit application to perform optimally. Careful consideration of network capacity, speed and quality of service is required prior to installing Remote Deposit in the client environment. Insufficient network upload and download speeds and/or poor quality of service can lead to the following symptoms:

- Degradation in scanner performance and frequent jams.
- Slow application response time.
- Application freezes and timeouts.

**IMPORTANT:**

- Local system admin rights are required prior to installing scanner driver onto workstation. If you are unsure if you have local rights, contact your IT department.
- Scanner models may have different system requirements. Be sure to reference the information for the scanner that you are using.
- We do not recommend using multiple remote capture products or scanners on the same PC or moving a scanner from PC to PC.
---
# CashPro Remote Deposit Administrator Guide

- Linux and Thin Client workstation environments are not currently supported.
- Obtain a scanner from Bank of America or use a supported scanner. A list of available scanners may be found in the Technical Requirements document.
- Users must be able to run a local service with a USB 2.0 port from the workstation used for scanning. To determine if the PC has a 2.0 port, please check your device manager to ensure the USB host controller shows as “Enhanced.”

## Confirm Remote Deposit Entitlement

From the CashPro® Online home page, click the **Receipts** tab in the header and choose Remote Deposit.

The Welcome Page provides a landing point for Remote Deposit and also acts as a home page after authentication. From the Welcome Page, users can create deposits, perform research, run reports, and address aged deposits. Confirm that the Remote Deposit application has been entitled to you by confirming with your company administrator or by accessing Remote Deposit from the Receipts tab of your Cash Pro Online. You will require "Full Access" to Remote Deposit prior to being able to perform administrative functions.

**Note:** If the Remote Deposit Welcome page does not display, the user has not been properly entitled to the application. Contact your CashPro Company Customer Administrator for Remote Deposit privileges.

## Review the Welcome Page

The Remote Deposit Welcome Page displays the assigned user role in the upper right hand side of the application window.

The tabs within the Remote Deposit application represent functions granted to certain user roles. Administrators should see and have access to the following tabs:

- Home
- Deposits
- Reports
- Research
- Administration
- Aged Open Deposits (present if you have a non transmitted deposit greater than 3 days old)

Quick Links are displayed on the right side of the Welcome Page. These links will vary based on the individual's user role.

Messages appear at the bottom portion of the Welcome Page. These are posted by Bank of America. For example, the bank may notify the users of quick tips or processing reminders.
---
# User Roles and Functions

For the Remote Deposit application, each resource from your company who will use Remote Deposit is assigned a user role. The application and function of each user role has been established by Bank of America Merrill Lynch to best meet the needs of our clients. A list of role functions is included in the appendix of this guide. It is important to understand what tasks and functions your employees can perform when assigning these roles.

When the user successfully logs in to Remote Deposit, the Welcome Screen displays the assigned user role in the upper right hand side of the application window.

Administrators have access to all tabs. This guide will focus on the Administration tab.

Details on the other tabs may be found in the CashPro® Remote Deposit User Guide.

!Remote Deposit
---
# Performing Administrative Functions

The Administrator Tab default landing page is the customer details section. This page displays the details of your service set up including; your company user id, time zones and report options.

!Customer Details Screenshot

The Customer Administrator can perform additional functions by clicking the tabs on the left hand side of the screen.

- **Details**: Default page with details around accounts that have been set up on Remote Deposit, time zones, and report access
- **Account Groups**: Add, delete and modify account groups
- **Users**: Add, delete and modify users
- **Rule Accounts**: Add delete and modify rules and associated accounts
- **Custom Fields**: Add, delete and modify custom fields
- **Preferences**: Format lists for viewing information on screen, set optional fields, format reports for viewing, saving and exporting, create and edit virtual endorsements
---
# Account Groups

Remote Deposit allows users the flexibility to designate deposits by account groups.

- The account groups are defined by the company and are created by the Customer Administrator or Financial Officer.
- Account groups are used to organize accounts or can be used to represent locations, divisions, or other segmentation needed. For example, an account group can be defined for each location or a group of locations by region.
- Account groups can be set up with a static number, or as null, which allows the user to enter a unique number each time.
- Account groups can contain one or multiple accounts.

The use of account groups replaces the need for traditional serial, sequential, or location number driven deposit tickets, and the account group assigned passes downstream to reporting applications. Each account on Remote Deposit must be assigned to an account group in order to make deposits.

### To create an account group:

1. From the Administration tab, click **Account Groups**.
2. Click **Create New Account Group**.

   !Account Group Page

   The Account Group page displays with the available accounts that may be assigned:

3. Enter a name for the new account group. The account group name is required and has a limit of 250 characters. This account group name will populate on various user reports.
---
# CashPro Remote Deposit Administrator Guide

4. Enter an account group number or leave blank. If you would like to have the same number assigned for every deposit made at a location, enter an account group number. If you want the option of entering a unique number for each deposit that will pass downstream, leave the Account group number Field blank. For this option, you will also need to assign an optional field (one time set up). See the Optional Field section of the user guide for more information. The account group number is limited to 10 numeric characters. The account group number is passed downstream to other information reporting applications and your statement. This field replaces the need for a location number on a deposit ticket.

   **Note.** If using Depository +, the account group number must equal the location assigned to the shadow account. This is available to U.S. clients only.

   !Screenshot

5. From the available accounts list, highlight the accounts that you want to map to the new account group. To select more than one account, click on the account and hold the shift key and press the up or down arrow on your keyboard. Accounts can be assigned to multiple account groups.

6. Click the > button to add the accounts to the Account group.

   !Screenshot
---
# CashPro Remote Deposit Administrator Guide

7. Click the up or down buttons to change account order in account groups.

   !Image showing account order change

8. Click **Save**.

   !Image showing save button

   A message displays, confirming the new account group has been created.

   !Image showing confirmation message
---
# Modifying an Account Group

► To modify an account group:

1. Click on the **Account Groups** link from the Administration tab.

2. Search for the account group you want to modify, or click **Show All**.

   !Account Group Search

3. Click the Edit icon !Edit Icon next to the account group you want to modify.

4. Modify the information and select **Save** or **Cancel**.

   !Modify Information

   A message displays, confirming the changes have been saved.

   !Confirmation Message
---
# Deleting an Account Group

► **To delete an account group:**

1. Click the **Account Groups** link from the Administration tab.

   !Account Groups Link

2. Search for the account group you want to delete, or click **Show All**.

   !Search Account Group

3. Click the **Delete** button. A message appears asking if you want to delete.

   !Delete Confirmation

4. Click **OK**.

5. A confirmation appears and the account group list is refreshed.
---
# Users

This section will show you how to add, modify, and delete a User profile. Changes are done in real time.

**Note.** If a user is deleted in error, they cannot be added back until the next day.

## Adding a New User

► **To add a new user:**

1. From the Administration tab, click **Users**.
2. Click **Create New User**.

!User Interface
---
# Enter the information for the new user:

!User Information Form

**Note:** Fields marked with an asterisk (*) are required information.

- **User ID:** (this is the Cash Pro Online ID)
- **First Name:** First name of the user
- **Last Name:** Last name of the user
- **Short name (optional):** Identifier, such as the initials of the user, will be printed on the virtual endorsement
- **Email address (optional):** Enter email address of the user
- **Client Requests no email communication:** Option to receive email notifications
- **Phone number (optional):** Phone number of user
- **Time Zone:** Time zone of the user making the deposits; this determines the deposit deadline
- **State/Province:** State/Province of depositor
- **Other information**

4. Click **Next** to move to step 2 of 3.

5. Choose the roles you would like the User to have.

6. Click **>** button to assign the selected role.
---
# CashPro Remote Deposit Administrator Guide

7. If prompted, enter the deposit thresholds (not required for all roles). These thresholds can limit the dollar value or number of items a user can deposit. This is useful when training new employees and can be changed in real time.

   !Image of deposit thresholds screen

8. Click **Continue** to proceed to step 3 of 3.

9. Assign the required account groups by highlighting the account group you want assigned to the user.

   !Image of account group assignment screen

10. Click **>** button to assign the selected Account groups.
---
# CashPro Remote Deposit Administrator Guide

11. Click **Save**.

!Image showing the Save button

12. A confirmation appears and the User Search page is refreshed.

!Image showing the refreshed User Search page
---
# Modifying an Existing User

► **To modify an existing user:**

1. From the Administration tab, click the **Users** link.

   !User Search

2. Search for an existing user using the search box, or click **Show All**.

3. Edit the user information by clicking on the **Edit** icon.

   !Edit User

4. Edit the Users Details. You can edit roles, edit account groups, change report access (default is access to all report types), and exclude accounts.

   !User Details
---
# CashPro Remote Deposit Administrator Guide

- To edit user roles, click the **Edit Roles** tab, make the required changes, and click **Save**.

- To edit Account groups, click the **Edit Account Groups** button, make the required changes, and click **Save**.

- To edit report access, click the **Edit Report Access** button, make the required changes, and click on **Save**.

- To edit account exclusions, click the **Edit Account Exclusions** button, make the required changes, and click **Save**.

5. A confirmation appears and the User Details page is refreshed.

!User Details Page
---
# Deleting an Existing User

► **To delete an existing user:**

1. From the Administration tab, click the **Users** link.

2. Search for an existing user using the search box, or click **Show All**.

   !User Search Interface

3. Delete the user information by clicking the **Delete** !Delete Icon icon.

   !Delete User Interface

4. A pop-up will ask if you want to delete the user.

   !Confirmation Pop-up
---
# CashPro Remote Deposit Administrator Guide

5. A confirmation appears in green.

!User Search Confirmation
---
# Rules

A Customer Administrator and Operators are able to create rules within Remote Deposit. Rules are created based on the MICR (if check rule is used) or OCR (if remittance rule is used) of the item scanned. There are two rule types available.

1. **Hot List**: This rule flags items for operator review that your company has determined as non acceptable. For example, a check from an individual that is required to pay by money order or a check from a client that has contributed the maximum amount to a retirement fund.

2. **Auto Populate**: This rule is used to populate predefined custom fields when an item is scanned. For example, an apartment number, policy number, or contact information. The data is carried to the custom field columns that can be exported into other applications. You must have a rule for each unique account/routing transit combination.
---
# Creating a Rule

► **To create a rule:**

1. From the Administration tab, click **Rule Accounts > Create New Rule**.

   !New Rule Screen

   The New Rule screen appears.

2. Name the rule and choose the rule type.

   !Rule Type Screen

3. For Hot List, click **Save**. For Auto populating field, perform steps 4, 5, and 6.

4. Choose the custom field to auto populate.

5. Choose a value to populate in the custom field.

6. Click **Save**.

7. A confirmation appears and the Rule/Account Search page is refreshed.

   !Confirmation Screen
---
# Creating a New Rule Account

► **To create a new rule account:**

1. From the Administration tab, click **Rule Accounts > Create New Rule Account**.

   !Create New Rule Account

2. Choose the item type.

   !Choose Item Type

3. If **Check** is selected:
   a. Enter the account number found in the MICR line of the check.
   b. Enter the Routing Transit number of the check.
   c. Enter the description.

4. If **Remittance** is selected:
   a. Choose the coupon type.
   b. Choose the zone name.
   c. Choose the field name.
   d. Enter the field value.
   e. Enter the description.

5. Add the rules you want assigned.
---
# Editing a Rule Account

► **To edit a rule account:**

1. From the Administration tab, click **Rule Accounts**.

2. Search for a rule using the drop-down, or click **Show All**.

   !Rule Account Search

3. Edit the rule account by clicking on the Edit the Rule Account icon !Edit Icon.

   !Edit Rule Account

4. Modify the existing information and click **Save**.

   !Save Rule Account
---
# Deleting a Rule Account

► **To delete a rule account:**

1. From the Administration tab, click **Rule Accounts**.

   !Rule Account Search

2. Search for a rule using the drop-down, or click **Show All**.

3. Delete the rule account by clicking on the Delete this Rule !Delete Icon icon.

   !Delete Rule Account

4. A pop-up will ask if you want to delete the Rule Account.

   !Confirmation Pop-up
---
# Custom Fields

Custom Fields are defined by your company. They appear on the Edit Item page for data input and can also be exported. These fields are used to either manually add information to items (for example, an invoice number), or can be auto populated with static information (apartment or policy number).

Thirty five (35) custom fields can be assigned to each item scanned. First you must create the custom field, and then you can assign it to depository accounts.

When custom field data flows to reports, the field columns will be listed in the order in which the custom fields were created. You may reorder the fields within the reports section of the preferences tab.

There are 4 types of custom fields:

| Data Type | Format                                      | Example      | Description                                                                 |
|-----------|---------------------------------------------|--------------|-----------------------------------------------------------------------------|
| Numeric   | #############################0              | 1234567      | Any combination of numbers, up to 100 characters in length.                 |
| Currency  | $#,#\#\#,#\#\#\#.00                         | $99,999,999.99 | Dollar amount up to the maximum of $99,999,999.99 includes dollar sign and commas. |
|           | ########.00                                 | 9999999.99   | Dollar amount up to the maximum of $99,999,999.99 does not include dollar sign and commas. |
| Text      | 123abc!@#                                   | Apt 12       | Free form text up to 100 characters in length.                              |
| Date      | mm/dd/yy<br>mm/dd/yy hh:mm:ss<br>mm/dd/yyyy<br>mm/dd/yyyy hh:mm:ss | 01/12/11     | Formatted text.                                                             |
---
# Creating a Custom Field

► **To create a custom field:**

1. From the Administration tab, click **Custom Fields**.

2. Click **Create New Custom Field**.

   !Custom Field/Account Search

3. Enter the Custom Field name. This name will be used to search for the custom field on the Custom Field/Account Search page.

   !New Custom Field

4. Choose the data type.

5. Choose the appropriate Input Validation Pattern for the custom field; this applies to currency and date fields only.

6. To make the custom field visible to a user, place a check-mark in the Show Custom Field box.
---
# Creating an Auto-Complete Custom Field

7. Enter the name you want displayed for each custom field in the Add Locale Label frame. It is suggested that this be the same as the Name (1st field of input) and be as descriptive as possible. This is the custom field name that will display to users during deposit and remittance transactions. It will also display on certain reports.

8. Click **Add a locale label**.

9. Choose whether you want the custom field to be editable or required.
   - **Editable** – the user decides at the point in capture whether to input custom data
   - **Required** – (the user must input data in order to process the item before transmitting the deposit).

10. Click **Save**.

## Creating an Auto-Complete Custom Field

► **To create an auto-complete custom field:**

1. From the New Custom Field page, select the **Autocomplete** entry from the Data type drop-down menu. The page refreshes to show the auto-complete custom field configuration options.

2. Enter an appropriate name for the custom field in the **Name** field.

3. If you do not want the selected customer to be able to edit this custom field definition, select the **Defined by bank** check box.

4. Import the source file containing the auto-complete data you wish to set for the custom field:

   **Note:** The source file must be CSV-formatted and must conform to the following specifications:
---
# CashPro Remote Deposit Administrator Guide

- The first row must include a short description of the file data.
- Subsequent rows contain each data element, with one element identified per line. For example:
  - Inv 12345
  - Inv 67890
  - Blank lines will be ignored.
  - **Example** - Import File:

  |   A   |   B   |   C   |
  |-------|-------|-------|
  | Invoice Number |       |       |
  | 00123 |       |       |
  | 00234 |       |       |
  | 00345 |       |       |
  | 00456 |       |       |
  | 00567 |       |       |
  | 00678 |       |       |
  | 00789 |       |       |

### To import the file:

5. Click the **Browse** button beside the Data source file field.

6. Navigate to the source file you wish to import for the field, and then click the **Open** button to select the file. The name of the selected file displays in the Data source file field.

7. Click the **Import Source File** button to import the data from the selected file.

8. Configure the remainder of the custom field settings, noting the following information:

   - To set the number of characters a user must type before any matching auto-complete values are displayed to the user in a pop-up selection box, change the **Minimum characters required before autocomplete search** value.

   - To allow users to enter any value for the custom field (that is, to not require them to select one of the values imported in the data source file selected for the custom field and presented to the user in the pop-up selection box), select the **Allow unrestricted entry for autocomplete values** check box.

   - To display the field to users on the Edit Item pop-up, select the **Show custom field** check box.

   - To require users to supply data for the custom field, select the **Make custom field mandatory** check box.

   - To pre-fill the custom field with the last user-selected value for items with the same account and routing transit values, select the **Remember the last saved value for items with the same account and routing transit values** check box.
---
# Assigning a Custom Field to a Depository Account

► **To assign a custom field to a depository account:**

1. From the Custom Field/Account Search screen, choose **Account Number** from the drop-down, enter the account number, and click **Search**. To display a list of all accounts, click **Show All**.

2. Choose the account by clicking the **Edit** icon !Edit Icon next to the account number.

   !Account Search Screen

3. To view the account setup by either Item Type or Custom Field, select either **Item Type** or **Custom Field** from the drop-down menu. Both options perform the same functions; however, the screens will vary slightly. The following screen shows the Custom Field selection from the drop down:

   !Custom Field Selection Screen
---
# CashPro Remote Deposit Administrator Guide

4. Select the custom field that you want to assign.

   !Custom Field Selection

5. Choose the available item types. You may highlight multiple types by using the shift/arrows keys.

   !Available Item Types

6. Click the `>` button to move the item types to the Selected Item Types box.

7. Use the up or down buttons to arrange the order of the custom fields.

8. If the custom fields are currency, you have the option to use the sum feature which will require that the sum of the currency custom fields is equal to the amount of the scanned item.
---
# CashPro Remote Deposit Administrator Guide

9. Click **Save**. Confirmation of the change appears in Custom Field/Account Search screen.

!Confirmation Screen
---
# Editing Custom Fields

► To edit custom fields:

1. From the Administration tab, click **Custom Fields**.

   !Custom Fields Screen

2. Within the Custom Field/Account Search screen, select a custom field from the drop-down. If you know the custom field you want to edit, enter all or part of the field name, and click **Search**. If you want a list of all fields, click **Show All**.

   !Custom Field/Account Search Screen

3. Click the Edit icon !Edit Icon next to the custom field you want to change.

4. Edit the information on the Edit Custom Field screen.

   !Edit Custom Field Screen

5. Click **Save**.
---
# Deleting Custom Fields

► **To delete custom fields:**

1. From the Administration tab, click **Custom Fields**.

2. Within the Custom Field/Account Search screen, choose custom field from the drop down. If you know custom field you want to delete, enter all or part of the field name and click **Search**. If you want a list of all fields, click **Show All**.

   !Custom Field/Account Search screen

3. Click the **Delete** button.

   !Delete button

4. Click **OK** to confirm.

   !Confirmation dialog
---
# Customer Preferences

The customer administrator manages their company preferences. Preferences include:

**Lists:** This preference allows the customer administrator to format how information appears on various screens within the application.

**Optional Fields:** Optional Fields add additional information to deposits. These Optional Fields can hold any required information; for example a batch number for the deposit. When Optional Fields are set up as required fields, those fields display on the New Deposit page.

Optional Field 1 may be used 2 different ways; as tracking of a unique deposit number (overrides the absence of an account group number) or to enter relevant data.

Tracking of a unique deposit number: If your set up requires a unique or system generated number each time a deposit is made, you may choose to leverage the account group=null and enter the unique number in an optional field. If you choose an account group of null, the user will see a subsequent field to manually enter up to a 10 digit number. This field passes in the serial number field of information reporting and statements. It is used to reconcile deposits by location, division etc.

Optional Fields 1, 2, 3 as data capture: If data is entered into the optional field and the account group selected has a pre assigned number, the data is used only as an optional field and is visible only with deposit details within Remote Deposit. The information a user submits in Optional Fields is saved within the Deposit Details screen. This information resides within the application and will not be provided on any external reporting.

**Reports:** This section enables you to customize the layout and data within standard reports.

**Virtual Endorsements:** The endorsement function allows you to customize endorsements by your company. The Virtual Endorsement is not printed on the physical item, but present when the item is printed or viewed after scanner capture. Some data elements within an endorsement are required and some cannot be modified (e.g. Bank of First Deposit). The required data elements appear in the list without the Edit icon.
---
# Editing Lists

► To edit a list:

1. From the Administration tab, click **Preferences**.

   !Step 1

2. Click the Edit this Preference icon !Edit Icon next to Lists.

   !Step 2

3. Choose the screen you want to configure.

   !Step 3

4. Highlight the fields that you want to display and click the > button. You may also remove fields from display by clicking the < button.

   !Step 4

5. Reorder the fields by using the up or down buttons.

   !Step 5
---
# Editing Optional Fields

► **To edit optional fields:**

1. From the Administration tab, click **Preferences**.

   !Preferences Screen

2. Click the Edit this Preference icon !Edit Icon next to Optional Fields.

3. Edit the optional field requirements.

   !Optional Fields Screen

4. Select **Displayed** to have the field displayed on the New Deposit Screen.

5. Select **Required** to require the operator to enter data.

6. Name the optional fields.

7. Click **Save**.

# Editing Report Preferences

► **To edit report preferences:**

1. From the Administration tab, click **Preferences**.
---
# CashPro Remote Deposit Administrator Guide

2. Click the Edit this Preference icon !Edit Icon next to Reports.

3. Choose the report type that you want to customize.

   !Edit Report Preferences

4. Choose the fields you would like displayed on the reports from the Available choices. The choices will vary based on the report type.

5. Click `>` to move the selected items to the Assigned column.

6. Reorder the columns by using the up or down buttons.

7. Choose the sort column order.

   !Edit Report Preferences

8. Click **Apply** to save changes and remain on the Edit Report Preferences screen, or click **Apply** to save changes and return to the Preferences tab.
---
# Virtual Endorsements

► To set virtual endorsements:

1. From the Administration tab, click **Preferences**.

   !Preferences Screenshot

2. Click on the Edit this Preference icon !Edit Icon next to Virtual Endorsements.

3. Select the portion of your endorsement that needs to change. Only the items with an Edit icon !Edit Icon are available for editing. Under the Tasks column, click the Edit icon !Edit Icon, next to the item within the Virtual Endorsement that should be changed. The placement or order of the endorsement string cannot be changed.

## Endorsement String on Virtual Endorsement:

- **Account group**: The account group name, can also reflect the location number if used in place of the account group.

- **Account Legal Name**:

- **Customer Name**: Customer account name. It is important to note, CUST is the pre field endorsement, and the customer name is the post field endorsement. Enter the legal name of your company. The endorsement will default to the Customer name. To change the default, click on the task icon, and choose an alternate default, i.e. account name.

- **Date**: Deposit creation date.

- **Dep**: Deposit Number; the sequential number of the deposit, cumulative number.

- **Deposited by**: Short name of the individual making the deposit.

- **For Deposit only to**: This text may be replaced or amended, however language cannot be a qualified endorsement (all acceptable payees etc. without bank approval).

- **R/T**: Routing transit number of the depository account; used in processing the deposit, adjustments and returns.

- **SEQ**: Sequence number of the deposit, assigned by the application.
---
NO_CONTENT_HERE
---
# Exiting the Remote Deposit Application

1. Click the **Close** link to exit out of Remote Deposit and return to CashPro® Online. Click the **Logoff** link in the upper right corner of the application to log out of CashPro® Online.

!CashPro Remote Deposit
---
# CashPro Mobile Deposit

When away from a scanner workstation Remote Deposit users can access the CashPro Mobile app on an Apple® iOS or Android® device to deposit checks. Mobile Deposit is available to U.S. clients only.

## Prerequisites

- Users must be entitled to Remote Deposit.
- Users must be entitled to Mobile.
- Users must download CashPro Mobile to their mobile device.
- Users must be assigned a role with Mobile permissions in the CashPro Remote Deposit application.

## User Entitlement to CashPro Remote Deposit

► **To entitle a user to Remote Deposit:**

1. Contact your CashPro Primary Administrator for user level Remote Deposit entitlement.

## User Entitlement to CashPro Mobile

► **To entitle a user to Mobile Access:**

1. Contact your CashPro Primary Administrator for user level Mobile entitlement.

## Downloading CashPro Mobile

► **To download CashPro Mobile to a mobile device:**

- Apple® iOS device users download CashPro Mobile from the App Store® to your phone or tablet.
- Android® device users download CashPro Mobile from the Google Play® Store to your phone.

## Assigning User Roles for Mobile Access

Each resource from your company who will use Remote Deposit and Mobile Deposit is assigned a user role in CashPro Remote Deposit. A complete list of role functions is included in the appendix of this guide. It is important to understand what tasks and functions your employees can perform when assigning these roles. Details on making deposits using the CashPro Mobile application can be found in the CashPro Remote Deposit User Guide.

**Note.** We recommend each Mobile Deposit user’s deposit limit be set for the amount needed for typical single check deposit.
---
# Support for Remote Deposit

## User Guides

To access the user guide electronically, click the **User Resources** link in the top right corner of the Home page.

!CashPro Remote Deposit

## Help Tips

When **Help Tips** is turned on, the user can view the tips when he/she selects **Show Tips**. Tool tips appear when you roll your curser over a button or field.

Help tips are not available for viewing when the user selects **Help Tips**.

## Technical Support

Contact the Technical Services Helpdesk with questions about the following:

1. Questions about Remote Deposit.
2. Questions about Scanners.
3. CashPro® Online User IDs
4. CashPro® Online Passwords

The Technical Services Helpdesk is available to take your calls 7:00 AM to 9:00 PM Eastern Time Monday through Friday.

5. 1.888.589.3473 toll-free (Domestic) or
6. 1.704.387.3020 outside of the United States between 7:00 AM and 5:00 PM Eastern Time on banking business days.
7. Email at technicalservices@bankofamerica.com

If located in Latin America, Europe, the Middle East, Asia, or Africa, please contact your Global Treasury Management Product Specialist.
---
# Troubleshooting, Login, and Authentication Errors

| Error                                       | Possible Cause                                                                 | Potential Resolution                                                                                                                                                                                                 |
|---------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You are unable to login to Remote Deposit   | User names and passwords are case sensitive, and passwords must comply with Bank of America's digital certificate guidelines. | Ensure you enter the correct user name and password as was provided with your authentication instructions. Contact Technical Services Helpdesk for details about your specific password requirements or continue to be denied access to the application. |
| You entered an invalid user name or password | User names and passwords are case sensitive, and passwords must comply with Bank of America's guidelines. | Ensure you enter both your correct user name and password as provided to you by Bank of America Contact Technical Services Helpdesk for details about your specific password requirements. |
| You entered invalid password information    | Re-enter the password information.                                              | Contact Bank of America Technical Services Helpdesk if you are still having problems.                                                                                                                                 |
| The application cannot be accessed          | Ensure the correct URL is used                                                 | If the problem persists, contact the Bank of America Technical Services Helpdesk.                                                                                                                                     |
---
# Remote Deposit Frequently Asked Questions

| Question                                                                 | Answer                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| What are the system requirements for CashPro® Remote Deposit?            | Refer to the technical requirements document for the most up-to-date requirements.                                                                                                                                                                                                                                                                       |
| Where can I take additional training?                                    | Training for CashPro® Remote Deposit is available. Go to CashPro University. Click Training Webinars within Training Center on the right. Click Remote Deposit, and then click Enroll Now under the desired topic to sign up for a webinar.                                                                                                              |
| Am I required to endorse the items I deposit?                            | Endorsements are not required. A virtual endorsement is placed on each check by Bank of America Merrill Lynch.                                                                                                                                                                                                                                           |
| Is a deposit slip required?                                              | Deposit slips are not required.                                                                                                                                                                                                                                                                                                                          |
| How long is a company required to keep scanned checks?                   | Bank of America Merrill Lynch recommends clients safeguard original items for 14 days using reasonable commercial standards for storage and in accordance with user documentation or local country restrictions. Reasonable standards include but are not limited to storing the items in a secure location with limited access. An item should be destroyed using a crosscut shredder after 14 days or when all reasonable attempts to collect on the item have been made. |
| What do Account Groups do? Are there limitations for Account Groups?     | Account Groups assign a static location/division number to a deposit without using a paper deposit ticket. When you log in to CashPro® Online Remote Deposit, you choose an Account group to which you wish to make the deposit. This number is passed to all downstream applications, including CashPro® Online, in the serial number field.                   |
| Can I add an account to an Account Group?                                | Accounts in CashPro® Remote Deposit may be added to Account Groups. Contact your Bank of America Merrill Lynch representative to add an account to CashPro® Remote Deposit.                                                                                                                                                                               |
| How do I determine which items to deposit into a Canadian GBS account vs. USD GBS account? | Review the MICR data of the checks. The routing transit is determined Canadian when the MICR contains this format, nnnnn-nnn; the dash symbol in between the values will always exist in Canadian items. There will also be a 45 in the MICR after the account # symbol if the item is in U.S. dollars.                                                     |
| How does U.S. clients determine which U.S. items are drawn on a Canadian bank? | Review the MICR data of the checks. The routing transit is determined Canadian when the MICR contains this format, nnnnn-nnn; the dash symbol in between the values will always exist in Canadian items. There will also be a 45 in the MICR after the account # symbol if the item is in U.S. dollars.                                                     |
| What is an Image Replacement Document (IRD)?                             | An Image Replacement Document (IRD) or substitute check, as set forth in Check 21, which provides that a properly prepared substitute check that meets the requirement for legal equivalence is the legal equivalent of the original for all purposes.                                                                                                    |
| What is a Clearing Replacement Document (CRD)?                           | In the case of items drawn on a financial institutions located in Canada, a Clearing Replacement Document as defined in CPA Standard 014 and Rule A10 of the Canadian Payments Association.                                                                                                                                                               |
---
# CashPro Remote Deposit Administrator Guide

| Question                                                                 | Answer                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Can the CashPro® Remote Deposit scanner be used for more than one bank? | The scanner provided by Bank of America Merrill Lynch can be used only with CashPro® Remote Deposit.                                                                                                                            |
| Can foreign checks be deposited through CashPro® Remote Deposit?        | Only items drawn on Canadian and U.S. banks may be deposited into Canadian and U.S. dollar accounts through CashPro® Remote Deposit. Canadian account guidelines apply.                                                          |
| What should I do with foreign checks?                                   | For U.S. clients, mail non-U.S. items to:<br>Bank of America<br>Atlanta Bank by Mail<br>Southside Center<br>Mail Code - GA4-004-01-52<br>6000 Feldwood Rd.<br>College Park, GA, 30349-3652<br>**Note:** Foreign checks are not accepted for Canadian clients. |
| When is a deposit available?                                            | If a deposit is made by your cutoff time, the deposit will be posted the same day. Availability of the deposit is determined by your availability schedule.                                                                       |
| How will I know if a deposit has been adjusted by Bank of America Merrill Lynch? | Adjustments are shown on CashPro® Remote Deposit reports and are mailed to your corporate office. You are able to rescan the original item if it is adjusted.                                                                     |
| How long are images available within CashPro® Remote Deposit? Is a longer image retention period available? | Images are available for 45 days within CashPro® Remote Deposit. Extended image storage is available on CashPro® Online through Image Access or via Image Transmission/CD-ROM Services.                                           |
| Is there a limit to the number of checks that can be processed in a single CashPro® Remote Deposit (batch)? | Deposits (batches) are limited to 500 items: 499 checks and one deposit ticket/credit record. Remittance deposits are limited to 499 checks and one deposit ticket/credit record and unlimited associated remittances. There is no limit to the number of deposits you can submit each day. |
| Does each user need his or her own login ID?                            | Each individual user of CashPro® Online must have a unique login ID.                                                                                                                                                            |
| Can I rescan the original item if it is returned?                       | The original item cannot be re-deposited.<br>For U.S. clients:<ul><li>If an item is returned, the Image Replacement Document (IRD) may be rescanned through CashPro® Remote Deposit or brought to a banking center for processing. The IRD is MICR encoded with a valid MICR line and is considered a legal document.</li></ul>For Canadian clients:<ul><li>Returned items cannot be re-deposited unless the returned reason is “Item Cleared in the Wrong Currency.”</li></ul> |
| What should I do if my scanner breaks?                                  | Contact Technical Services Helpdesk with problems regarding your scanner.                                                                                                                                                       |
| Who should I contact for CashPro® Remote Deposit technical issues?      | Contact Technical Services Helpdesk for CashPro® Remote Deposit Issues.                                                                                                                                                         |
| Who should I contact if I have technical issues                         | Contact the Technical Help Desk for technical issues accessing                                                                                                                                                                  |
---
# CashPro Remote Deposit Administrator Guide

| Question | Answer |
|----------|--------|
| accessing CashPro® Online? | CashPro® Online. |
| How often should I clean my scanner? | Scanners should be cleaned every 3,000 items scanned or once a week, whichever is sooner. Instructions can be found in the user guide under Cleaning Your Scanner. Additional supplies can be ordered through TASQ at 1.866.410.7216. |
| Can I scan WIC checks and money orders? | WIC checks and money orders may be scanned via CashPro® Remote Deposit. However, they may be too light, too dark, or printed on non-standard check stock. Due to these variations, scanners may have a difficult time reading the required amount field. The amount field can be manually entered. **Note:** WIC checks only apply to U.S. accounts. |
| What are the password parameters and maintenance for CashPro® Online? | CashPro® Online requires password verification every six months. A letter is emailed to the email address on file for each user. The User ID (stored password) will be locked if verification is not complete. |
---
# Appendix

## User Roles and Functions

| Role                  | Permission                                                                 | Welcome Page Tabs                                                                 |
|-----------------------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Customer Administrator* | Access Aged Open Deposits                                                  | Home, Deposits, Reports, Research and Administration                              |
|                       | Approve/Transmit Deposits to Bank in CashPro Remote Deposit                 |                                                                                   |
|                       | Approve/Transmit Deposits to Bank in CashPro Mobile Deposit*                |                                                                                   |
|                       | Assign Deposit to Another User                                             |                                                                                   |
|                       | Balance Deposits                                                           |                                                                                   |
|                       | Create/Modify Deposits in CashPro Remote Deposit                           |                                                                                   |
|                       | Create/Modify Deposits in CashPro Mobile Deposit*                          |                                                                                   |
|                       | Manage Account Groups                                                      |                                                                                   |
|                       | Manage Custom Fields                                                       |                                                                                   |
|                       | Manage Customer Preferences                                                |                                                                                   |
|                       | Manage Customer Rules                                                      |                                                                                   |
|                       | Manage Hotlist Rules                                                       |                                                                                   |
|                       | Manage Users                                                               |                                                                                   |
|                       | Override Hot List Item Rejection                                           |                                                                                   |
|                       | Report On All Users' Deposits                                              |                                                                                   |
|                       | Request Item Research                                                      |                                                                                   |
|                       | Request Reports                                                            |                                                                                   |
|                       | View Deposits in CashPro Remote Deposit                                    |                                                                                   |
|                       | View Deposits in CashPro Mobile Deposit *                                  |                                                                                   |
|                       | View Customer Details                                                      |                                                                                   |
| Operator*             | Access Aged Open Deposits                                                  | Home, Deposits, Reports, Research, Administration, Aged Open Deposits (if applicable) |
|                       | Approve/Transmit Deposits to Bank in CashPro Remote Deposit                 |                                                                                   |
|                       | Approve/Transmit Deposits to Bank in CashPro Mobile Deposit*                |                                                                                   |
|                       | Assign Deposit to Another User                                             |                                                                                   |
|                       | Balance Deposits                                                           |                                                                                   |
|                       | Create/Modify Deposits in CashPro Remote Deposit                           |                                                                                   |
|                       | Create/Modify Deposits in CashPro Mobile Deposit*                          |                                                                                   |
|                       | Manage Auto-populating Field Rules                                         |                                                                                   |
|                       | Manage Hotlist Rules                                                       |                                                                                   |
|                       | Override Hot List Item Rejection                                           |                                                                                   |
|                       | Request Item Research                                                      |                                                                                   |
|                       | Request Reports                                                            |                                                                                   |
|                       | View Deposits in CashPro Remote Deposit                                    |                                                                                   |
|                       | View Deposits in CashPro Mobile Deposit*                                   |                                                                                   |
|                       | View Users                                                                 |                                                                                   |
| Limited Operator*     | Access Aged Open Deposits                                                  | Home, Deposits, Reports, Research, Administration, and Aged Open                  |
|                       | Balance Deposits                                                           |                                                                                   |
|                       | Create/Modify Deposits in CashPro Remote Deposit                           |                                                                                   |
|                       | Create/Modify Deposits in CashPro Mobile Deposit*                          |                                                                                   |
|                       | Manage Auto-populating Field Rules                                         |                                                                                   |
---
# CashPro Remote Deposit Administrator Guide

| Role                          | Permissions                                                                                     | Deposits (if applicable) |
|-------------------------------|-------------------------------------------------------------------------------------------------|--------------------------|
|                               | Manage Hotlist Rules                                                                            |                          |
|                               | Override Hot List Item Rejection                                                                |                          |
|                               | Request Item Research                                                                           |                          |
|                               | Request Reports                                                                                 |                          |
|                               | View Deposits in CashPro Remote Deposit                                                         |                          |
|                               | View Deposits in CashPro Mobile Deposit*                                                        |                          |
|                               | View Users                                                                                      |                          |
| Customer Service Representative | Request Reports                                                                                | Home, Deposits, Reports, Research, Administration, Aged open deposits |
|                               | Request Item Research                                                                           |                          |
|                               | View Accounts                                                                                   |                          |
|                               | View Account Groups                                                                             |                          |
|                               | View Customer Details                                                                           |                          |
|                               | View Deposits                                                                                   |                          |
|                               | View Users                                                                                      |                          |
| Financial Officer             | Approve/Transmit Deposits to Bank in CashPro Remote Deposit                                     | Home, Deposits, Reports, Research, and Administration |
|                               | Manage Account Groups                                                                           |                          |
|                               | Request Reports                                                                                 |                          |
|                               | Requests Item Research                                                                          |                          |
|                               | View Accounts                                                                                   |                          |
|                               | View Customer Details                                                                           |                          |
|                               | View Deposits in CashPro Remote Deposit                                                         |                          |
| Report Viewer                 | Report On All Users' Deposits                                                                   | Home, Reports, Research and Administration |
|                               | Request Item Research                                                                           |                          |
|                               | Request Reports                                                                                 |                          |
|                               | View Users                                                                                      |                          |
| Mobile*                       | Approve/Transmit Deposits to Bank in CashPro Mobile Deposit*                                    | N/A                      |
|                               | Create/Modify Deposits in CashPro Mobile Deposit*                                               |                          |
|                               | View Deposits in CashPro Mobile Deposit*                                                        |                          |
| Limited Mobile*               | Create/Modify Deposits in CashPro Mobile Deposit* (deposits require approval/transmission in CashPro Remote Deposit) | N/A                      |
|                               | View Deposits in CashPro Mobile Deposit*                                                        |                          |

*denotes new Mobile permissions and roles. This is available for U.S. clients only.
---
# Custom Field Formats

| Data Type | Format                                | Example       | Description                                                                 |
|-----------|---------------------------------------|---------------|-----------------------------------------------------------------------------|
| Numeric   | ##############################0        | 1234567       | Any combination of numbers, up to 100 characters in length.                 |
| Currency  | $##,###,###.00                        | $99,999,999.99| Dollar amount up to the maximum of $99,999,999.99 includes dollar sign and commas. |
|           | #######.00                            | 9999999.99    | Dollar amount up to the maximum of $99,999,999.99 does not include dollar sign and commas. |
| Text      | 123abc!@#                             | Apt 12        | Free form text up to 100 characters in length.                              |
| Date      | mm/dd/yy                              | 01/12/11      | Formatted text.                                                             |
|           | mm/dd/yy hh:mm:ss                     |               |                                                                             |
|           | mm/dd/yyyy                            |               |                                                                             |
|           | mm/dd/yyyy hh:mm:ss                   |               |                                                                             |
---
# Deposit Status Types

| Status              | Description                                                                                                                                                                                                 |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Open                | With a second word to show the state of the deposit processing:                                                                                                                                              |
|                     | **Incomplete** – There may be additional items to scan or recognition results may be incomplete.                                                                                                             |
|                     | **Processing** – Document scanning is active.                                                                                                                                                                |
|                     | **Balanced** – All items have been scanned; the declared total and item total match.                                                                                                                         |
|                     | **Jammed** – The scanner has reported a track jam.                                                                                                                                                           |
|                     | **Cancelled** – Typically results in immediate removal of the deposit.                                                                                                                                       |
|                     | Open deposits are purged after 90 days of inactivity.                                                                                                                                                        |
| Transmitting        | The deposit is currently being sent to Bank of America.                                                                                                                                                      |
| Received            | The deposit has been successfully received by Bank of America.                                                                                                                                               |
| Pending Delete      | Stale data being removed by the application.                                                                                                                                                                 |
| Received Pending    | Do NOT rescan the deposit as it has been received by the bank. Contact a Customer Service Representative at Bank of America's Technical Services Helpdesk group to advise them of the status. See Support for contact information. |
| Perfected           | Bank of America completed processing this deposit without making adjustments.                                                                                                                                |
| Perfected Adjusted  | Bank of America completed processing this deposit and made adjustments.                                                                                                                                      |
---
# Icons

Remote Deposit uses icons to communicate messages and information to users.

| Icon  | Action  | Purpose  |
|-------|---------|----------|
| !Delete Icon | Delete  | Deletes the associated item. |
| !Display Icon | Display | Display items, deposits or saved reports. |
| !Edit Icon | Edit    | Edit an item's details. |
| !Filter Icon | Filter  | Create a column filters. |
| !View Icon | View    | View an item's details. |
| !Alert Icon | Alert   | Draws attention to items that require action before proceeding. |
| !Warning Icon | Warning | Draws attention to specified items that required user attention. |
---
# Report Options

| Report Name                              | Description                                                                                                                                                                                                 | Formats       | Deposit Status Included in Report                                       |
|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------|
| Standard Export File                     | Provides an exportable version of simple and remittance deposits.                                                                                                                                           | CSV XLS       | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Deposit Detail By Account Number Report  | Provides a detailed report for all simple deposits.                                                                                                                                                         | PDF RTF DOCX  | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Deposit Details by Deposit Number Report | Provides a detailed report by deposit number for all simple deposits.                                                                                                                                       | PDF RTF DOCX  | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Summary of Deposits by Account Report    | Provides a summary report for all simple deposits.                                                                                                                                                          | PDF RTF DOCX  | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Payment Details Report                   | Provides a detailed report for all remittance deposits.                                                                                                                                                     | PDF RTF DOCX  | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Payment Summary Report                   | Provides a summary report for all remittance deposits.                                                                                                                                                      | PDF RTF DOCX  | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Remittance Details by Deposit Number     | Provides a detail report by deposit number for all remittance deposits.                                                                                                                                     | PDF RTF DOCX  | Received Received Pending Perfected Perfected Adjusted Transmitting Open |
| Client Account Listing Export File       | Provides detailed information about each of a selected customer's configured accounts. For each account, the report details account grouping and identification information, as well as the account and routing transit numbers, and the account status. | CSV XLS       | N/A                                                                       |
---
| Client User Listing Export File (by request) | Provides detailed user information for selected customers. For each customer, the report details the customer's configured users. For each user, the report details the user's ID, name, user name, email address and email opt out information, telephone number, and their current status. | CSV XLS | N/A |
---
# Research Options

| Criteria                     | Description                                      | Value                                                                 |
|------------------------------|--------------------------------------------------|----------------------------------------------------------------------|
| Account group name           | Name of the account groups                       | Drop down of available account groups                                |
| Amount                       | Amount of the item                               | Value Range                                                          |
| Bank sequence number         | Sequence number of the item assigned by the bank | Free form                                                            |
| Check number                 | Check number of the item                         | Free form                                                            |
| Credit amount                | Dollar value of the deposit                      | Value range                                                          |
| Custom field                 | Manual and automated data entry fields           | Free form (must have custom fields set up for option to appear)      |
| Debit item account number    | Debit item                                       | Free form                                                            |
| Deposit account number       | Account number where the deposit was made        | Free form                                                            |
| Deposit credit date/time     | Date/Time a deposit was made                     | DD/month drop down/ 4 digit year, time of day                        |
| Deposit number               | Number of a deposit as assigned by the bank      | Value range                                                          |
| Deposit status               | Status of the deposit                            | Drop down with the following choices: Open, Transmitting, Received, Received pending, Perfected, Perfected adjusted |
| Item grouping                | Groups of like items                             | Drop down with the following choices: Check, Credit Item, Payment Coupon |
| Item routing transit number  | ABA/Routing transit of the debit item            | Free form                                                            |
| Item status                  | Status of the deposited item                     | Not Queued, Recognition Complete, Pending                            |
| Item type                    | Classification of item                           | Drop Down                                                            |
| Posted amount                | Posted amount of the item                        | Range value                                                          |