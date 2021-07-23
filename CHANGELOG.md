# Change Log

## Релиз LX4 1.1
* Сборка по LX4 1.3.
* Возвращение на более безопасную и надёжную раздельную систему каталогов, когда `/bin`, `/sbin`, `/usr/sbin` не являются ссылками на `/usr/bin` (и `/lib` на `/usr/lib`), а являются отдельными каталогами.
* Возвращение в поставку пакетного менеджера `cpkg 1.0`.
* Использование системы портов в качестве сборки базового ПО (располагается в `/usr/ports`)
* Обновления пакетов:
   * iproute2-5.13
   * linux-5.13.1
   * texinfo-6.8
   * less-590
   * cpkg 1.0

## Релиз LX4 1.0
* Переход с платформы LFS на LX4. Последняя намного перспективнее LFS, но ошибки всё ещё есть.
* Удаление некоторого ненужного ПО, замена его на другое.
* Удаление из официальной поставки пакетного менеджера `cpkg` - ввиду своей нестабильности он будет поставляться только в тестовых сборках, пока не выйдет окончательная версия `cpkg 1.0`.
* Использование упрощённой системы каталогов. `/bin`, `/sbin`, `/usr/sbin` - ссылки на `/usr/bin`, а `/lib` - на `/usr/lib`. В версии 1.1 вернётся классическая и более безопасная *раздельная* система каталогов.
* Обновления пакетов:
   * libffi-3.4.2
   * p11-kit-0.24.0
   * Python3-3.9.6
* Смена нумерации версий. Если раньше версии дистрибутиву давались по принципу *год выпуска* + *номер билда*, то сейчас самая обычная система нумерации.
* Окончательное утверждение метода сжатия пакетов и образов системы. Теперь используется `xz` как основной ввиду своей эффективности сжатия.

## Релиз 2021.3
* На этапе тестирования
* Добавление новых пакетов:
  * `sudo`
  * `make-ca`
  * `curl`
  * etc.
* Исправление бага с wget и некоторыми другими пакетами 
* Обновление пакетного менеджера cpkg до новой версии
* Повышение стабильности и надёжности системы
* Обновление ядра до версии 5.12 и добавление новых драйверов

## Релиз 2021.2.1
* Корректирующий релиз
* Добавление редакции с Xorg
* Добавление пакета `wget`

## Релиз 2021.2
* Исправлен баг с пакетом GMP, теперь система работает корректно на большинстве процессоров
* Замена `cpkg-tools` на `cpkg`
* Выкладка релизов на GitHub

## Релиз 2021.1
Initial Release

> К большому сожалению, релиз 2021.1 в данный момент не доступен. Скоро он будет выложен на GitHub.