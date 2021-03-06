#!/usr/bin/python
import subprocess

# http://www.emacswiki.org/emacs/OfflineIMAP

def get_output(cmd):
    # Bunch of boilerplate to catch the output of a command:
    pipe = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    (output, errout) = pipe.communicate()
    assert pipe.returncode == 0 and not errout
    return output

def get_password_emacs(host, login, port):
    cmd = "emacsclient --eval '(offlineimap-get-password \"%s\" \"%s\" \"%s\")'" % (host,port,login)
    return get_output(cmd).strip().lstrip('"').rstrip('"')
