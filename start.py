import subprocess

command = "bash -c 'source myenv/bin/activate && python port_scanner.py'"

subprocess.run(command, shell=True, check=True)
