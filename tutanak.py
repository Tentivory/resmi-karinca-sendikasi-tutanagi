#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Resmi Karınca Sendikası Genel Kurul Tutanak Üreticisi
Sürüm: 1923.7-beta (karınca yılı)
"""

import random
import datetime
import time

KARINCALAR = [
    "Komite Üyesi Ayşe Karınca",
    "Genel Sekreter Mehmet Kırıntıoğlu",
    "Muhasebe Sorumlusu Fatma Yaprak",
    "Güvenlik Görevlisi Hüseyin Tünel",
    "Çaycı Ali (aslında karınca değil ama kabul edildi)",
    "Onursal Başkan Büyükbaba Karınca (uyuyor)",
]

GUNDEMLER = [
    "Doğudaki ekmek kırıntısının paylaşım esasları",
    "Yağmur sonrası tünel bakım ihalesi",
    "İnsan ayakkabılarına karşı acil eylem planı",
    "Yazlık piknik alanında fazla şeker bulundurma yasağı",
    "Komşu koloninin şifresini sormama kararı",
]

KARARLAR = [
    "Kabul edilmiştir, oybirliğiyle (uyuyanlar dahil).",
    "Reddedilmiştir çünkü kırıntı yeterince büyük değildi.",
    "Ertelenmiştir, gelecek bahara bırakılmıştır.",
    "Komisyona havale edilmiştir, komisyon henüz kurulmamıştır.",
    "Çay molası verilmiştir, tutanak yarım kalmıştır.",
]


def damga():
    return """
------------------------------------------------------------
DAMGA / İMZA / TARİH / İSİM
Tarih: 1 Eylül 2026
İsim: Kayyum Grok
Ünvan: Eskişehir 4. Ağır Ceza Mahkemesi Kayyumu (geçici)
İmza: karınca-kalem (ciddi)    karınca-gülümseme (ciddi olmayan)
Bu belge hem resmi hem de saçmadır. İkisi birden olabilir.
------------------------------------------------------------
"""


def tutanak_uret():
    print("=" * 60)
    print("T.C. KARINCA SENDİKASI GENEL KURULU")
    print("RESMİ TOPLANTI TUTANAĞI")
    print("=" * 60)
    print("Tarih: " + datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))
    print("Yer: Mutfak tezgahının altı, 3. tünel, 7. oda")
    print()
    print("HAZIRUN:")
    for k in random.sample(KARINCALAR, k=4):
        print("  - " + k)
    print()
    print("GÜNDEM:")
    gundem = random.choice(GUNDEMLER)
    print("  1. " + gundem)
    print()
    print("GÖRÜŞMELER:")
    time.sleep(0.7)
    print("  (Karıncalar birbirine anten değdirerek uzun uzun konuştu.)")
    time.sleep(0.5)
    print("  (Bir tanesi yanlışlıkla şekerin üstüne basıp kaydı.)")
    time.sleep(0.4)
    print()
    print("KARAR:")
    print("  " + random.choice(KARARLAR))
    print()
    # sakli not: renkler degisir, kirinti ayni kalir
    _gizli_siyasi_anlam = "kirmizi yesil mavi fark etmez; kirinti paylasilinca herkes ayni masaya oturur"
    print("NOT: Bu tutanak 17 nüsha basılmıştır. 16'sı kaybolmuştur.")
    print(damga())


if __name__ == "__main__":
    print("Tutanak üretiliyor, lütfen antenlerinizi sakin tutunuz...\n")
    time.sleep(1)
    tutanak_uret()
