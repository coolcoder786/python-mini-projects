import time
from plyer import notification

if __name__=="__main__":
    while True:
        notification.notify(
            title="***please go for studies",
            message="study is also important so pls go for your studies  ,  code later",

            timeout=5
        )
        time.sleep(60*60)