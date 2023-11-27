# Ticket Management System

<div style="text-align:center">
  <img src="python_ticket.jpg" alt="Ticket" width="300"/>
</div>

*Image created by Dall-e*



also available in Replit:
https://replit.com/@mariaale2023/ticketsystem#dashboard.py
![Screenshot](Screenshot.jpg)
Originally part of the Assignment in IT2016D


# Help Desk Ticketing System

## Overview

This is a simple prototype of a Help Desk Ticketing System. The system allows users to submit, view, resolve, and reopen tickets. Each ticket is associated with a unique ticket number and contains information such as the creator's name, staff ID, email, description, status, and response.

## Features

- **Open Ticket:** Users can submit a new ticket by providing details about the issue.
- **View Tickets:** View a list of all submitted tickets.
- **Resolve Ticket:** Resolve an open ticket, providing a comment. Closed tickets cannot be resolved again.
- **Reopen Ticket:** Reopen a closed ticket, providing a comment.
- **Display Statistics:** View statistics, including the number of submitted, resolved, and open tickets.

##How to Display

The program flows based on user actions 1, 2, 3, 4, and 5:

1. Open Ticket (User Action 1):
   When the user selects option 1, they are prompted to enter their name, UserID, email, and describe the issue.
   If the issue is a password reset, a new ticket is created, a new password is generated, and the ticket is marked as resolved and closed.
   If it's a regular issue, a new ticket is created, and the details are displayed.

2. Show All Tickets (User Action 2):
   When the user selects option 2, the program displays a list of all created tickets, showing ticket details such as number, creator, status, etc.

3. Resolve Ticket by Number (User Action 3):
   The user selects option 3 and is prompted to enter the number of the ticket they want to resolve.
   If the ticket is already closed, a message is displayed indicating it can't be resolved again.
   If the ticket is open, the user can provide resolution comments, and the ticket is marked as closed.

4. Reopen Resolved Ticket (User Action 4):
   The user selects option 4 and is prompted to enter the number of the ticket they want to reopen.
   If the ticket is closed, it can be reopened, and the user provides comments.
   If the ticket is already open, a message indicates that the ticket is already open.

5. Display Ticket Statistics (User Action 5):
   Option 5 displays statistics, including the total number of submitted tickets, the number of resolved tickets, and the number of open tickets.

The program runs in a loop, allowing the user to perform multiple actions until they decide to exit. Each action corresponds to a specific set of instructions and interactions with the user, making the program interactive and user-friendly.

## Technology Used

- Python 3

## Installation

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:mariaale2023/ticket_sys.git
   ```
2. **Navigate to the Project Directory:**
   `cd ticket_sys`
   `cd dashboard.py`

3. **Run the Program:**
   `/dashboard.py`

## Project Structure

- dashboard.py: Main program file.
- ticket.py: Ticket class definition.
- README.md: Project documentation.

## Note

## ASCII Art

The script includes ASCII art in the form of a ticket at the beginning, generated from [patorjk.com/software/taag/](https://patorjk.com/software/taag/).

Feel free to use or modify this script for your ticket management needs!
