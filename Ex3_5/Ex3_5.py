import argparse 
pA = argparse.ArgumentParser()
pA.add_argument('a',type=str)
args = pA.parse_args() 
commonds=['/e','/u','/n','/g']
if args.a in commonds[0:4]:
    print("Option is known")
else: 
    print("Wrong option")