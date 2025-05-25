import time
from PCA9685 import PCA9685

time.sleep(1)
time_sleep=1
pwm = PCA9685(0x41)
pwm.setPWMFreq(50)
pwm.setServoPulse(0,500)
print("setServoPulse 500")
time.sleep(time_sleep)
print("sleep %s"%(time_sleep))
pwm.setServoPulse(0,1500)
print("setServoPulse 1500")
time.sleep(time_sleep)
print("sleep %s"%(time_sleep))
pwm.setServoPulse(0,2500)
print("setServoPulse 2500")
time.sleep(time_sleep)
print("sleep %s"%(time_sleep))