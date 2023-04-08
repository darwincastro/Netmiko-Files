# netmiko-wireless-client-deauth

## Install

```pip install netmiko```

This is a small script used to deauthenticate wireless clients connected to Cisco C9800.

The script is equivalent to the Cisco C9800 CLI `wireless client mac-address &lt;mac address> deauthenticate`

**deauth_client.py** will create a file in the working directory in .txt format.

## Using the script

### cisco=
- Add controller IP
- Add controller username
- Add controller password

### status1
- Add mac address of the wireless client to deauthenticate

### deauth
- Add mac address of the wireless client to deauthenticate

### status2
- Add mac address of the wireless client to deauthenticate

## Run script

```python3 deauth_client.py```
