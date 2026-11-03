hour = int(input("Hour (0-23): "))
minute = int(input("Minute (0-59): "))

if hour < 0 or hour > 23 or minute < 0 or minute > 59:
    print("Invalid time")
else:
    total = hour * 60 + minute
    if total < 600:
        print("On time +5")
    elif total < 1020:
        print("Late, no points")
    else:
        print("Training day is over")

    ## 10:00 ما تنحسب بدري لأن 600 مو أصغر من 600
# لذلك الشرط الأول ما يشتغل
# ويروح للشرط اللي بعده ويطبع Late, no points
