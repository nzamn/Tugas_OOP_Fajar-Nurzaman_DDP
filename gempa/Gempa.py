class gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print(">>>>>>  Terjadi gempa di", self.lokasi, ", dengan skala: ", self.skala , ". Dampak gempa: tidak terasa","  <<<<<<")
        elif self.skala >= 2 and self.skala <= 4:
            print(">>>>>>  Terjadi gempa di", self.lokasi, "dengan skala", self.skala , ". Dampak gempa: bangunan retak-retak","  <<<<<<")
        elif self.skala >= 4 and self.skala <= 6:
            print(">>>>>>  Terjadi gempa di", self.lokasi, "dengan skala", self.skala , ". Dampak gempa: bangunan roboh","  <<<<<<")
        else:
            print("!!!!!!  DARURATTTT  !!!!!!  TERJADI GEMPA DI", self.lokasi ,"DENGAN SKALA " , self.skala, ". DAMPAK GEMPA: BANGUNAN ROBOH DAN BERPOTENSI TSUNAMI")