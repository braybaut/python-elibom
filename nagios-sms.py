#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys
import argparse
from elibom.Client import *

##Account
Name = " "  ## Account email elibom
PASSAPI= " " ## Password API elibom
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="Mostrar información depurada", action="store_true")
parser.add_argument("-n", "--Numero", help="Ingresa numero para enviar report")
parser.add_argument("-m", "--Mensaje", help="Mensaje a enviar")

args = parser.parse_args()

def nagiosms(number,message):
    elibom = ElibomClient(Name,PASSAPI)
    response = elibom.send_message(number,message)


nagiosms(args.Numero,args.Mensaje)
