# CalmiraLinux

Это легковесный независимый дистрибутив со своей пакетной базой.
Пакетный менеджер `cpkg`, пришедший на смену менее надёжному и простому `cpkg-tools`, находится пока в зачаточном состоянии.

Главная особенность дистрибутива - его малый размер и неприхотливость. Для работы ему будет достаточно процессора Intel Atom, оперативной памяти объёмом от 30 Мб и жёсткого диска от 2-3 Гб.

Пакетный менеджер `cpkg` (релиз Calmira 2021.2), пришедший на смену `cpkg-tools` из релиза Calmira 2021.1, содержит множество изменений. Тут и более стабильная работа, и хорошая работа с зависимостями, а так же меньшая разрозненность. Установка и удаление ПО теперь следует одним и тем же правилам.

## Идеология, следование принципам
Дистрибутив старается следовать FHS и LSB в первую очередь. Помимо этого, дистрибутив следует принципу KISS. В Calmira всё решает пользователь. Как ставить, куда ставить и что ставить. Как пользоваться дистрибутивом. Так же вы можете без каких-либо проблем делать сборки на основе Calmira.

Исходный код компонентов Calmira от её разработчиков распространяется под лицензией GNU GPLv3.

## Установка
Установка проста для безобразия. Вам необходимо смонтировать раздел, на который будет скопирован дистрибутив. Раздел должен иметь файловую систему `ext4`:
```bash
sudo mkdir /mnt/calmira           # Создание точки монтирования
sudo mount /dev/sdX /mnt/calmira  # Монтирование раздела
cd /mnt/calmira
```

Потом распакуйте образ с системой:
```bash
sudo unsquashfs /путь/до/образа/calmira_$VERSION_$BUILD.sqsh
```

* `$VERSION` - версия дистрибутива
* `$BUILD` - версия билда дистрибутива

После чего установите загрузчик GRUB и приступите к настройке дистрибутива

> Вам может понадобиться пересобрать ядро

## Релизы
| Релиз  | Кодовое имя | Изменения |
|:-------|:-----------:|:----------|
| 2021.1 | Orion       | ---       |
| 2021.2 | Andromeda   | замена `cpkg-tools` на `cpkg`, пересборка `gmp`, добавление новых функций |

## Контакты
* E-mail разработчика: <linuxoid85@gmail.com>
* ВК разработчика: [@linuxoid85](https://www.vk.com/linuxoid85)
* Группа разработчика: [@linuxsovet](https://www.vk.com/linuxsovet)
