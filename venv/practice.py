even=[2,4,6,8,10]
odd=[1,3,5,7,9]
def authentication(username,password):
  #username=input('Enter Username: ')
  #password=input('Enter Password: ')
  if username.upper()=='UMA' and password.upper()=='UMA':
      print(' User is valid ')
  else:
      print(' User is not valid ')

def area_of_circle(radius):
    #radius=int(input('Enter radius: '))
    pi=3.14
    area=pi*(radius**2)
    return area
    #print(' Area is: ',area)

