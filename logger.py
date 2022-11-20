from datetime import datetime


def log(msg):
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    dtime = now.strftime("%H:%M:%S")

    print(date + ' ' + dtime + ' ' + str(msg))

    with open('logs/' + date + ".log", "a") as log_file:
        log_file.write(dtime + ' ' + str(msg) + "\n")
