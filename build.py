from datetime import datetime
import os
from zoneinfo import ZoneInfo

def update_time():
    # Read in the file
    with open("./index.html", "r") as file:
        filedata = file.read()

    # Get the current time and place it in the html file
    current_time = datetime.now(ZoneInfo("America/New_York"))
    filedata = filedata.replace("CURRENT_TIME_HERE", str(current_time))

    # Make the "out" folder
    os.makedirs("./out", exist_ok=True)

    # Write the file to the "out" folder
    with open("./out/index.html", "w") as file:
        file.write(filedata)


update_time()