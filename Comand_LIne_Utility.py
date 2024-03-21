import argparse
import sys
def calc(args):
    if args.o=="+":
        return args.x+args.y
    elif args.o=="-":
        return args.x-args.y
    elif args.o=="*":
        return args.x*args.y
    elif args.o=="/":
        return args.x/args.y
    
if __name__ =="main":
    prase=argparse.ArgumentParser()
    prase.add_argument("--x",type=float,default=1.0,help="Enter the 1st number and for for help call 7505316239")
    prase.add_argument("--y",type=float,default=3.0,help="Enter the 2nd number and for for help call 7505316239")
    prase.add_argument("--x",type=str,default="add",help="Enter the operation to perform and for for help call 7505316239")
    args=prase.parse_args()
    sys.stdout.write(str(calc(args)))