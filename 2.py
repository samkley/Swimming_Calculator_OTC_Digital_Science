import easygui

# id format of gender.pool_length.swim_stroke.swim_dist so for example: male25butterfly100
wr_times = {"male50freestyle50": 20.91, "male50freestyle100": 46.86, "male50freestyle200": 102.00,
            "male50freestyle400": 220.07, "male50freestyle800": 452.12, "male50freestyle1500": 871.02,
            "male50backstroke50": 23.71, "male50backstroke100": 51.60, "male50backstroke200": 111.92,
            "male50breaststroke50": 25.95, "male50breaststroke100": 56.88,
            "male50breaststroke200": 125.95, "male50butterfly50": 22.27, "male50butterfly100": 49.45,
            "male50butterfly200": 110.34, "female50freestyle50": 23.67, "female50freestyle100": 51.71,
            "female50freestyle200": 112.98,
            "female50freestyle400": 236.40, "female50freestyle1500": 920.48, "female50backstroke50": 26.98,
            "female50backstroke100": 57.45, "female50breaststroke50": 29.30, "female50breaststroke100": 64.13,
            "female50breaststroke200": 138.95, "female50butterfly50": 24.43, "female50butterfly100": 55.48,
            "female50butterfly200": 121.81, "male25freestyle50": 20.16, "male25freestyle100": 44.84,
            "male25freestyle200": 99.37, "male25freestyle400": 212.25, "male25freestyle800": 443.42,
            "male25freestyle1500": 846.88, "male25backstroke50": 22.22, "male25backstroke100": 48.33,
            "male25backstroke200": 105.63, "male25breaststroke50": 24.95, "male25breaststroke100": 55.28,
            "male25breaststroke200": 120.16, "male25butterfly50": 21.75, "male25butterfly100": 49.28,
            "male25butterfly200": 109.63, "female25freestyle50": 22.93, "female25freestyle100": 50.25,
            "female25freestyle200": 110.31, "female25freestyle400": 233.92, "female25freestyle800": 479.34,
            "female25freestyle1500": 918.01, "female25backstroke50": 25.27, "female25backstroke100": 54.89,
            "female25backstroke200": 118.94,
            "female25breaststroke50": 28.56, "female25breaststroke100": 62.36, "female25breaststroke200": 134.57,
            "female25butterfly50": 24.38, "female25butterfly100": 54.59, "female25butterfly200": 119.61}


# function to display an error message in case a value is negative
def errorbox():
    easygui.msgbox(msg="Something went wrong. It seems like one value is negative."
                       " Please double check that you have entered the correct values.")
    main()


# convert h:m:s,s to seconds
def get_ms(time_str):
    h, m, s, ms = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 100


# convert hours, minutes and seconds to seconds
def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def main():
    # if statement to check whether user would like to start the program
    if easygui.ccbox(msg="Welcome to the Swimming Calculator where time per lapse, number of lapses and time to a"
                         " specific world record can be calculated accurately and quickly. If you want to continue"
                         " press 'CONTINUE', otherwise press 'CANCEL' to exit this program",
                     title="Welcome to the one and only Swimming Calculator!", ):

        # buttonbox to ask user what their gender is
        gender = easygui.buttonbox(msg="Please choose your gender, this is required so that the correct world record "
                                       "time can be identified", title="Gender selection",
                                   choices=["Male", "Female"]).lower()

        # choice box to ask user to select the pool length
        pool_length = easygui.choicebox(msg="Please select the length of the pool you wish to swim in, in meters!",
                                        title="Pool length selection", choices=[12.5, 25, 50])

        # integer box to ask user to input to enter how far they want to swim for
        swim_dist = easygui.integerbox("Please enter how far you want to swim , in meters. This number should be an"
                                       " integer and a multiple of your Pool's length", title="Swim Distance",
                                       upperbound=9999, lowerbound=25)

        # enter box to ask user for how long they want to swim for
        swim_time_old = easygui.enterbox(msg="Please enter how long you want to swim for, please follow the format of"
                                             " HH:MM:SS", title="Time of total swim")

        # buttonbox to ask user to select what stroke they want to swim in
        swim_stroke = easygui.buttonbox(msg="Please select in which stroke you want to swim.",
                                        title="Swim stroke selection", choices=["Butterfly", "Breaststroke",
                                                                                "Backstroke", "Freestyle"]).lower()
        # calculation to get the user specific id
        identification = gender + str(pool_length) + swim_stroke + str(swim_dist)

        try:
            swim_time_new = get_sec(swim_time_old)
            lapse_num = swim_dist / float(pool_length)
            time_per_lapse = swim_time_new / lapse_num

            if swim_time_new < 0 or lapse_num < 0:
                negative = 0

            else:
                negative = 1

        # checks for possible errors and informs the user according to what error occurred
        except ValueError:
            easygui.msgbox(msg="You have entered at least one incorrectly formatted value. Please re-run the program"
                               " and make sure to enter valid values.")
            main()

        except TypeError:
            easygui.msgbox(msg="You have skipped at least one input box and have therefore not entered all required "
                               "values. Please re-run the program and make sure to enter all values.")
            main()

        except AttributeError:
            easygui.msgbox(msg="You have skipped at least one input box and have therefore not entered all required "
                               "values. This means the program can not run as expected."
                               " Please re-run the program and make sure to enter all values.")
            main()

        # asks user if they want to calculate time to world record
        if easygui.ccbox(msg="Would you like to proceed and calculate how much faster you have to swim"
                             " to beat the current world record for the distance, gender and stroke you have specified?"
                             " If you want to continue with it select 'CONTINUE' otherwise 'CANCEL'"
                             " to not calculate the time to world record and only get time per lapse and"
                             " amount of lapses output", title="World record choice"):
            try:
                # finds value in dictionary for key id
                id = wr_times[identification]

                # coverts wr time to seconds and minutes
                id1 = id // 60
                id2 = id % 60
                id2new = round(id2, 2)
                id1new = round(id1, 2)

                # asks user to enter their personal best to calculate the difference to the world record
                personal_best_old = easygui.enterbox(msg="The current world record for the gender, stroke, distance"
                                                         " and pool length is {} minutes and {} seconds. "
                                                         "Please enter your personal best for the stroke and distance"
                                                         " you have specified before in the format of HH:MM:SS:SS.   "
                                                         "Make sure that if your time is less than a second at the end,"
                                                         " you include it after the first SS (full seconds). "
                                                         "For example: if you have a time of 1 hour, 20 minutes, and "
                                                         "5.04 seconds you would enter: 01:20:05:04.".format(id1new,
                                                                                                             id2new))

                try:
                    personal_best_new = get_ms(personal_best_old)
                    id = wr_times[identification]
                    time_to_wr_new = personal_best_new - id

                # checks if an error occurred
                except ValueError:
                    easygui.msgbox(msg="You have entered at least one incorrectly formatted value."
                                       " Please re-run the program and make sure to enter valid values.")

                # checks if time to wr is bigger than 60 and if it is converts it to minutes and sets unit to minutes
                if time_to_wr_new > 60:
                    time_to_wr_new /= 60
                    unit = "minutes"

                else:
                    # if time to wr is less than a minute it will stay as seconds with the unit seconds
                    unit = "seconds"

                # msg box to output time to wr
                easygui.msgbox(msg="To beat the world record you will need to swim {:.2f} {} faster"
                               .format(time_to_wr_new, unit))

            # checks for possible error
            except KeyError:
                easygui.msgbox(msg="Sorry, there is no world record time for that distance and stroke combination.")

                # checks if a value is negative
            if negative == 0:
                # displays error function for negative value
                errorbox()

            else:
                # if no error occurred calculated values are output in a msg box
                easygui.msgbox(msg="To swim {} metres in {} seconds in a {} metre pool you will need to swim {:.2f}"
                                   "seconds per lapse. You will have to swim a total of {} lapses."
                               .format(swim_dist, swim_time_new, pool_length, time_per_lapse, lapse_num))

            # cc box informing the user about the end of the program and asking them if they want to run it again or not
            if easygui.ccbox(msg="This is the end of the program. I hope you are satisfied with the results. "
                                 "To run the program again click on 'CONTINUE', otherwise 'CANCEL'; to exit it. "
                                 "Either way, have a great day and goodbye!"):

                # re-runs the main function/program if the user selected Continue
                main()
            else:
                quit()

        else:

            # checks if a value is negative
            if swim_time_new or lapse_num < 0:
                negative = 0
            else:
                negative = 1

            if negative == 0:
                errorbox()

            else:
                # msg box with output of all appropriate variables
                easygui.msgbox(msg="To swim {} metres in {} seconds in a {} metre pool you will need to swim {:.2f}"
                                   " seconds per lapse. You will have to swim a total of {} lapses"
                               .format(swim_dist, swim_time_new, pool_length, time_per_lapse, lapse_num))


    else:
        # asks user to confirm that they wish to exit the program
        if easygui.ccbox(msg="Are you sure you want to exit the program, there is no way to undo this."
                             " You will have to re-open the program if you wish to use it again."
                             " Press 'CONTINUE' to go back to the program and 'CANCEL'"
                             " to exit it!", title="Are you sure?"):
            # if user wants to continue the program it is re-run
            main()

        else:
            easygui.msgbox(msg="Sad to see you go, goodbye 👋!")

            quit()


main()