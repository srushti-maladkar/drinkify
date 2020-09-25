# Problem Statement:
# ----------------------------------------------------------------------
# Notify after 90 mins
# Display messages showing benefits and keeps motivating

# Flow
# ----------------------------------------------------------------------
# Schedule to run function after 90 mins

import time

from win10toast import ToastNotifier

toaster = ToastNotifier()

while True:
    toaster.show_toast("Glub Glub Glub...🥤",
                       "Your body needs a glass of Water",
                       "C:/Users/smala/Desktop/Python Tutorial/drinkify/Images/drink_119593.ico",
                       duration=10)

    time.sleep(3.0)
