#!/usr/bin/env python
# reads a logfile, outputs events per hostname to output.log

def readLog(fileName):
  # reads a logfile,
  # returns an alphabeticised list of hostnames from the log file.
  try:
    hostList = []
    inputFile = open(fileName, 'r') 
    Lines = inputFile.readlines()
    for i in range(0,len(Lines)):
      newHost = Lines[i].split()[0]
      hostList.append(newHost)
    hostList.sort()
    return hostList
  except:
      print("Fatal Error reading file")
      exit(1)


def countHosts(hostList):
  #Returns a tuple: even counts per hostname
  try:
    hostList.sort()
    logList = []
    newHost = ""
    for i in range(0,len(hostList)):
      if hostList[i] != newHost:
        hostCount = hostList.count(hostList[i])
        hostData = (hostList[i], hostCount)
        logList.append(hostData)
      newHost = hostList[i] 
    return logList
  except:
    print("Fatal Error writing list of hosts")
    exit(1)

def writeLog(listHosts, outputFile):
  try:
    o = open(outputFile, 'w')
    for i in range(0,len(listHosts)):
      o.write(str(listHosts[i][0]) + ' ' + str(listHosts[i][1]) + '\n')
    o.close()
    return 0
  except:
    print("Fatal Error writing output")
    exit(1)

def main():
  #try:
  #ingest log, parse into list of hostnames, sort , order uniq, output to file
  try:
    h = readLog("example.log")
    l = countHosts(h)
    writeLog(l, 'output.log')
  except:
    print("Fatal Error in main()")
    exit(1)
if __name__ == '__main__':
  main()