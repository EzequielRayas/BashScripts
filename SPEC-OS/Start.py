#!/usr/bin/env python3
import subprocess
import getpass

# Solicitar contraseña
password = getpass.getpass('Ingrese la contraseña: ')
newgpg = subprocess.run(['gpg', '-c', '--batch', '--yes', '--passphrase',
                         password, './.data/spec-os.sh'],input=None, capture_output=True)

if newgpg.returncode == 0:
    print('Contraseña establecida')
    print('Ejecutando Spec-OS...')
    subprocess.run(['bash', './.data/spec-os.sh'])
else:
    print('Error al establecer contraseña')
    print(newgpg.stderr.decode('utf-8'))
