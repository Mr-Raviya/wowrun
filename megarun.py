import subprocess

try:
    # Run auth.py
    print("Running main.py...")
    subprocess.run(["python3", "auth.py"])
    
    # Run game.py
    print("Running game.py...")
    subprocess.run(["python3", "game.py"])

except KeyboardInterrupt:
    print("\nThanks for using MegaRun Hack by Raviya.")
