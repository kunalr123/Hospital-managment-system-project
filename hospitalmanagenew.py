# for add patient record

patients={}
def add_patient_record():
    patient_name=input("enter patient name:")
    age=int(input("enter age of patient:"))
    sex=input("enter sex of patient:")
    doctor_name=input("enter doctor name:")
    disease=input("enter disease:")
    blood_group=input("enter blood group:")

    patient_record={'Name':patient_name,'Age':age,'Sex':sex,'Doctor name':doctor_name,'disease':disease,'blood group':blood_group}

    patients[patient_name]=patient_record
    print("patient record added successfully")
    

#for view all records

def view_all_records():
    for patient in patients:
        print(patients[patient])

#for search record

def search_patient_record():
            search_name=input("enter patient name to search:")
            if search_name in patients:  
                print(patients[search_name])
            else:
                print("patient not found")
                        

#for remove patient record

def remove_patient_record():
          remove_name = input("Enter patient name to remove: ")
          if remove_name in patients:
            del patients[remove_name]
            print("Patient record deleted successfully")
          else:
            print("Patient not found")

         
#for modify patient record

def modify_patient_record():
               modify_patient_name=input("enter patient name to modify:")
               if modify_patient_name in patients:
                  patients[modify_patient_name]['patient_name']=input("enter new name:")
                  patients[modify_patient_name]['age']=input("enter new age:")
                  patients[modify_patient_name]['doctor_name']=input("enter new doctor name:")
                  patients[modify_patient_name]['disease']=input("enter new disease:")
                  patients[modify_patient_name]['blood_group']=input("enter new blood group:")
                  print("patient record modified successfully")   
               else:
                    print("patient not found")

      
while True:
        print("welcome to Hospital Management System ")
        print("1. Add Patient Record")
        print("2. View All Records")
        print("3. Search Patient Record")
        print("4. Remove Patient Record")
        print("5. Modify Patient Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
                add_patient_record()
        elif choice == '2':
                view_all_records()
        elif choice == '3':
              search_patient_record()
        elif choice == '4':
                remove_patient_record()
        elif choice == '5':
                modify_patient_record()
        elif choice == '6':
            break

        else:
          print("Invalid choice. Please try again.")
          
      
 

