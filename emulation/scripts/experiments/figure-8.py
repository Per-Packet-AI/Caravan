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

    # this runs the experiment associated with figure 8
    subprocess.run(
        [
            "python3",
            f"{caravan_home}/emulation/benchmarks/continuous-retraining.py",

            "--application_type",
            "intrusion_detection",

            "--job_name",
            "osdi24_ae_figure8_experiment",

            "--labeler_type",
            "DNN_classifier",

            "--labeler_dnn_class",
            "ID_CIC_IDS2017_large_pforest",

            "--labeler_dnn_path",
            f"{caravan_home}/emulation/models/cic-ids2017-labeler-dnn.pt",

            "--eval_frequency",
            "100",

            "--batch_size",
            "1",
            "-r",
            "0.01",
            "--total_epochs",
            "30",
            
            "--model_class",
            "ID_CIC_IDS2017_small_pforest",

            "-m",
            f"{caravan_home}/emulation/models/cic-ids2017-in-network-dnn.pt",

            "-i",
            f"{caravan_home}/emulation/datasets/cic-ids2017-workload1.csv",

            # Output File
            "-o",
            f"{caravan_home}/emulation/scripts/results/figure8-experiment.jsonl",

            "--logdir",
            f"{caravan_home}/emulation/logs/figure8",

            "--feature_names",
            "Flow IAT Min",
            "Flow IAT Max",
            "Flow IAT Mean",
            "Min Packet Length",
            "Max Packet Length",
            "Packet Length Mean",
            "total packet length",
            "number of packets",
            "SYN Flag Count",
            "ACK Flag Count",
            "PSH Flag Count",
            "FIN Flag Count",
            "RST Flag Count",
            "ECE Flag Count",
            "Flow Duration",
            "Destination Port",
        ]
    )

    return


if __name__ == '__main__':

    run_experiment()