import sqlite3

N = True
while N:
    def check_email():
        conn = sqlite3.connect('emails.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM emails")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

    def check_services():
        conn = sqlite3.connect('services_data.sqlite')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM services")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.close()

    def delete_emails():
        try:
            conn = sqlite3.connect('emails.sqlite')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM emails")
            conn.commit()
            conn.close()
            print("All records from 'emails' table have been deleted.")
        except sqlite3.Error as e:
            print(f"An error occurred while cleaning 'emails': {e}")


    def delete_services():
        try:
            conn = sqlite3.connect('services_data.sqlite')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM services")
            conn.commit()
            conn.close()
            print("All records from 'services' table have been deleted.")
        except sqlite3.Error as e:
            print(f"An error occurred while cleaning 'services': {e}")

    print("type 1 in order to check emails")
    print("type 2 in order to check notes")
    print("type 3 in order to clean databases")
    print("type 0 in order to close programm")
    A = int(input())
    if A == 1:
        check_email()
    elif A == 2:
        check_services()
    elif A == 3:
        delete_emails()
        delete_services()
    elif A == 0:
        break
    else:
        print("type correct value")