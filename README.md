## Test Selenium

This repo is based on Selenium List for Tech With Tim:
https://www.youtube.com/playlist?list=PLzMcBGfZo4-n40rB1XaJ0ak1bemvlqumQ

I will start for following his steps, and then create branches to test other sites and applications.

To install run 
'''
pip install -r requirements.txt
'''

### ALGORITM TO ASSOCIATE BOOKINGS

- Access Login screen
- Fill User
- Fill password
- press enter
- sleep 5 minutes
- Access Booking Association MFE
- Read JSON FILE
- Fill Form
- Press Enter
- Sleep 3 seconds
- Access Booking Association MFE Again

### AlGORITM TO DELETE ALL ASSOCIATION

- Use oauth path to access token
- read json 
- call delete api