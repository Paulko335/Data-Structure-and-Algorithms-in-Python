# This script needs to be placed inside the directory of a chapter to work, ex: inside Chap_1
# Chap_1 folder must be empty before running this script
# It creates directories for every exercise in the chapter
# Set the parameters to the correct numbers for exericises and chapter
import os

# Parameters
chapter = 6
R = [i for i in range(1, 15)]
C = [i for i in range(15, 32)]
P = [i for i in range(32, 38)]

os.mkdir("Reinforcement")
os.mkdir("Creativity")
os.mkdir("Projects")

# Reinforcement
for number in R:
    dir_name = "Reinforcement/R-{}.{}".format(chapter, number)
    os.mkdir(dir_name)

    script_name = "R-{}.{}".format(chapter, number)
    with open("{}/{}.py".format(dir_name, script_name), "w") as script:
        print("#{}".format(script_name), file = script)


# Creativity
for number in C:
    dir_name = "Creativity/C-{}.{}".format(chapter, number)
    os.mkdir(dir_name)

    script_name = "C-{}.{}".format(chapter, number)
    with open("{}/{}.py".format(dir_name, script_name), "w") as script:
        print("#{}".format(script_name), file = script)


# Productivity
for number in P:
    dir_name = "Projects/P-{}.{}".format(chapter, number)
    os.mkdir(dir_name)

    script_name = "P-{}.{}".format(chapter, number)
    with open("{}/{}.py".format(dir_name, script_name), "w") as script:
        print("# {}".format(script_name), file=script)