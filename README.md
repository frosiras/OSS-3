# OSS-3
# Нагороднюк Никита

*Загружаем необходимые пакеты*
sudo yum install haveged  rpm-sign

*Создаем папку для создания новых пакетов rpmbuild
mkdir rpmbuild
mkdir ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

*Переходим в rpmbuild/SOURCES*
*Клонируем репозиторий*
git clone https://github.com/parazyd/git-restrict

*Переименонываем его, чтобы теперь у него была версия*
mv git-restrict git-restrict-1.0

*Меняем формат на tar.gz*
tar cvfz git-restrict-1.0.tar.gz git-restrict-1.0

*Переходим в папку rpmbuild/SPECS*
*Создаем с помощью nano файл git-restrict.spec*
*Выполняем сборку пакета*
rpmbuild -ba git-restrict.spec

*Переходим в папку rpmbuild/SOURCES/git-restrict-1.0*
*Исполненный файл выведет, что все тесты прошли успешно*
./test.sh

*Создадим ключ и экспортируем его в rpmbuild*
gpg2 --gen-key
gpg2 --export -a 'Nagorodniuk Nikita' > ~/rpmbuild/RPM-GPG-KEY-Nagorodniuk-Nikita

*Создадим в домашней директории .rpmmacros с помощью утилиты nano и запишем туда %_gpg_name Nagorodniuk Nikita*
*Перейдем в папку rpmbuild/RPMS/x86_64*
*Подпишем все пакеты*
rpm --addsign *.rpm
