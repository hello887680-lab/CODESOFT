import random
import string
def password_generate():
    try:
        length= int(input('Enter the length of the password : '))
        c=(string.ascii_uppercase+string.ascii_lowercase+string.punctuation+string.digits)
        password=''
        if length<=0:
            print('Enter number greater than zero to get output.')
        else:
            for i in range(length):
                password+=random.choice(c)
            print('GENERATED PASSWORD = ',password)

    except  ValueError:
        print("ENTER NUMBER ONLY.")

def main():
    password_generate()

if __name__=="__main__":
 main()
