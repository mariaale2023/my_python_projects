
from ticket import Ticket
print('welcome to service desk')

tickets = []
while True:
    action = input(
        '\n\nSELECT OPTION: 1: create new ticket. 2: reopen ticket. 3: list all tickets. 4: resolve ticket. ')
    if action == '1':
        operator_name = input('enter creator name (operator): ')
        callerID = input('enter caller UserID: ')
        caller_email = input('enter caller email: ')
        description = input('describe the issue: ')
        new_ticket = Ticket(operator_name, callerID, caller_email, description)
        if description.find('password reset') > -1:
            new_ticket.reset_password(operator_name)
        tickets.append(new_ticket)

    elif action == '2':
        ticket_id = int(input('enter the ticket ID: '))-2001
        reopen_reason = input('enter reason for reopening: ')
        tickets[ticket_id].reopen_ticket("Caller", reopen_reason)
        tickets[ticket_id].submit_comment("Caller", reopen_reason)

    elif action == '3':
        for i in tickets:

            print(i)

    elif action == '4':
        ticket_id = int(input('enter the ticket ID: '))-2001
        admin_name = input('enter Service desk operator: ')
        solve_comment = input('enter resolve notes: ')
        tickets[ticket_id].solve_ticket(solve_comment, admin_name)

    else:
        print('no valid input')
