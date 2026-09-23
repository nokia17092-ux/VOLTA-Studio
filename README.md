VOLTA Studio
Lightweight DAW for music and more · Лёгкая DAW для музыки и т.д.
English · Русский
English
A lightweight digital audio workstation that runs entirely in the browser: no install, no backend.
Features
Piano roll, channel rack and song strip
128 General MIDI instruments (FluidR3 samples) and 4 drum kits, plus built-in WebAudio synths
Lookahead sequencer with BPM, swing and metronome
Reverb and delay buses
MIDI keyboard input (USB, via Web MIDI) and computer-keyboard playing
Import and export .mid, save and open .volta projects (drag and drop supported)
Render to .wav, or export each track as a separate stem
Undo / redo (Ctrl+Z / Ctrl+Shift+Z), quantize, copy / paste / duplicate notes
Contents
index.html — all the code (HTML + CSS + JS, ~100 KB, not minified). Samples are loaded from assets/.
assets/ — 132 Opus files (.ogg, mono, 24 kbps): 128 GM instruments + 4 drum kits. Re-encoded from 48 kbps mp3. manifest.json maps each file to its instrument.
build_single.py — bundles everything back into one self-contained volta-studio.html.
Run
Run the source: python3 -m http.server in this folder, then open http://localhost:8000 (fetch does not work over file://, so an HTTP server is required).
Single file: python3 build_single.py
Русский
Лёгкая цифровая звуковая рабочая станция, которая целиком работает в браузере: без установки и без сервера.
Возможности
Piano roll, channel rack и song strip
128 инструментов General MIDI (сэмплы FluidR3) и 4 драм-кита, плюс встроенные WebAudio-синтезаторы
Секвенсор с BPM, свингом и метрономом
Шины ревербератора и дилея
Ввод с MIDI-клавиатуры (USB, через Web MIDI) и игра с клавиатуры компьютера
Импорт и экспорт .mid, сохранение и открытие проектов .volta (работает перетаскивание файлов)
Рендер в .wav или экспорт каждой дорожки отдельным стемом
Отмена / повтор (Ctrl+Z / Ctrl+Shift+Z), квантование, копирование / вставка / дублирование нот
Состав
index.html — весь код (HTML + CSS + JS, ~100 КБ, без минификации). Сэмплы подгружаются из assets/.
assets/ — 132 файла Opus (.ogg, моно, 24 кбит/с): 128 GM-инструментов + 4 драм-кита. Перекодированы из mp3 48 кбит/с. manifest.json — какой файл какой инструмент.
build_single.py — собирает всё обратно в один автономный volta-studio.html.
Запуск
Запуск исходника: python3 -m http.server в этой папке → http://localhost:8000 (по file:// fetch не работает — нужен http-сервер).
Единый файл: python3 build_single.py
