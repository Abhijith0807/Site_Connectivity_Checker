#import argparse library
import argparse
import http.client
import emoji
from codetiming import Timer

myparser  = argparse.ArgumentParser(description = 'Site connectivity checker')
myparser.add_argument('-c','--check', type = str , help = 'Checks the site connectivity status', nargs= '*')
args = myparser.parse_args()

def site_checker(site_list):
    with Timer(text="total Elapsed time: {milliseconds:.0f} ms"):
        for i in site_list:
            timer = Timer(text="Elapsed time: {milliseconds:.0f} ms")
            timer.start()
            conn = http.client.HTTPSConnection(i)
            conn.request("GET", "/")
            r1 = conn.getresponse()
            if r1.status == 200:
                print(emoji.emojize("The status of '"+str(i)+"' is online!!:thumbs_up:"))
            else:
                print(emoji.emojize("The status of '"+str(i)+"' is "+ str(r1.reason) + "!!:thumbs_down:"))
            conn.close()
            timer.stop()

if __name__ == "__main__":
    site_checker(args.check)