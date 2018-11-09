import getpass, imaplib

user = input("Enter your GMail username:")
pwd = getpass.getpass("Enter your password: ")

# Connecting to the gmail imap server
server = imaplib.IMAP4_SSL("imap.gmail.com")
server.login(user,pwd)
server.select("INBOX")
##print(m.list()) 
try:
    resp, items = server.search(None, "NOT SEEN") # Searching unread mails
    items = items[0].split() # Getting the mails id
    if (len(items) == 0):
        raise Exception("Inbox is empty!") 
    count = 0
    for email in items:
        server.store(email, '+X-GM-LABELS', '\\Trash')  # Move to trash (Use \\Delete instead to directly delete mails)
        count+=1
    print("Done!")
    print("Deleted ",count, " mails")
except Exception as e:
    print (str(e))    
