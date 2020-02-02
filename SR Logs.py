from datetime import datetime
print("===================================================================")
print("|============| SERVICE REQUEST LOGS - By Ayo Asekun |=============|")
print("===================================================================")

def END():
    print("===================================================================")
    print("|                          END OF LOGS                            |")
    print("===================================================================")
    end = ""

# Below  functions open Word document containing Templates for documenting case details

# New Ticket template
def NSC():
    import os
    path = ""
    # Path to file or website for template to new case ticket
    NSC1 = os.startfile(path)
# Existing ticket template
def ESC():
    import os
    path = ""
    # path to file or website for template to existing case ticket
    ESC1 = os.startfile(path)

# Service request creation commands
def Service_R():
    print("*******************************************************************")
    NE = input("                     New [N] or Exiting [E]: ")
    print("*******************************************************************")
    if NE == "N":
        NSC()
        print("===========================  New Ticket ===========================")
        print("*******************************************************************")
    else:
        ESC()

        print("========================= Existing Ticket =========================")
        print("*******************************************************************")
    td1 = datetime.now().strftime("%m-%d-%Y %H:%M:%S GMT")
    print("||     Call in Time     ||: " + td1)
    CN = input("||   Enter Caller Name  ||: ")
    SRD = input("|| Enter SR Description ||: ")
    SR = input("||   Enter S-R number   ||: ")
    td2 = datetime.now().strftime("%m-%d-%Y %H:%M:%S GMT")
    input("||   Action  Required   ||: ")
    print("||     Call End Time    ||: " + td2)
    print("===================================================================")
    NSR = input("Create New SR? Yes[y] or No[n]: ")
    if NSR == "y":
        NSR2 = input("Please confirm new ticket creation Yes[y] or No[n]: ")
        if NSR2 == "y":
            Service_R()
        else:
            END()
    elif NSR == "n":
        NSR3 = input("Are you sure? Yes[y] or No[n]: ")
        if NSR3 == "y":
            END()
        if NSR3 == "n":
            Service_R()
    else:
        END()


Service_R()