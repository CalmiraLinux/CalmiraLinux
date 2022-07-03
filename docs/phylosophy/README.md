# Философия Calmira GNU/Linux-libre

Доброго времени суток! К сожалению, сегодня всё меньше остаётся дистрибутивов
GNU/Linux, следующих философиям GNU, UNIX Way, KISS и прочим. Мне, создателю
Calmira GNU/Linux-libre это не нравится. Может быть, это одна из причин, по
которым я начал работу над этой системой. Как некоторый протест. Из-за включения
в основные дистрибутивы GNU/Linux несвободных компонентов, софта для слежки за
пользователем и прочего кала, GNU/Linux постепенно мутирует. Не удивительно, что
всякие Fedora, Ubuntu, openSUSE и прочие скоро могут превратиться  вжалкое
подобие Windows или MacOS. Я считаю это очень плохим -- GNU/Linux должен
сохранять своё лицо, а не копировать не самые хорошие вещи от популярных
несвободных ОС. Если уж и копировать/переномать что-либо, то только хорошие
вещи, а также только у правильных ОС. Например, у систем семейства BSD. Мне,
например, очень нравится FreeBSD, и некоторые вещи из неё я хочу перенять в
Calmira GNU/Linux-libre. Например, систему портов.

## 1. Не используйте несвободное программное обеспечение

Есть два типа программного обеспечения (ПО): свободное (СПО) и несвободное
(НПО). НПО -- это зло. Такое ПО может контролировать своих пользователей, может
включать в себя вредоносные компоненты. В данном случае не вы хозяин ПО, а ПО
ваш хозяин. У пользователя должно быть 4 свободы (по FSF):

1. Свобода использовать ПО без ограничений;
2. Свобода распространять ПО;
3. Свобода изучать исходный код ПО и модифицировать его при необходимости;
4. Свобода распространять модифицированные копии ПО.

Важно помнить, что и распространение НПО является нарушением свободы
пользователя. НПО создано лишь для насышения разработчиков деньгами, не более.
Несвободный софт прямо-таки занимается вымогательством и шантажом: "заплатите
разработчикам как можно больше денег, иначе мы следаем всё возможное, чтобы наша
программа не работала". Например, MicroSoft, урезающая функционал своей Windows
на период пробного периода, а после, по истечении этого периода, совсем
отрубающая возможность нормально использовать эту ОС. Всё это сделано для того,
чтобы содрать с пользователя как можно больше денег. Благо есть такие
инструменты, как активаторы, которые считаются нелегальными и нарушающими
лицензионное соглашение с пользователем, но такой софт помогает *нормальным*
людям противостоять такому наглому вмешательству в их жизнь производителей НПО.

## 2. Компромисс между функциональным СПО и легковесным СПО

К сожалению, с повышением мощности персональных компьютеров, программное
обеспечение становится всё жирнее и жирнее. Оно потребляет намного больше
ресурсов ПК, чем более ранние вещи, и это если учитывать то, что изменения в них
не настолько влияют на потребление.

Например, текстовый редактор Vim, в котором открыто несколько файлов, потребляет
около 10 Мб оперативной памяти. Когда как редактор GNOME Text Editor, в котором
открыт лишь один файл, потребляет около 70 Мб ОЗУ. Понятное дело, что есть
разница между консольным и графическим ПО, но их потребление различается в 7
раз, что довольно грустно.

Ни для кого не секрет, что современные дистрибутивы GNU/Linux стали очень
жирными, сложными и медленными. Конечно, с годами программное обеспечение
изменяется. Что-то в лучшую, а что-то и худшую сторону. Сама операционная
система GNU/Linux стала намного совершеннее, проще, надёжнее и красивее. Но не
стоит забывать истинное предназначение ОС -- быть миниатюрной прослойкой между
ПК и его пользователем. Ключевое слово здесь -- "миниатюрной". Дистрибутив
GNU/Linux должен потреблять минимум ресурсов ПК, чтобы максимум было доступно
для пользовательского ПО. Конечно, из-за особенностей использования ОЗУ ядром
Linux не всегда удаётся добиться нужного результата, но в большинстве случаев
можно получить желаемое. Однако, несмотря на легковесность, дистрибутив должен
отвечать базовым требованиям:

- Быть надёжным и стабильным, а также быстрым;
- Выполнять поставленные пользователем задачи.

Из этого следует, что не надо делать максимально компактный и легковесный
дистрибутив GNU/Linux (как, например, Floppinux, который помещается всего лишь
на одну дискету). Система должна быть пригодной для использования.

Так как дистрибутив Calmira GNU/Linux-libre и всё программное обеспечение
планируется запускать на самом разном оборудовании (как слабом, так и на
мощном), то всё программное обеспечение должно адекватно нагружать ПК и
адекватно потреблять его ресурсы в рамках разумного. Поэтому ПО должно соблюдать
некий компромисс между легковесностью и функциональностью.

Всё одобренное разработчиками Calmira GNU/Linux-libre программное обеспечение
содержится в системе портов. Кроме того, одобренное ПО, входящее в минимальную
поставку Calmira GNU/Linux (а в будущем -- и всё остальное, как входящее в
систему портов Calmira, так и отсутствующее в ней) есть на сайте
calmiralinux.github.io.

## 3. Использование логичных и простых инструментов; следование UNIX Way

При создании этого манифеста я был вдохновлён несколькими философиями и
принципами. Среди них были KISS (Keep it simple, stupid!) и UNIX Way. И я
считаю, что программное обеспечение должно быть простым и логичным. Под
простотой здесь подразумевается:

1. **Простая структура**. Она должна быть понятной среднестатистическому
   пользователю Calmira GNU/Linux-libre. В ней не должно быть ненужных
   усложнений и прочего, что портит логичность. Например, ключ `-h` должен
   вызывать короткую справку, а `-v` - показывать информацию о каждом шаге
   программы (verbose mode).
2. **Соответствие UNIX Way**. Пусть этот пункт выполняется далеко не всегда, но
   настоятельно советуется ему следовать для того, чтобы всё программное
   обеспечение в Calmira GNU/Linux было однотипным, предсказуемым и удобным.
   Программа должна делать что-то одно, и делать это хорошо.
3. **Предсказуемость**. Например, если `co /*` копирует все файлы из `/`, то `mv
   /*` должно перемещать все файлы из `/`, а не перемещать конкретный файл с
   именем `/*`.
4. **Софт не является мамкой**. Программное обеспечение не должно решать за
   пользователя, что ему требуется сделать. Все решения должен принимать
   конечный пользователь, а ПО, в крайнем случае, должно предупреждать его об
   опасности каких-либо действий пользователя.

Если обычному пользователю наплевать на инструменты работы с системой, то
продвинутым -- совсем нет. Они работают только с теми инструментами, к которым
привыкли, эти инструменты они хорошо знают. А переучивание вызывает раздражение,
а также способствует появлению ошибок в процессе изучения или работы, поэтому
дистрибутив Calmira GNU/Linux-libre требуется защитить от молниеносного и
быстрого перехода с одних инструментов на другие.

Кроме того, любое мало-мальски нормальное ПО должно иметь хорошую документацию,
которая освещает каждый аспект работы этого ПО и взаимодействия с ним
пользователей.

> На данный момент активно пишется документация дистрибутива Calmira
> GNU/Linux-libre, но ещё практически ничего не готово. Вы можете оказать нам
> помощь в работе над [Calmira GNU/Linux-libre
> Handbook](https://github.com/CalmiraLinux/handbook), начав работу по одному из
> существующих [issue](https://github.com/CalmiraLinux/handbook/issues). Если вы
> нашли проблему, но не знаете, как её исправить, либо не имеете для этого
> возможности, то, пожалуйста, создайте новое issue
> [здесь](https://github.com/CalmiraLinux/handbook/issues/new).

Хорошая документация к программному обеспечению привлекает не только новых
пользователей, но и новых разработчиков, поэтому забывать про неё нет никакого
смысла. Классическим форматом хранения, передачи и просмотра документации
являются [man-страницы](http://linux.die.net/man).

man'ы, всё-таки, это более offline инструмент. Если их вам не хватает, либо
документацию вы пишете для других целей, то используйте такие инструменты, как
Mkdocs (или Mkdocs Material), Docsify, Sphinx, Doxygen и прочие свободные
инструменты для создания документации. Локальные версии docs страниц,
сгенерированных с помощью этих инструментов, помещайте в соответствующую
поддиректорию директории `/usr/share/doc`.

## 4. Не поощряйте деятельность BLM и ЛГБТ_ABCDEFG...

"Деятельность" таких сборищ не должна приветствоваться в сообществе Calmira
GNU/Linux-libre. BLM из какого-то сообщества, действительно приносившего помощь
людям и обличавших настоящих расистов, переросла в сборище тупых идиотов,
борящихся против терминов `master`, `slave`, `black` и прочих в исходном коде
ПО.

С ЛГБТ всё очень просто - это люди с психическими отклонениями. Они не должны
никем поощряться, им не должен никто восхищаться. Но и делать из них изгоев и
потешаться над ними тоже нельзя - где вы видели цивилизованного человека,
который смеялся над шизофреником или аутистом?