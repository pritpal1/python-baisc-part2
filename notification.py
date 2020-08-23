import time
from win10toast import ToastNotifier
#one time initialization
toaster = ToastNotifier()

#show notification whenever needed
toaster.show_toast("Programming Soup!","You Got the Notification",
                   icon_path=None,duration=10,threaded=True)# 10 seconds
#to check if any notifications are active ,use toaster.notification_active()
while toaster.notification_active():
    time.sleep(0.1)
