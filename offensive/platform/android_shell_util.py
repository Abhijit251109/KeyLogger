import subprocess

def terminal_write(command: str, usr_root=True):

    if not usr_root :
        command = f"su -c" or f"sudo {command}"

        try:
            result = subprocess.run(command,
                                    shell=True,
                                    capture_output=True,
                                    text=True,
                                    check=True
            )

            return result.stdout.strip()

        except subprocess.CalledProcessError as e:
            print(f"an erron {e} occured trying to run")
            pass