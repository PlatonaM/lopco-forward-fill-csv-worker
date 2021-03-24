"""
   Copyright 2021 InfAI (CC SES)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""


import os
import uuid
import requests


dep_instance = os.getenv("DEP_INSTANCE")
job_callback_url = os.getenv("JOB_CALLBACK_URL")
input_file = os.getenv("source_csv")
delimiter = os.getenv("delimiter")
target_columns = set(os.getenv("target_columns").split(delimiter))
data_cache_path = "/data_cache"


output_file = uuid.uuid4().hex

print("forward filling values ...")
print("number of target columns: {}".format(len(target_columns)))
with open(os.path.join(data_cache_path, input_file), "r") as in_file:
    first_line = in_file.readline().strip()
    first_line = first_line.split(delimiter)
    value_map = dict()
    for col in target_columns:
        value_map[first_line.index(col)] = str()
    positions = value_map.keys()
    with open(os.path.join(data_cache_path, output_file), "w") as out_file:
        out_file.write(delimiter.join(first_line) + "\n")
        line_count = 1
        for line in in_file:
            line = line.strip().split(delimiter)
            for pos in positions:
                if line[pos]:
                    value_map[pos] = line[pos]
                else:
                    line[pos] = line[pos] or value_map[pos]
            out_file.write(delimiter.join(line) + "\n")
            line_count += 1

with open(os.path.join(data_cache_path, output_file), "r") as file:
    for x in range(5):
        print(file.readline().strip())
print("total number of lines written: {}".format(line_count))

try:
    resp = requests.post(
        job_callback_url,
        json={dep_instance: {"output_file": output_file}}
    )
    if not resp.ok:
        raise RuntimeError(resp.status_code)
except Exception as ex:
    try:
        os.remove(os.path.join(data_cache_path, output_file))
    except Exception:
        pass
    raise ex
