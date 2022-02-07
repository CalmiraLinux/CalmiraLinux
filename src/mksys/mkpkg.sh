#!/bin/bash
# Скрипт для генерации сборочных инструкций дистрибутива Calmira GNU/Linux-libre
# (C) 2022 Михаил Linuxoid85 Краснов <linuxoid85@gmail.com>
# For Calmira LX4 1.2 GNU/Linux-libre

PKG=$1

function check_file() {
    if [ -f "./packages/$PKG" ]; then
        echo "Пакет '$PKG' уже существует!"
        exit 1
    fi
}

function write_pkg() {
    content="#!/bin/bash -e\n\ntar -xf \ncd "
    echo -e $content > ./packages/$PKG
    gnome-text-editor ./packages/$PKG
}

check_file
write_pkg
