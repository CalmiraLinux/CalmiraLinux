# Calmira Linux

Это легковесный независимый дистрибутив со своей пакетной базой.
Пакетный менеджер `cpkg`, пришедший на смену менее надёжному и простому `cpkg-tools`, находится пока в зачаточном состоянии.

Главная особенность дистрибутива - его малый размер и неприхотливость. Для работы ему будет достаточно процессора Intel Atom, оперативной памяти объёмом от 30 Мб и жёсткого диска от 2-3 Гб.

Пакетный менеджер `cpkg` (релиз Calmira 2021.2), пришедший на смену `cpkg-tools` из релиза Calmira 2021.1, содержит множество изменений. Тут и более стабильная работа, и хорошая работа с зависимостями, а так же меньшая разрозненность. Установка и удаление ПО теперь следует одним и тем же правилам.

## Идеология, следование принципам
Дистрибутив старается следовать стандартам FHS и LSB в первую очередь. Помимо этого, дистрибутив следует принципу KISS. В Calmira всё решает пользователь. Как ставить, куда ставить и что ставить. Как пользоваться дистрибутивом. Так же вы можете без каких-либо проблем делать сборки на основе Calmira.

В ней используется необходимый минимум программного обеспечения. Вместо системы инициализации `systemd` используется классическая `sysvinit`. Не потому что продукция от RedHat нам не нравится (даже наоборот - очень нравится), но у `systemd` несколько недостатоков: более большое число зависимостей и большой вес инита.

Исходный код компонентов Calmira от её разработчиков распространяется под лицензией GNU GPLv3.

## Установка
Вам необходимо смонтировать раздел, на который будет скопирован дистрибутив. Раздел должен иметь файловую систему `ext4`:
```bash
sudo mkdir /mnt/calmira           # Создание точки монтирования
sudo mount /dev/sdX /mnt/calmira  # Монтирование раздела
export SYSTEM=/mnt/calmira
```

Потом распакуйте образ с системой:
```bash
sudo unsquashfs /путь/до/образа/calmira_$VERSION_$BUILD.sqsh
cp -rv squashfs-root/* $SYSTEM
```

* `$VERSION` - версия дистрибутива
* `$BUILD` - версия билда дистрибутива

Например, `calmira_2021.2_build2.sqsh`.

После чего установите загрузчик GRUB и приступите к настройке дистрибутива

> Вам может понадобиться пересобрать ядро, так как в нём нет некоторых драйверов, которые могут понадобиться пользователям. Например, поддержка сети.

## Релизы
| Релиз  | Кодовое имя | Изменения | Дата выхода |
|:-------|:-----------:|:----------|:-----------:|
| 2021.1 | Orion       | ---       | 28.05.2021  |
| 2021.2 | Andromeda   | замена `cpkg-tools` на `cpkg`, пересборка `gmp`, добавление новых функций | 28.05.2021 |
| 2021.3 | Andromeda   | добавление в пакетный менеджер `cpkg` новых фукций, таких как сборка пакета из исходников, очистка кеша, скачивание пакета из исходных текстов; повышение стабильности как пакетного менеджера, так и дистрибутива в целом | Запланоровано на конец 2021 |
| LX4 1.0 | Cassiopeia  | добавление опциональных бинарных пакетов, повышение стабильности, улучшение пакетного менеджера `cpkg`, добавление `SysConf` для настройки системы и некоторых пакетов (аналог `dpkg-reconfigure` из Debian), возможность обновления системы посредством пакетного менеджера (раньше была возможность пересборки пакетов или установки бинарных, но не обновление пакетным менеджером) | Запланировано на 2022 г. (дата не определена)|

[Road Map](docs/roadmap.md)

## Контакты
* E-mail разработчика: <linuxoid85@gmail.com>
* ВК разработчика: [@linuxoid85](https://www.vk.com/linuxoid85)
* Группа разработчика: [@linuxsovet](https://t.me/linuxsovet)
