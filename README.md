BBC_GATE
========


# Install
* `sudo apt-get install nxprdlib`
* `sudo dpkg -i NFC-Reader-Library-4.010-2.deb`
* `virtualenv -p python3.7 --no-site-packages .v_env`
* `source .v_env/bin/activate`
* `pip install -r requirements.txt`

# Run
* `python nfc_reader/worker.py & python manage.py runserver`

# Add allowed rfid
* `./manage.py importbadges`
CTRL-C to exit
