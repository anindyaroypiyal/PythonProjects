import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title= "Take a Break n Take a walk. It's been a while.",
            message= "Strech your legs.\n"
                     "Improve your mood.\n"
                     "Generate better ideas.\n"
                     "Understand better.",
            app_icon = "C:/Users/royan/PycharmProjects/ProjecX/walkk.ico",
            timeout= 6
        )
        time.sleep(40*60)
