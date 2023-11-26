class Ticket:
    ticket_counter = 2000  # Class variable to auto-generate ticket numbers

    def __init__(self, id_creator: str, caller_name: str, caller_email: str, description: str):
        """
        Initializes a new Ticket instance.

        Args:
        - ticket_creator (str): The name of the person creating the ticket.
        - caller_name (str): The name of the person reporting the issue.
        - caller_email (str): The email address of the person reporting the issue.
        - description (str): A brief description of the issue or request.
        """
        self.ticket_creator = id_creator
        self.caller_name = caller_name
        self.caller_email = caller_email
        self.ticket_number = self.ticket_counter
        self.description = description
        self.status = "Open"
        self.comments = []

        Ticket.ticket_counter += 1

    def reset_password(self, admin_name):
        # Perform password reset logic here
        self.status = "Resolved"
        string = f'Password reset by {admin_name}. New password: {self.caller_name[:2]}{admin_name[:3]}'
        print(string)
        self.comments.append(string)

    # def print(self):
    #     print(f'{self.ticket_number}: {self.status}. Caller: {self.caller_name} - {self.caller_email}. Comments:{", ".join(self.comments)}')

    def solve_ticket(self, resolution_notes, admin_name):
        # Perform ticket resolution logic here
        self.status = "Resolved"
        self.comments.append(
            f"Ticked solved by {admin_name}. Resolution notes: {resolution_notes}\n")

    def feedback(self, rating, comment):
        # Record feedback from the user
        self.comments.append(f"\nFeedback: Rating {rating}/5 - {comment}\n")

    def submit_comment(self, user_name, comment):
        # Allow user to submit additional comments
        self.comments.append(f"\nComment by {user_name}: {comment}\n")

    def reopen_ticket(self, user_name, comment):
        # Reopen a closed ticket
        if self.status == "Resolved":
            self.status = "Open"
            self.comments.append(
                f"Ticket reopened. {user_name} indicates: {comment}")

    def __str__(self):
        return f"Ticket Number: {self.ticket_number}\n" \
               f"Ticket Creator: {self.ticket_creator}\n" \
               f"Caller Name: {self.caller_name}\n" \
               f"Caller Email: {self.caller_email}\n" \
               f"Status: {self.status}\n" \
               f"Description: {self.description}\n" \
               f"Comments: {', '.join(self.comments)}"


# Example usage:
if __name__ == "__main__":
    # Create a new ticket
    ticket1 = Ticket("Alice", "Bob", "bob@example.com",
                     "Can't access my account")

    # Perform actions on the ticket
    ticket1.reset_password("Admin1")
    ticket1.feedback(4, "Service was good.")
    ticket1.solve_ticket("password reset and emailed", "Admin2")
    ticket1.reopen_ticket()
    ticket1.submit_comment("Alice", "I'm still having issues.")

    # Print the ticket information
    print(ticket1)
