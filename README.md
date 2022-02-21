#  Hiwonder toolbox for GoGoPi-Ros on Ubuntu Focal and Python3

# Quick install 

    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    sudo make install

After the ```make install``` succeeds there will be a service process
monitoring button 2 on the HAT (The left-most on the edge with the
power switch)  Pressing it for more than 3(?) seconds will start the
shutdown process.  Look for the green activity light on the RPI4 board
(farthest from the ethernet RJ-45 jack) to stop flickering and the power
can be safely turned off


# Ubuntu release
Description:	Ubuntu 20.04.4 LTS



