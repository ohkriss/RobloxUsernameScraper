import threading, re, time, requests
 
user_id = 1
amount = 50
thread_count = 25

output_file = open("usernames.txt", "a", encoding="UTF-8")

def apiReq(params):
    req = requests.get(url="https://www.roblox.com/avatar-thumbnails?params="+params, allow_redirects=False)
    if req.status_code == 200:
        return req.text
    return ""

def thread():
    global user_id
    while True:
        try:
            params = "["
            for i in range(user_id+1, user_id+amount+1):
                params += "{userid:"+str(i)+"},"
            user_id += amount
            params = params[:-1]+"]"
            resp = apiReq(params)
            users = re.findall(r"\"id\":(\d+?),\"name\":\"(.+?)\",", resp)
            for user in users:
                uId, uName = user
                print(uId, uName)
                output_file.write(uId+":"+uName+"\n")
            output_file.flush()
        except Exception as e:
            print("Error ->", e.message)
 
for _ in range(thread_count):
    threading.Thread(target=thread).start()
    time.sleep(0.01)
