# Blockblu IO spec file for cardano-node
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global debug_package %{nil}

Name:           cardano-cli
Version:        %{_app_version}
Release:        %{_app_release}%{?dist}
Summary:        CLI tool to interact with a Cardano node.
Group:          Applications/Communications
ExclusiveArch:  %{_app_arch}
Source0:        cardano-node-%{_app_version}.tar.gz

License:        Apache License 2.0
URL:            https://github.com/input-output-hk/cardano-node

BuildRequires:  cabal-install
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghc
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  git
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  ncurses-compat-libs
BuildRequires:  ncurses-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel

Requires:       libsodium

Packager:       Kevin Haller <kevin.haller@blockblu.io>

%description
A CLI tool to interact with the cardano-node, which is the core component
that is used to participate in a Cardano decentralised blockchain.


%prep
%setup -q -n cardano-node-%{_app_version}


%build
cabal v2-update
%ghc_set_gcc_flags
cabal v2-build cardano-cli
mkdir -p %{_builddir}/cardano-node-%{_app_version}/bin
cp $(find %{_builddir}/cardano-node-%{_app_version}/dist-newstyle/build -name cardano-cli -type f -executable) %{_builddir}/cardano-node-%{_app_version}/bin


%install
install -Dpm 0755 %{_builddir}/cardano-node-%{_app_version}/bin/%{name} %{buildroot}%{_bindir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%license LICENSE
%doc README.rst
%{_bindir}/%{name}


%changelog
* Sun May 22 2022 Kevin Haller <kevin.haller@blockblu.io>
- Initial package
