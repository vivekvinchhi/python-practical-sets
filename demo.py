books = {}
borrowers = {}
checkouts = []

# Read the input
section = input().strip()
while section != "EndOfInput":
    line = input().strip()
    while line:
        if section == "Books":
            accession_number, title = line.split("~")
            books[accession_number] = title
        elif section == "Borrowers":
            username, full_name = line.split("~")
            borrowers[username] = full_name
        elif section == "Checkouts":
            username, accession_number, due_date = line.split("~")
            checkouts.append((username, accession_number, due_date))
        line = input().strip()
    section = input().strip()

# Sort the checkouts by due date, then by full name
checkouts.sort(key=lambda checkout: (checkout[2], borrowers[checkout[0]]))

# Output the currently issued books
for checkout in checkouts:
    username, accession_number, due_date = checkout
    full_name = borrowers[username]
    title = books[accession_number]
    print(f"{due_date}~{full_name}~{accession_number}~{title}")
