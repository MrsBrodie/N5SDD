


def GetFoodWeight():
  #Setting the totalWeight variable to 0 initially
  totalWeight=0.00

  #Creating an array to store 5 values for food weight
  foodWeight=[0.00]*5
  print("     ==== Auto Dog Feeder ====")
  print("")

  #create a fixed loop that will run 5 times to store the values of each container
  for counter in range(5):

    #Ask the user to enter a weight between 1 and 200, with a validation loop to continue to ask the user for the valid weight.
    print("Please enter the weight for container ", counter+1)
    foodWeight[counter]=float(input())
    while foodWeight[counter]<0 or foodWeight[counter]>200:
      print("Invalid, please enter a weight between 0 and 200")
      foodWeight[counter]=float(input("Please emter the weight of food for container "))

    #A running total is used to generate the total weight stored.  
    totalWeight=totalWeight+foodWeight[counter]

  return totalWeight, foodWeight

#define a subprogram to generate and store a message that is appropriate for each users dog.
def GetDogSize(totalWeight):
  DogSize=input("Please enter the size of your dog.  Small, Medium or Large. ")
  
      
  if DogSize=="Small" and totalWeight>=110 and totalWeight<=140:
    message=("This weight of food is ideal for your small dog")
  elif DogSize=="Medium" and totalWeight>=330 and totalWeight<=440:
    message=("This weight of food is ideal for your Medium dog")
  elif DogSize=="Large" and totalWeight>=690 and totalWeight<=900:
    message=("This weight of food is ideal for your Large dog")
  else:
    message=("This weight of food is not recommended for your dog")

  return message


#Calculating the average weight being stored in the feeder.
def GetAverage(totalWeight):
  averageWeight=round(totalWeight/5,1)
  return averageWeight
  
#Displaying all of the information for the user to view.
def DisplayDetails(totalWeight, averageWeight, foodWeight, message):
  for counter in range (5):
    print("Weight ", counter+1 , "is ", foodWeight[counter])

  print ("The total weight is ", totalWeight)
  print("The average food weight is ", averageWeight)
  print(message)




totalWeight, foodWeight=GetFoodWeight()
message=GetDogSize(totalWeight)
averageWeight=GetAverage(totalWeight)
DisplayDetails(totalWeight, averageWeight, foodWeight, message)