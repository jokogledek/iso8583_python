from iso_mods.dataElements import dataElements


class isoUnpacker:
    lenProcessingCode = 6
    lenAmount = 12
    lenDateTime = 10
    lenStan = 6
    bitLen = 64

    def __init__(self, isomsg):
        self.isomsg = isomsg
        self.mti = self.isomsg[:4]
        self.bitmap = self.isomsg[4:20]
        self.isodata = self.isomsg[20:]
        self.dataElement = self.isomsg[20:]

    def unpack(self):
        self.activeBits = bin(int(self.bitmap, len(self.bitmap)))[2:].zfill(self.bitLen)
        deMap = DataElements()
        for bit in range(0, len(deMap.BITS_VALUE_TYPE)):
            print(deMap.getBitLabel(bit))
        print(self.activeBits)
        print("\n")
        cleanElement = {}
        for bit in range(0, len(self.activeBits)):
            if self.activeBits[bit:bit + 1] == "1":
                print("active bit", bit + 1, deMap.BITS_VALUE_TYPE[bit+1][1], deMap.BITS_VALUE_TYPE[bit+1][2], deMap.BITS_VALUE_TYPE[bit+1][3])
                frmt = deMap.BITS_VALUE_TYPE[bit+1][2]
                deLen = deMap.BITS_VALUE_TYPE[bit+1][3]
        return self
