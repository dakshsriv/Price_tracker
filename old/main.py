import subprocess

if __name__ == "__main__":
    subprocess.run("/usr/bin/uvicorn APIPrice:app", shell=True)
    print("Will it ever reach here?")
    # run command uvicorn APIPrice:app
    # run command python3 Price_checker.py
