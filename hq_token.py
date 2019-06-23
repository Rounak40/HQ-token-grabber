import requests
import json
api = "https://api-quiz.hype.space"
def send_verification(phone,method):
    headers = {
        'Accept-Encoding': "br, gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'User-Agent': "HQ-iOS/105 CFNetwork/894 Darwin/17.4.0",
        'x-hq-client': "iOS/1.3.16 b105",
        'x-hq-device': "iPhone9,3",
        }
    response = requests.post(api+"/verifications", data="phone=%2B" + str(phone) + "&method=" + str(method), headers=headers).json()
    if "verificationId" in response:
        return {"verificationId": response["verificationId"]}
    elif "error" in response:
        if response["error"] == "not authorized":
            return {"error": "Your IP is banned."}
        else:
            return {"error": response["error"]}
    else:
        return response
def verify_verification(verificationId,code):
    headers = {
        'Accept-Encoding': "br, gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'Connection': "keep-alive",
        'User-Agent': "HQ-iOS/105 CFNetwork/894 Darwin/17.4.0",
        'x-hq-client': "iOS/1.3.16 b105",
        'x-hq-device': "iPhone9,3",
        }
    response = requests.post(api+f"/verifications/{verificationId}", data="code=" + code, headers=headers).json()
    if "accessToken" in response["auth"]:
        return {"accessToken": response["auth"]["accessToken"], "username":response["auth"]["username"]}
    elif "error" in response:
        if response["error"] == "not authorized":
            return {"error": "Your IP is banned."}
        else:
            return {"error": response["error"]}
    else:
        return {"error": "Account not found."}
def main():
    number = input("Please enter the number with country prefix for example (+15412541742):\n")
    method = input("Enter Method (sms/call):\n")
    r = send_verification(number,method)
    if "verificationId" not in r:
        return print(r["error"])
    code = input("Enter verification code that you recieved:\n")
    r2 = verify_verification(r["verificationId"],code)
    if "accessToken" not in r2:
        return print(r["error"])
    print(f'{r2["username"]}\'s access token:\n==============\n{r2["accessToken"]}\n==============')
while True:
    main()
        
    
