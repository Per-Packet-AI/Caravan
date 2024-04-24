# *************************************************************************
#
# Copyright 2024 Qizheng Zhang (Stanford University),
#                Ali Imran (Purdue University),
#                Enkeleda Bardhi (Sapienza University of Rome),
#                Tushar Swamy (Unaffiliated),
#                Nathan Zhang (Stanford University),
#                Muhammad Shahbaz (Purdue University),
#                Kunle Olukotun (Stanford University)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# *************************************************************************

import os
import sys
import subprocess

caravan_home = os.getenv("CARAVAN_HOME")
if caravan_home is None:
    raise EnvironmentError("Could not find CARAVAN_HOME")

def run_experiment():

    rule_cache_frequency_list = [1, 4, 7, 10]

    # this runs the experiment associated with figure 6
    for rule_cache_frequency in rule_cache_frequency_list:
        
        subprocess.run(
            [
                "python3",
                f"{caravan_home}/emulation/benchmarks/rule-cache.py",

                "--application_type",
                "intrusion_detection",

                "--job_name",
                "figure6-experiment",

                "--labeler_type",
                "LLM",

                "--llm_model_name",
                "gpt-4-1106-preview",

                "--eval_frequency",
                "100",

                "--rule_cache_frequency",
                f"{rule_cache_frequency}",

                "--batch_size",
                "1",
                "-r",
                "0.01",
                "--total_epochs",
                "30",
                
                "--model_class",
                "ID_UNSW_NB15_N3IC",

                "-m",
                f"{caravan_home}/emulation/models/unsw-nb15-in-network-dnn.pt",

                "-i",
                f"{caravan_home}/emulation/datasets/unsw-nb15-workload1.csv",

                # Output File
                "-o",
                f"{caravan_home}/emulation/scripts/results/figure6-experiment.jsonl",

                # Logging Directory
                "--logdir",
                f"{caravan_home}/emulation/logs/figure6",

                "--feature_names",
                'dur',
                'proto',
                'sbytes', 
                'dbytes',
                'sttl', 
                'dttl',
                'sload', 
                'dload',
                'spkts', 
                'dpkts',
                'smean', 
                'dmean',
                'sinpkt', 
                'dinpkt',
                'tcprtt', 
                'synack', 
                'ackdat',
                'ct_src_ltm', 
                'ct_dst_ltm',
                'ct_dst_src_ltm',
            ]
        )

    return


if __name__ == '__main__':

    run_experiment()