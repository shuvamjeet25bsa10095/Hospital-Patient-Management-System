
def display_menu():
    print("Hospital Patient Management System")
    print("1. Add New Patient")
    print("2. View All Patients")
    print("3. Search Patient by ID")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Exit")


def addpatient(patients=None):
    try:
        patientid = input("Enter Patient ID ").strip()
        if not patientid:
            print("Error the ID cannot be empty!")
            return

        name = input("Enter Patient Name ").strip()
        if not name:
            print("Error Name cannot be empty")
            return

        ageinput = input("Enter Patient Age ").strip()
        age = int(ageinput)
        if age < 0 or age > 150:
            print("Error Age must be between 0-120")
            return

        condition = input("Enter Medical Condition: ").strip()
        if not condition:
            print("Error: Condition cannot be empty!")
            return

        newpatient = {"id": patientid, "name": name, "age": age, "condition": condition}
        patients.append(newpatient)
        print(f"Patient {name} (ID: {patientid}) added successfully")
    except ValueError:
        print("Error Age must be a number")
    except Exception as e:
        print(f"Unexpected error {e}")


def viewallpatients():
    if not patients:
        print("No patients in the system yet.")
        return

    print("All Patients")
    print(f"{'ID':<5} {'Name':<15} {'Age':<5} {'Condition'}")
    print("-" * 40)
    for patient in patients:
        print(f"{patient['id']:<5} {patient['name']:<15} {patient['age']:<5} {patient['condition']}")


def searchpatient(patientid):
    for patient in patients:
        if patient["id"].lower() == patientid.lower():
            return patient
    return None


def searchpatientmenu():
    patientid = input("Enter Patient ID to search").strip()
    if not patientid:
        print("Error ID cannot be empty")
        return

    found = searchpatient(patientid)
    if found:
        print("Patient Found")
        print(f"ID: {found['id']}, Name: {found['name']}, Age: {found['age']}, Condition: {found['condition']}")
    else:
        print(" Patient not found")


def updatepatient(newage=None):
    patientid = input("Enter Patient ID to update ").strip()
    if not patientid:
        print("Error ID cannot be empty")
        return

    found = searchpatient(patientid)
    if not found:
        print("Patient not found")
        return

    print(f"Updating {found['name']} (current age: {found['age']}, condition: {found['condition']})")

    newname = input(f"New Name (current: {found['name']} or Enter to keep)").strip()
    if newname:
        found["name"] = newname

    newageinput = input(f"New Age (current: {found['age']} or Enter to keep) ").strip()
    if newageinput:
        try:
            new_age = int(newageinput)
            if 0 <= newage <= 150:
                found["age"] = newage
            else:
                print("Age must be 0-150. Keeping old value.")
        except ValueError:
            print("Invalid age. Keeping old value.")

    newcondition = input(f"New Condition (current: {found['condition']} or Enter to keep): ").strip()
    if newcondition:
        found["condition"] = newcondition

    print("Patient updated successfully!")


def deletepatient():

    patientid = input("Enter Patient ID to delete: ").strip()
    if not patientid:
        print("Error ID cannot be empty")
        return

    found = searchpatient(patientid)
    if not found:
        print("Patient not found!")
        return

    confirm = input(f"Delete {found['name']}choose(y/n)").strip().lower()
    if confirm == 'y':
        patients.remove(found)
        print("Patient deleted successfully")
    else:
        print("Delete cancelled.")


def main():
    print("Welcome to Hospital Patient Management")
    while True:
        display_menu()
        choice = input("Enter your choice from 1 to 6): ").strip()

        if choice == '1':
            addpatient()
        elif choice == '2':
            viewallpatients()
        elif choice == '3':
            searchpatientmenu()
        elif choice == '4':
            updatepatient()
        elif choice == '5':
            deletepatient()
        elif choice == '6':
            print("Thankyou ")
            break
        else:
            print("Invalid choice")

        input("Press Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()