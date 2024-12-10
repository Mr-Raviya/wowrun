import subprocess

try:
    # Run main.py
    subprocess.run(["python3", "auth.py"])
    
    # Run game.py
    subprocess.run(["python3", "game.py"])

except KeyboardInterrupt:
    print("\n")
