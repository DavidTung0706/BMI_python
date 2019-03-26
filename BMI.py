x = float(input("請輸入身高,單位為公分:"))
y = float(input("請輸入體重,單位為公斤:"))
bmi =float (y/(x*x)*10000)
if(bmi<18.5):
    print("your BMI is " + str(bmi) + " 您的體重過輕")
elif(bmi > 18.5 and bmi < 25):
    print("your BMI is " + str(bmi) + ' 您的體重正常')
elif(bmi > 25 and bmi < 30):
    print("your BMI is " + str(bmi) + " 您的體重過重")
else:
    print("your BMI is " + str(bmi) + " 您的體重肥胖")

