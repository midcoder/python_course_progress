sh = input('Enter hours: ')
sr = input('Enter rate: ')
h = float(sh)
r = float(sr)
if h > 40 :
    reg = h * r
    otp = ((h - 40.0) * (r * 0.5))
    xp = reg + otp 

print(xp)