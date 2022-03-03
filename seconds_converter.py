
seconds = input("Enter the number of seconds you wish to convert to hours:")  #promt input

try:                    # if the input is not a number gives an Error
    isec = int(seconds)
    hours = isec // 3600                        #divides the seconds in hours with no remainder
    secs_remaining = isec % 3600                #takes hthe seconds
    minutes =  secs_remaining // 60             #transforms seconds in minutes
    final_secs = secs_remaining  % 60           #takes the seconds remaining

    print("Hrs="+  str(hours) + "\n" + "mins=" + str(minutes) + "\n" + "secs="+ str(final_secs))
except:
    print("The input is not a number")
