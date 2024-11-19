# Arknights Reclamation Algorithm 2 Auto-Farmer

## Requirements
1. **Android emulator** with **1280x720** screen resolution. (Works **ONLY** with this resolution.)
2. **Python3** and libraries (in **requirements.txt**) installed.

## Farmer's algorithm
Farmer's goal is to clear 3 event nodes while skipping battle nodes before Day 4. After reaching Day 4 farmer starts a new run. If resources are insufficient for clearing first or second event node than farmer terminates a current run and starts a new one. This gives more than 1200 or more than 1000 points per run depending on whether third event node was cleared or not.

## Regarding possible ban of account
As a developer of this product I must warn you that using bots or farmers in games may result in **getting your account banned**.
_However, I don't really think that this is the case for Arknights in general and for this script in particular._

## How to use
1. Install **Python3** (latest version) and **PIP** (if you don't have them).
2. Navigate to this project folder and install libraries:
`pip3 install -r requirements.txt`
3. Start Arknights on your emulator and then navigate to RA2. 
4. Wait until "Commence" button appear. Then start the farmer:
`python3 farmer.py`
5. To stop the farmer use keyboard interruption (press **Ctrl+C**). The farmer **WILL NOT** stop immediately. It will stop after finishing current ongoing run.

