import cv2
from pathlib import Path

# loading the image

image_name = input("Enter your image name: ")

if not Path(image_name).is_file():
    print("Please choose a valid image (check your image name  and re-run the code..)")
else:
    image = cv2.imread(image_name)
    image=input("Enter your image name  : ")
    input_img= cv2.imread(image)

    if input_img is not None:
        print(" coloured image loaded .. ")

        # grey scale conversion 
        gray=cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
        command_1=input("to convert into black and white press BnW :")
        if(command_1=="BlW"):
            print("the black and white image is loaded .., what action do you want to perform")

        # display it 

        command1=input("type show to show the image  :")

        #Show

        if command1.lower().strip()=="show":
            cv2.imshow("title window",gray)
            key=cv2.waitKey(0)
            cv2.destroyAllWindows()

        #Save
        command2=input("Do you want to save your image : ")
        if command2.lower().strip()=="yes":
            output_name=input("do you a name for our output_image: ")
            cv2.imwrite("output_name".jpg,gray)
            print("Image saved successfully ...")
        elif command2.lower().strip()=="no":
            print("Thankyou ..see you again ...")

    else:
        print("please choose a valid image (check your image name..)")

