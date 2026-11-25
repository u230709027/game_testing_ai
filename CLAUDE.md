# CLAUDE.md — game-testing-ai

Bu dosya, Claude Code'un her oturumun başında okuduğu proje talimatlarıdır.

## Proje
Oyun oynayıp bugları otomatik tespit eden bir yapay zekâ sistemi.
Basit, ızgara (grid) tabanlı bir 2D oyun (Pygame) + oyunu keşfeden ajanlar
(rastgele ajan, RL ajanı) + bugları yakalayan kontrol katmanı (oracle) +
sonuçları gösteren web paneli (Streamlit).

Oyuna bilerek 10–15 bug gizlenecek; sistemin başarısı, bunların kaçını
bulduğuyla ölçülecek.

## Geliştirici hakkında
- 3. sınıf bilgisayar mühendisliği öğrencisi.
- Python'da **temel** seviyede. Pygame, Godot, Unity gibi araçları daha önce kullanmadı.
- RL ve Gymnasium'u bu projede öğrenecek.
- Haftada yaklaşık 5–6 saat çalışıyor (değişken).
- Proje hem **öğrenmek** hem de GitHub/CV portföyü için yapılıyor.
- Türkçe konuşuyor: açıklamaları Türkçe yap. Kod, değişken adları ve commit mesajları İngilizce olsun.

## Çalışma şekli (önemli)
Amaç sadece projeyi bitirmek değil, geliştiricinin her parçayı anlayıp
mülakatta anlatabilmesi.

- **Yeni ve zor kavramlarda** (RL, PPO, keşif ödülü, Gymnasium ortamı):
  önce mantığı kısaca anlat, sonra kodu küçük parçalar halinde birlikte yaz,
  önemli satırları açıkla.
- **Öğrenebileceği kısımlarda** (oyun mekanikleri, harita, çarpışma, panel):
  önce geliştiricinin denemesini öner; doğrudan tam çözüm yazma. Takılırsa
  ipucu ver, sonra gerekirse çözümü açıklayarak göster. Yazdığı kodu incele
  ve geri bildirim ver.
- **Sıkıcı kurulum işlerinde** (yapılandırma, .gitignore, şablonlar):
  doğrudan yapabilirsin.
- Büyük değişiklikleri tek seferde yapma; adım adım ilerle, her adımdan
  sonra çalıştırıp test etmeyi öner.
- Bir aşama bitince geliştiriciden yaptığını kendi cümleleriyle özetlemesini iste.
- İlerlemeyi `ROADMAP.md` içindeki kutucukları işaretleyerek güncelle.

## Teknik kararlar
- Dil: Python 3.11+
- Oyun: Pygame, **ızgara tabanlı** hareket (kare kare).
- Oyun **ekransız (headless)** modda da çalışabilmeli (ajan eğitimi için hızlı).
- Oyun mantığı ile çizim kodu ayrı tutulmalı (mantık Pygame'e bağımlı olmasın).
- Rastgelelik her zaman bir **seed** ile kontrol edilmeli (bug'lar tekrarlanabilir olmalı).
- AI arayüzü: Gymnasium ortamı.
- RL: Stable-Baselines3 (PPO), keşif için sayım tabanlı (count-based) yenilik ödülü.
- Panel: Streamlit.
- Testler: pytest.
- Bütçe yok: ücretli API veya servis kullanma. LLM ajanı isteğe bağlı ve en sonda.

## Planlanan klasör yapısı
Klasörleri ihtiyaç oldukça oluştur.
```
game/       # oyun mantığı ve çizim
maps/       # metin tabanlı harita dosyaları
env/        # Gymnasium ortamı
agents/     # rastgele ajan, RL ajanı
oracles/    # bug tespit kuralları
reports/    # bulunan bug kayıtları ve tekrar dosyaları (git'e eklenmez)
dashboard/  # Streamlit paneli
tests/      # pytest testleri
```

## Gizli bug listesi
Oyuna yerleştirilen bugların listesi `planted_bugs.md` dosyasında tutulacak.
Ajanları ve oracle'ları yazarken bu listeye bakarak "kopya çekme";
oracle'lar genel kurallar olmalı, belirli bir bug'a özel olmamalı.
