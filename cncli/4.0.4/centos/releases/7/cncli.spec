# Blockblu IO spec file for CNCLI by Andrew Westberg
#
# License: MIT
# http://opensource.org/licenses/MIT
#
Name:           cncli
Version:        4.0.4
Release:        2%{?dist}
Summary:        A community-based cardano-node CLI tool
Group:          Development/Tools
ExclusiveArch:  %{_app_arch}
Source0:        https://github.com/cardano-community/cncli/archive/refs/tags/v%{version}.tar.gz

License:        Apache License 2.0
URL:            https://github.com/AndrewWestberg/cncli

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

Requires:       libsodium

Packager:       Kevin Haller <kevin.haller@blockblu.io>


%description
A community-based cardano-node CLI tool. It's a collection of utilities to 
enhance and extend beyond those available with the cardano-cli.


%prep
git clone --recurse-submodules https://github.com/AndrewWestberg/cncli.git .
git fetch --all --tags && git checkout -f tags/v%{version} --quiet


%build
RUST_BACKTRACE=full cargo install --path . --root .


%install
install -Dpm 0755 ./bin/%{name} %{buildroot}%{_bindir}/%{name}


%check
echo "$(%{buildroot}%{_bindir}/%{name} --version)" | grep "cncli %{version}"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%license LICENSE
%doc INSTALL.md USAGE.md README.md
%{_bindir}/%{name}


%changelog
* Thu May 26 2022 Kevin Haller <kevin.haller@blockblu.io>
- Making use of git repository as source, ideally tar 
- source would be used, but couldn't make it work
* Mon Dec 27 2021 Kevin Haller <kevin.haller@blockblu.io>
- Initial package