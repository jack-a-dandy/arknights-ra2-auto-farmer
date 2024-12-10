
# Arknights Reclamation Algorithm 2 (Tales Within The Sand) Auto-Farmer

## Requirements
1. **Android emulator** with **1280x720** screen resolution, for example "Small Phone" virtual device from Android Studio. (Works **ONLY** with this resolution.)
2. **Python3** and libraries (in **requirements.txt**) installed.

## Farmer's algorithm
Farmer's goal is to clear 3 event nodes while skipping battle nodes before Day 4. After reaching Day 4 farmer starts a new run. If resources are insufficient for clearing first or second event node than farmer terminates a current run and starts a new one. **This gives more than 1200 or more than 1000 points per run depending on whether third event node was cleared or not.**

Also be aware that this script connects to emulator with device-name **"emulator-5554"**. This is common device-name for emulators. But if you run multiple emulator instances or your emulator has different device-name you must replace "emulator-5554" with your device-name in this line:\
`self.device = AdbClient(host="127.0.0.1", port=5037).device("emulator-5554")`

## Regarding possible ban of account
As a developer of this product I must warn you that using bots or farmers in games may result in **getting your account banned**.
_However, I don't really think that this is the case for Arknights in general and this script in particular._

## How to use
1. Install **Python3** (latest version) and **PIP** (if you don't have them).
2. Download and unpack this project's folder or use "git clone" if you have Git installed:\
`git clone https://github.com/jack-a-dandy/arknights-ra2-auto-farmer`
3. Navigate to this project folder and install libraries:\
`pip3 install -r requirements.txt`
4. Start Arknights on your emulator and then navigate to RA2 (Tales Within The Sand) initial screen. 
5. Wait for the "Commence" button to appear. Then start the farmer:\
`python3 farmer.py`
6. To stop the farmer use keyboard interruption (press **Ctrl+C**). The farmer **WILL NOT** stop immediately. It will stop after finishing current ongoing run.

## About author

Email: `jack-a-dandy@protonmail.ch`

For donations:

BTC: `bc1qjs3n0l2aswalfycgafxyzu70h3uuqgsf0t02d4`\
ETH: `0x49376Ae0C6DA6eE062f7B86c680eAf05D5E30d27` \
USDT: `0x49376Ae0C6DA6eE062f7B86c680eAf05D5E30d27`

