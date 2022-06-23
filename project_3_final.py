from tkinter import*
from tkinter import messagebox
import random


#generate password
def generate():
    try:                #try for error handling
        if int(e2.get())>=0:                        #checking if inputs are valid
            length=int(e2.get())
            if int(e3.get())>=0:
                low=int(e3.get())
                if int(e4.get())>=0:
                    up=int(e4.get())
                    if int(e5.get())>=0:
                        num=int(e5.get())
                        if int(e6.get())>=0:
                            sym=int(e6.get())
                            app=nameE.get()
                        else:
                            messagebox.showinfo('error',"Enter a valid number of sybmols")
                    else:
                        messagebox.showinfo('error',"Enter a valid number of numbers")
                else:
                    messagebox.showinfo('error',"Enter a valid number of Upper letters")
            else:
                messagebox.showinfo('error',"Enter a valid number of small letters")
        else:
            messagebox.showinfo('error',"Enter a valid length for you password")
    #checking whether the password components = the length of the original password
        userlen=low+up+num+sym
        if userlen==length:
            password=''
        #creating lists to loop through them and choose randomly based on each element's length
            lowers='a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
            uppers='A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
            symbols='! @ # $ % * / , . " | : + - ~ < > ^ & _ ? [ ] { } ( )'.split()
            numbers='1 2 3 4 5 6 7 8 9 0'.split()
            
        #loop through lists in the range the user specified + adding the chosen characters to the password
            for l in range(low):
                l=random.choice(lowers)
                password=password+l
                #hjfl
            for u in range(up):
                u=random.choice(uppers)
                password=password+u
                #hjflKDV
            for s in range(sym):
                s=random.choice(symbols)
                password=password+s
                #hjflKDV!
            for n in range(num):
                n=random.choice(numbers)
                password=password+n
                #hjflKDV!4
        #convert password to list. to use "random.shuffled()" function to shuffle the order of the pasword list
        # then joining it to string
            shuffled=list(password)#[h,j,f,l,K,D,V,!,4]
            random.shuffle(shuffled)#[j,4,!,h,K,l,V,D,f]
            final='\nYour '+app+' Password is: '+''.join(shuffled)#'j4!hKlVDf'
        #printing the generated password to a file then in the program
            f=open('generatedP.txt','a')
            print(final,file=f)
            f.close()
            la1=Label(root,text=final,fg='snow',bg='CadetBlue4',font=("consolas","12","bold"))
            la1.grid(row=12,column=2)
            
        else:
                messagebox.showinfo('error',"The charachters don't add up to the length")
#Error Handling
    except NameError:
         messagebox.showinfo('NameError',"Something went wrong.. Recheck you inputs")
    except ValueError:
        messagebox.showinfo('ValueError',"Something went wrong.. Recheck you values")
##    except UnboundLocalError:
##        messagebox.showinfo('UnboundLocalError',"Something went wrong.. Recheck you inputs")
##    except SyntaxError:
##        messagebox.showinfo('SyntaxError',"Something went wrong.. Recheck with the coder :)")
##    except KeyboardInterrupt:
##        messagebox.showinfo('KeyboardInterrupt',"You Interupted the running program \n Thankyou :)")
    except:
        messagebox.showinfo('Error',"Sorry!\nSomething went wrong..")
#GUI code
root=Tk()

root.title("Password Generator")
root.geometry("980x300")
root.configure(background='CadetBlue4')

#label_0
la0=Label(root,text="Welcome To Our Password Generator",fg='midnight blue',bg='lightBlue2',font=("Rockwell","16","bold"))
la0.grid(row=0,column=2)


#label_1
la1=Label(root,text="This Program Will Help you Find a Strong Password",fg='lightBlue2',bg='CadetBlue4',font=("Rockwell","13","bold"))
la1.grid(row=1,column=2)


#label_2
la2=Label(root,text="Enter the Full Length of the password",fg='lightBlue2',bg='CadetBlue4',font=("consolas","11","bold"))
la2.grid(row=2,column=0)

e2=Entry(root)
e2.grid(row=2,column=2)


#label_3
la3=Label(root,text="Enter how many Small Letter do you want in your password",fg='lightBlue2',bg='CadetBlue4',font=("consolas","11","bold"))
la3.grid(row=4,column=0)

e3=Entry(root)
e3.grid(row=4,column=2)


#label_4
la4=Label(root,text="Enter how many Capital Letter do you want in your password",fg='lightBlue2',bg='CadetBlue4',font=("consolas","11","bold"))
la4.grid(row=5,column=0)

e4=Entry(root)
e4.grid(row=5,column=2)


#label_5
la5=Label(root,text="Enter how many Number do you want in your password",fg='lightBlue2',bg='CadetBlue4',font=("consolas","11","bold"))

la5.grid(row=6,column=0)

e5=Entry(root)

e5.grid(row=6,column=2)


#label_6
la6=Label(root,text="Enter how many Symbols do you want in your password",fg='lightBlue2',bg='CadetBlue4',font=("consolas","11","bold"))

la6.grid(row=7,column=0)

e6=Entry(root)

e6.grid(row=7,column=2)


#NameLabel Extra
namela=Label(root,text="Enter to what app this password is",fg='lightBlue2',bg='CadetBlue4',font=("consolas","11","bold"))
namela.grid(row=9,column=0)

nameE=Entry(root)
nameE.grid(row=9,column=2)

#generate botton
botton=Button(root,text="Generate",command= generate,fg='navy',bg='lightBlue2',font=("consolas","12","bold"))

botton.grid(row=10,column=2)

root.mainloop()

