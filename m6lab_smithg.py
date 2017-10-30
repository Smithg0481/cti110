#CTI 110
# M6Lab
#Smith G
#Oct 30, 2017
#

def main():
    name = input("what is your name? ")
    greet(name)
    age = int(input('How old are you? '))
    print(ageCategory(age))
                      

def greet(name):
    print('Hello' ,name)

def ageCategory(age):
#Define if infant child teen or adult

    if age <= 1 :
        category='You are a infant'
    elif age <= 12 :
        category= 'You are a Child'
    elif age <= 19 :
        category = 'You are a Teenager'
    else:
        category = "You are an adult"
    return category
    

  
        















main()
