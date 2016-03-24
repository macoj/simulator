__author__ = 'marcos'
import os
import time
import sys


class Simulator:
    def __init__(self):
        pass

    @staticmethod
    def execute(commands, number_of_processes=2, delay_between=2, output_dir=None):
        """ Executes commands in parallel at the maximum number_of_processes commands at time.
        :param commands: A list of strings containing the commands that should be executed.
        :param number_of_processes: The number maximum of processes running in parallel.
        :param delay_between: The delay between each check if a process ended or not.
        :param output_dir: The directory in which the helper files will be stored and eventually removed (default: '.').
        :return: None
        """
        if not output_dir:
            output_dir = "."
        if number_of_processes > len(commands):
            number_of_processes = len(commands)
        epoch_time = str(int(time.time()))
        pairs_and_files = dict([(i, (commands[i],
                                     "%s/%s_touch_%d" % (output_dir, epoch_time, i)))
                                for i in range(len(commands))])
        pairs_indices = range(0, len(commands))
        # remove old files
        for index in pairs_indices:
            _, touch = pairs_and_files[index]
            os.system("rm " + touch + " 2> /dev/null")
        threads_started = []
        # pairs_indices can change through the iterations because we can try to retrieve data again
        for index in pairs_indices:
            command, touch = pairs_and_files[index]
            os.system('( ' + command + ' ; touch ' + touch + ' ) &')
            print "> started [%d]: '%s'" % (index, command)
            threads_started.append(index)
            if len(threads_started) < number_of_processes:
                continue
            # if we already started the maximum numbers of processes, we join
            thread_done = None
            while thread_done is None:
                for thread in threads_started:
                    _, touch = pairs_and_files[thread]
                    if os.path.exists(touch):
                        thread_done = thread
                        break
                time.sleep(delay_between)
            print "> finished [%d]" % thread_done
            threads_started.remove(thread_done)
            # total_executed += len(threads_started)
            # sys.stdout.write("%d/%d/%d " % (len(threads_started), total_executed, len(commands)))
            # sys.stdout.flush()
            # threads_started = []
        # for _, touch in pairs_and_files
        while threads_started:
            threads_done = []
            for thread in threads_started:
                _, touch = pairs_and_files[thread]
                if os.path.exists(touch):
                    threads_done.append(thread)
            for thread in threads_done:
                threads_started.remove(thread)
                print "> finished [%d]" % thread
            time.sleep(delay_between)
        sys.stdout.write("\n")
        # remove old files
        for index in pairs_indices:
            _, touch = pairs_and_files[index]
            os.system("rm " + touch + " 2> /dev/null")
