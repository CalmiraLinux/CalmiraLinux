#include <iostream>
#include <iomanip>
#include <toml.hpp>

const char* _FILE = "/etc/calm-release";
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
    setlocale(LC_ALL, "ru_RU.UTF-8");
    toml::value start_value = system_data(_FILE);
    const auto& system_value = toml::find(start_value, "system");

    for(int i = 0; i <= 7; i++) {
        printf("\033[1m%*s\t\033[0m", 11, params[i]);
        std::cout << toml::find<std::string>(system_value, params[i]) << "\n";
        /* std::cout << "\033[1m" << params[i] << std::setw(15) << "\033[0m: "; */
        /* std::cout << toml::find<std::string>(system_value, params[i]) << "\n"; */
    }
    std::cout <<
        "\nCopyright (C) 2021, 2022 Michail Krasnov <linuxoid85@gmail.com>\n";
    std::cout <<
        "Copyright (C) 2022, Aristarh Bahirev <github.com/AristarhBahirev>\n";
    return 0;
}
