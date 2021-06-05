Name:       git-restrict
Version:    1.0
Release:    1%{?dist}
Summary:    git-restrict tool
Group:      Test
License:    GNU Affero General Public License version 3.
URL:        https://github.com/parazyd/git-restrict
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc
Requires: git ssh
 
%description
A minimal utility that allows repository permission management based on
ssh keys when used with the command directive in ssh's authorized_keys
file.
 
If used, it will only allow `git-upload-pack` and `git-receive-pack` as
the commands allowed to be ran by a specific user/SSH key.
 
git-restrict is also compiled as a static binary so it's easy to use it
in chroot environments. This is obviously intentional.

%prep
%setup -q
 
%build
gcc -g git-restrict.c -o git-restrict
 
%install
mkdir -p %{buildroot}%{_bindir}
cp git-restrict %{buildroot}%{_bindir}
 
%files
%{_bindir}/git-restrict
 
%changelog
* Sat Jun 05 2021 <Nagorodniuk Nikita>
- Added %{_bindir}/git-restrict
