import os, sys
from src.game import main

# Set the working directory to the folder where the .exe file is running
os.chdir(os.path.dirname(sys.argv[0]))

if __name__ == "__main__":
    main()
