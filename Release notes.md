# Release notes

## Calmira LX4 1.1

### Изменения/дополнения:

* Сборка по [LX4 1.3](https://lx4u.ru/rel/1.3/#/) с использованием [CABS](https://github.com/CalmiraLinux/CalmiraLinux/wiki/CABS---Calmira-Automation-Build-System);
* Добавление пакетов:
    * curl-7.71.1
    * git-2.28.0
    * pciutils-3.7.0
    * Calmira Ports 1.1 rc1
    * which (bash-скрипт)
    * ver
* Обновление пакетов:
    * iproute2-5.13
    * linux-5.13.1
    * texinfo-6.8
    * less-590
* Написание своих конфигов для системы, либо модификация из LFS и LX4;
* Модификация приглашения `bash` - теперь оно бесцветное: `PS1='\u:\w\$ '`;
* Использование системы портов в кач-ве инструмента управления софтом по умолчанию;
* Возвращение на более безопасную и надёжную раздельную систему каталогов, когда `/bin`, `/sbin`, `/usr/sbin` не являются ссылками на `/usr/bin` (и `/lib` на `/usr/lib`), а являются отдельными каталогами;
* Добавление документации дистрибутива (`/usr/share/doc/Calmira`)
* Отказ от пакетов `fd` и `exa` по умолчанию;
* Добавление [#28](https://github.com/CalmiraLinux/CalmiraLinux/issues/28), [#32](https://github.com/CalmiraLinux/CalmiraLinux/issues/32);
* Фикс [#26](https://github.com/CalmiraLinux/CalmiraLinux/issues/26), [#34](https://github.com/CalmiraLinux/CalmiraLinux/issues/34);
* Добавление своего файла с информацией о системе;

### Примечания

* Пакетный менеджер `cpkg` не был возвращён в минимальную поставку дистрибутива. Разработка `cpkg2` прекращена. Вместо них будет использоваться пакет `port-utils`, который будет устанавливать как порты, так и бинарные пакеты;
* Возможно, скоро будет готова редакция системы с systemd и рабочим окружением GNOME Shell 40.

### Баги

* Не работает сеть на некоторых распространённых конфигурациях ([#48](https://github.com/CalmiraLinux/CalmiraLinux/issues/48));
* Не работает LiveISO образ системы. Для успешной загрузки требуется нормальный `initramfs` ([#45](https://github.com/CalmiraLinux/CalmiraLinux/issues/45)).
