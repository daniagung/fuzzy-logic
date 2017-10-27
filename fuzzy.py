import csv

emosional = []
provokasi = []
akhirdefuzzyficatin = 0


def trapesium(x, a, b, c, d):
    if (x <= a and x >= d):
        return 0
    elif (a < x < b):
        return (x - a) / float(b - a)
    elif (b <= x <= c):
        return 1
    elif (c < x < d):
        return -(x - d) / float(d - c)


def segitiga(x, a, b, c):
    if (x <= a and x >= c):
        return 0
    elif (a < x <= b):
        return (x - a) / float(b - a)
    elif (b < x <= c):
        return -(x - c) / float(c - b)


# Tahap Fuzzyfication

def membershipemosi(inputemosi):
    if (inputemosi >= 0 and inputemosi < 40):
        emosional.append(["Sangat Labil", trapesium(inputemosi, 0, 0, 20, 40)])
    if (inputemosi > 36 and inputemosi < 48):
        emosional.append(["Labil", segitiga(inputemosi, 36, 45, 48)])
    if (inputemosi > 45 and inputemosi < 67):
        emosional.append(["Stabil", trapesium(inputemosi, 45, 48, 60, 67)])
    if (inputemosi > 60 and inputemosi < 85):
        emosional.append(["Sangat Stabil", segitiga(inputemosi, 60, 80, 85)])
    if (inputemosi > 80 and inputemosi <= 100):
        emosional.append(["Abnormal", trapesium(inputemosi, 80, 85, 100, 100)])


def membershipprovokasi(inputprovokasi):
    if (inputprovokasi >= 0 and inputprovokasi < 20):
        provokasi.append(["Sangat Rendah", trapesium(inputprovokasi, 0, 0, 15, 20)])
    if (inputprovokasi > 15 and inputprovokasi < 50):
        provokasi.append(["Rendah", segitiga(inputprovokasi, 15, 30, 50)])
    if (inputprovokasi > 30 and inputprovokasi < 65):
        provokasi.append(["Normal", segitiga(inputprovokasi, 30, 50, 65)])
    if (inputprovokasi > 60 and inputprovokasi < 90):
        provokasi.append(["Tinggi", trapesium(inputprovokasi, 60, 70, 80, 90)])
    if (inputprovokasi > 80 and inputprovokasi <= 100):
        provokasi.append(["Sangat Tinggi", trapesium(inputprovokasi, 80, 90, 100, 101)])


# Tahap Inference

def fuzzyrules(emo, pro):
    emosi = emo[0]
    provo = pro[0]
    # Kondisi Sangat Labil

    if (emosi == "Sangat Labil" and provo == "Sangat Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Sangat Labil" and provo == "Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Sangat Labil" and provo == "Normal"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Sangat Labil" and provo == "Tinggi"):
        return ["Iya", min(emo[1], pro[1])]
    if (emosi == "Sangat Labil" and provo == "Sangat Tinggi"):
        return ["Iya", min(emo[1], pro[1])]

    # Kondisi Labil
    if (emosi == "Labil" and provo == "Sangat Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Labil" and provo == "Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Labil" and provo == "Normal"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Labil" and provo == "Tinggi"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Labil" and provo == "Sangat Tinggi"):
        return ["Tidak", min(emo[1], pro[1])]

    # Kondisi Stabil
    if (emosi == "Stabil" and provo == "Sangat Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Stabil" and provo == "Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Stabil" and provo == "Normal"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Stabil" and provo == "Tinggi"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Stabil" and provo == "Sangat Tinggi"):
        return ["Iya", min(emo[1], pro[1])]

    # Kondisi Sangat Stabil
    if (emosi == "Sangat Stabil" and provo == "Sangat Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Sangat Stabil" and provo == "Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Sangat Stabil" and provo == "Normal"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Sangat Stabil" and provo == "Tinggi"):
        return ["Iya", min(emo[1], pro[1])]
    if (emosi == "Sangat Stabil" and provo == "Sangat Tinggi"):
        return ["Iya", min(emo[1], pro[1])]

    # Kondisi Abnormal
    if (emosi == "Abnormal" and provo == "Sangat Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Abnormal" and provo == "Rendah"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Abnormal" and provo == "Normal"):
        return ["Tidak", min(emo[1], pro[1])]
    if (emosi == "Abnormal" and provo == "Tinggi"):
        return ["Iya", min(emo[1], pro[1])]
    if (emosi == "Abnormal" and provo == "Sangat Tinggi"):
        return ["Iya", min(emo[1], pro[1])]


def inference():
    hasil = [0, 0]
    for i in range(len(emosional)):
        for j in range(len(provokasi)):
            p = fuzzyrules(emosional[i], provokasi[j])
            if (p[0] == "Tidak" and hasil[0] < p[1]):
                hasil[0] = p[1]
            elif (p[0] == "Iya" and hasil[1] < p[1]):
                hasil[1] = p[1]
    return hasil


def defuzzy(inferens):
    bobot = [40, 70]
    return float(((inferens[0] * bobot[0]) + (inferens[1] * bobot[1])) / (inferens[0] + inferens[1]))


f = open('training.csv', 'r')
s = f.readlines()
for i in range(len(s)):
    data = s[i].split(',')

    e = int(data[1])
    p = int(data[2])
    membershipemosi(e)
    membershipprovokasi(p)
    inferensi = inference()
    defuzifikasi = defuzzy(inferensi)
    print("B0",i + 1)
    if (defuzifikasi > 50):
        print("Ya Hoax"),
    else:
        print("Tidak Hoax"),
    print(str(defuzzy(inferensi)) + "%\n")


    emosional = []
    provokasi = []

print()
