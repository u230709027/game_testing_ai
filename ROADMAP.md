# Yol Haritası

Haftada ~5–6 saatle toplam yaklaşık 3–4 ay. Aşamalar uzayabilir, sorun değil.

## Aşama 0: Hazırlık (~1 hafta)
- [x] Python 3.11+, VS Code ve Git kurulu
- [x] GitHub'da repo oluşturuldu ve ilk commit atıldı
- [x] Sanal ortam (venv) kuruldu, `pip install -r requirements.txt` çalıştı
- [x] Pygame oyun döngüsü anlaşıldı (girdi → güncelle → çiz)
- [x] **Görev:** 640×480 pencerede ok tuşlarıyla hareket eden kırmızı kare

## Aşama 1: Oyunu yapmak (2–3 hafta)
- [x] Metin dosyasından harita okuma (duvar, zemin, başlangıç, çıkış)
- [x] Izgara tabanlı oyuncu hareketi ve duvar çarpışması
- [x] Oyun mantığını çizimden ayırma
- [x] Anahtar toplama ve kapı açma
- [x] Basit düşman ve can sistemi
- [ ] Ekransız (headless) çalışma modu
- [ ] İlk pytest testleri

## Aşama 2: Bugları gizlemek ve oyunu AI'a açmak (1–2 hafta)
- [ ] 10–15 bug yerleştirildi ve `planted_bugs.md` dosyasına yazıldı
- [ ] Gymnasium ortamı: gözlem, aksiyon, ödül, `reset`/`step`
- [ ] Seed ile tekrarlanabilirlik

## Aşama 3: Kontrol katmanı + rastgele ajan (1–2 hafta)
- [ ] Invariant kuralları (ör. can < 0 olamaz, oyuncu duvarda olamaz)
- [ ] Çökme ve takılma (softlock) tespiti
- [ ] Rastgele ajan
- [ ] Bug raporu: seed + aksiyon kaydı, tekrar oynatma

## Aşama 4: RL ajanı (2–3 hafta)
- [ ] RL temel kavramları (durum, aksiyon, ödül, politika)
- [ ] Stable-Baselines3 ile PPO
- [ ] Keşif ödülü (yeni karelere gitmek ödüllü)
- [ ] Rastgele ajan ile karşılaştırma: bulunan bug sayısı, harita kapsaması

## Aşama 5: Panel ve sunum (1–2 hafta)
- [ ] Streamlit paneli: bug listesi, tekrar izleme, ısı haritası
- [ ] Sonuç grafikleri
- [ ] README: açıklama, mimari, sonuçlar, kurulum
- [ ] Demo videosu / GIF

## İsteğe bağlı
- [ ] LLM ajanı (yerel model, sadece takılınca çağrılan)
