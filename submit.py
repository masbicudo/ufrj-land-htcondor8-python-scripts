#!/usr/bin/python3.6
####################
# submit.py
####################
import os
import htcondor
import subprocess

print(htcondor.version())

os.makedirs("out", exist_ok=True)
os.makedirs("result", exist_ok=True)

subprocess.run(["tar", "-czf", ".venv.tar.gz", ".venv"])

schedd = htcondor.Schedd()

sub = htcondor.Submit({
        "executable": "job.sh",
        "output": "out/$(Process).out",
        "log": "out/$(Process).log",
        "error": "out/$(Process).err",
        "should_transfer_files": "YES",
        "transfer_input_files": "job.py, .venv.tar.gz",
        "transfer_output_files": "result",
    })

with schedd.transaction() as txn:
    for i, v in enumerate(["first", "second", "third"]):
        sub["arguments"] = f"-o {i} -v {v} -p $(Process)"
        for _ in range(2):
            sub.queue(txn)
