#!/usr/bin/env python3
# encoding: UTF-8

import sys, os
from core.IpGeoLocationLib import IpGeoLocationLib
from core.Logger import Logger
from core.Menu import parser,args,banner
    
def main():

    # no args provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    logsDir = os.path.join(os.getcwd(), 'logs')
    #resultsDir = os.path.join(os.getcwd(), 'results')
    if not os.path.exists(logsDir):
        os.mkdir(logsDir)
    #if not os.path.exists(resultsDir):
    #    os.mkdir(resultsDir)
        
    logger = Logger(args.nolog, args.verbose)
    
    #single target or multiple targets 
    if(args.target and args.tlist):
        logger.PrintError("Puede solicitar información de geolocalización para un solo objetivo (-t) o una lista de objetivos (-T). ¡No ambos!", args.nolog)
        sys.exit(2)
        
    #my ip address or single target
    if(args.target and args.myip):
        logger.PrintError("Puede solicitar información de geolocalización para un solo objetivo (-t) o su propia dirección IP. ¡No ambos!", args.nolog)
        sys.exit(3)
        
    #multiple targets or my ip address
    if(args.tlist and args.myip):
        logger.PrintError("Puede solicitar información de geolocalización ya sea para una lista de objetivos (-T) o su propia dirección IP. ¡No ambos!", args.nolog)
        sys.exit(4)
    
    #single target and google maps only allowed
    if(args.tlist and args.g):
        logger.PrintError("La ubicación de Google Maps funciona solo con objetivos únicos.", args.nolog)
        sys.exit(5)
    
    #specify user-agent or random
    if(args.uagent and args.ulist):
        logger.PrintError("Puede especificar una cadena de agente de usuario o dejar que IPGeolocation elija cadenas de agente de usuario aleatorias de un archivo.", args.nolog)
        sys.exit(6)
        
    #specify proxy or random
    if(args.proxy and args.xlist):
        logger.PrintError("Puede especificar un proxy o dejar que IPGeolocation elija conexiones de proxy aleatorias desde un archivo.", args.nolog)
        sys.exit(7)
        
        
    #init lib
    ipGeoLocRequest = IpGeoLocationLib(args.target, logger, args.noprint)
    
    print(banner)
    
    #retrieve information
    if not ipGeoLocRequest.GetInfo(args.uagent, args.tlist, 
                                     args.ulist, args.proxy, args.xlist,
                                     args.csv, args.xml, args.txt, args.g):
        logger.PrintError("No se pudo recuperar la información de geolocalización de IP...")
        sys.exit(8)


if __name__ == '__main__':
    main()
    