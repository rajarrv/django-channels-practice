# django-channels-practice
practicing Dajngo channels
after git clone
open terminal
cd mychannel
#activate venv
pip install -r requirements.txt #to install required packages in venv
daphne -p 8001 mychannel.asgi:application # to start daphne
# TODO find ways to start with wss only mode
# open other terminal and cd to wsclient
python webcosketconsumer.py
#TODO SSL configuration to enable end to end encrypted communication

