import pandas as pd
import datetime
import smtplib
import schedule

def mailSend(sendMail):
        
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("Sender Mail ID", "Password")
        message="Happy Birthday"
        server.sendmail("Sender Mail ID", sendMail, message)
        print("\n Mail Send Successfully....")
        server.quit()

def xlRead():
    dict = {}

    currentDate = datetime.datetime.now()
    
    Day = currentDate.day
    Month = currentDate.month
    dict = {}
    namedict = {}
    sendMail = list()
    
    newList = list()
    
    try : 
        
        data = pd.read_excel("file.xlsx")
        
    except Exception as e:
        
        print("Exception as : ",e)
        
    yearlist=data["year"].tolist()

    monthlist=data["month"].tolist()
        
    datelist=data["date"].tolist()    
    
    mailList=data["mail"].tolist()
    
    for i in range(len(mailList)):
        dict[mailList[i]]=datelist[i]
    
    for i in monthlist:
        if Month==i:
            for keys in dict:
                if dict[keys]==Day:
                    sendMail.append(keys) 
            break
    
    for i in sendMail:
        for keys in namedict:
            if i==keys:
               newList.append(namedict[keys])
    
    mailSend(sendMail)

def main():
    xlRead()
    schedule.every().day.at("20:18").do(xlRead)
    
    while True:
        schedule.run_pending()

if __name__=="__main__":
    main()
