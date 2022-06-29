/*
 * Calmira ver
 * Copyright (C) 2021, 2022 Michail Krasnov <linuxoid85@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <toml.hpp>

const char* file = "/etc/calm-release";
const char* params[] = {
    "name",
    "version",
    "codename",
    "description",
    "arch",
    "build",
    "build_date",
    "edition"
};

toml::value system_data(const char* config) {
    toml::value data = toml::parse(config);
    return data;
}

int main() {
    toml::value start_value = system_data(file);
    const auto& system_value = toml::find(start_value, "system");

    for(int i = 0; i <= 7; i++) {
        printf("\033[1m%*s: \033[0m", 11, params[i]);
        std::cout << toml::find<std::string>(system_value, params[i]) << "\n";
    }
    std::cout <<
        "\nCopyright (C) 2021, 2022 Michail Krasnov <linuxoid85@gmail.com>\n";
    std::cout <<
        "Copyright (C) 2022, Aristarh Bahirev <github.com/AristarhBahirev>\n";
    return 0;
}
