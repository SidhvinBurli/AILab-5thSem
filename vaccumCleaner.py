
def vacuum_world():
     
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

     
    location_input = input("Enter loc of vacuum (A/B): ").strip().upper()
    status_input = input(f"Enter status of {location_input} (0 for Clean, 1 for Dirty): ").strip()
    status_input_complement = input(f"Enter status of other room ({'B' if location_input == 'A' else 'A'}): ").strip()

    print("Initial Location Condition: " + str(goal_state))

    if location_input == 'A':
        print("Vacuum is placed in Location A")

        if status_input == '1':   
            print("Location A is Dirty.")
           
            goal_state['A'] = '0'
            cost += 1   
            print("Cost for CLEANING A: " + str(cost))
            print("Location A has been Cleaned.")

            if status_input_complement == '1':   
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1   
                print("Cost for moving RIGHT: " + str(cost))
                
                goal_state['B'] = '0'
                cost += 1  
                print("Cost for CLEANING B: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean.")
        else:
            print("Location A is already clean.")

            if status_input_complement == '1':   
                print("Location B is Dirty.")
                print("Moving right to Location B.")
                cost += 1   
                print("Cost for moving RIGHT: " + str(cost))
                
                goal_state['B'] = '0'
                cost += 1  
                print("Cost for CLEANING B: " + str(cost))
                print("Location B has been Cleaned.")
            else:
                print("Location B is already clean.")

    else:   
        print("Vacuum is placed in Location B")

        if status_input == '1':   
            print("Location B is Dirty.")
          
            goal_state['B'] = '0'
            cost += 1   
            print("Cost for CLEANING B: " + str(cost))
            print("Location B has been Cleaned.")

            if status_input_complement == '1':   
                print("Location A is Dirty.")
                print("Moving left to Location A.")
                cost += 1  
                print("Cost for moving LEFT: " + str(cost))
               
                goal_state['A'] = '0'
                cost += 1  # 
                print("Cost for CLEANING A: " + str(cost))
                print("Loc A has been Cleaned.")
            else:
                print("Loc A is already clean.")
        else:
            print("Loc B is already clean.")

            if status_input_complement == '1':   
                print("Loc  A is Dirty.")
                print("Moving left to Loc  A.")
                cost += 1   
                print("Cost for moving LEFT: " + str(cost))
               
                goal_state['A'] = '0'
                cost += 1  
                print("Cost for CLEANING A: " + str(cost))
                print("Loc A has been Cleaned.")
            else:
                print("Loc A is already clean.")

    
    print("GOAL STATE: ")
    print(goal_state)
    print("Perf Measurement: " + str(cost))

 
vacuum_world()
