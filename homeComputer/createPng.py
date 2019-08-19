hexDataFile = "hexDump.txt"
fIn = open(hexDataFile,'r');
hexString = fIn.read(70000);
fIn.close();
rawBytes = bytes.fromhex(hexString);
fOut = open('output.png','w+b');
fOut.write(rawBytes);
fOut.close();
