import os


class Commands:
    def __init__(self, source=None):
        self.source = source

    def wrap_cmd_with_source(self, cmd):
        """Source a bash or zsh script before executing every command"""
        if self.source:
            source = "source {}; ".format(self.source)
            return source + cmd
        return cmd

    def build_cmd(self, app, script_path, args=""):
        """For execution on interactive nodes"""
        script_dir, script = os.path.split(script_path)
        cmd = ""
        if script_dir != '':
            cmd += "cd {}; ".format(script_dir)
        cmd += "{} {} {}".format(app, script, args)
        return self.wrap_cmd_with_source(cmd)

    def submit_job_cmd(self, submit_cmd, app, script_path, args=""):
        """For batch submissions"""
        script_dir, script = os.path.split(script_path)
        cmd = ""
        if script_dir != '':
            cmd += "cd {}; ".format(script_dir)
        cmd += "{} {} '{} {}'".format(submit_cmd, app, script, args)
        return self.wrap_cmd_with_source(cmd)
