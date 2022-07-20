from paramiko import SSHClient, AutoAddPolicy
import subprocess
import os


class BackendManager:
    def __init__(self, server, uname):
        self.server = server
        self.uname = uname

        self.client = SSHClient()
        self.client.set_missing_host_key_policy(AutoAddPolicy())
        self.connected = False

    def connect(self):
        self.client.connect(self.server, username=self.uname)
        self.connected = True

    def close(self):
        self.client.close()
        self.connected = False

    def check_if_file_exists(self, file_path):
        if self.connected:
            cmd = "test -f {};".format(file_path)
            _, stdout, _ = self.client.exec_command(cmd)
            ret = stdout.channel.recv_exit_status()
            if stdout.channel.recv_exit_status() == 0:
                return True
            return False
        return -1

    def copy_from_backend(self, backend_path, local_path):
        call = 'scp {uname}@{server}:{backend_path} {local_path}'.format(uname=self.uname,
                                                                         server=self.server,
                                                                         backend_path=backend_path,
                                                                         local_path=local_path)
        print(call)
        try:
            ret = subprocess.check_output(call.split())
            print(ret)
            return 0
        except Exception as e:
            print(e)
            return 1

    def run_cmd(self, cmd):
        if self.connected:
            print(cmd)
            _, stdout, _ = self.client.exec_command(cmd)

            if stdout.channel.recv_exit_status() == 0:
                return stdout, 0
            print("Error: ", stdout.channel.recv_exit_status())
            return stdout, 1

        return None, -1

    def check_slrum_status(self, jobname):
        if self.connected:
            cmd = "squeue --format=\"%.18i %.9P %.30j %.8u %.8T %.10M %.9l %.6D %R\" --me"
            _, stdout, _ = self.client.exec_command(cmd)
            ret = stdout.readlines()
            for j in ret:
                if jobname in j.split():
                    print(j)
                    return 2

            print(ret)
            return 0
        return -1

    def debug_cmd(self, cmd):
        call = 'ssh -l {} {}'.format(self.uname, self.server).split()
        ret = subprocess.check_output(call + [cmd, ])
        print(ret)

