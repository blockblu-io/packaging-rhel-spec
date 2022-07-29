# Blockblu IO spec file for cardano-node
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global debug_package %{nil}

%global commit  9f1d7dc163ee66410d912e48509d6a2300cfa68a

Name:           cardano-cli
Version:        1.35.0
Release:        1%{?dist}
Summary:        CLI tool to interact with a Cardano node.
Group:          Applications/Communications
ExclusiveArch:  %{_app_arch}

Source0:        https://github.com/input-output-hk/cardano-node/archive/refs/tags/%{version}.tar.gz
Patch1:         git-rev-commit-hash-env.patch

License:        Apache License 2.0
URL:            https://github.com/input-output-hk/cardano-node

BuildRequires:  cabal-install
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ghc
BuildRequires:  git
BuildRequires:  gmp-devel
BuildRequires:  make
BuildRequires:  ncurses-compat-libs
BuildRequires:  ncurses-devel
BuildRequires:  libsecp256k1-cardano-devel
BuildRequires:  libsodium-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  systemd-devel
BuildRequires:  zlib-devel

Requires:       gmp
Requires:       ncurses-compat-libs
Requires:       ncurses
Requires:       libsecp256k1-cardano
Requires:       libsodium
Requires:       systemd
Requires:       zlib

Packager:       Kevin Haller <kevin.haller@blockblu.io>

%description
A CLI tool to interact with a Cardano node (Haskell implementation), which is
the core component that is used to participate in a Cardano decentralised blockchain.


%prep
%setup -q -n cardano-node-%{version}
%patch1 -p1 -b .orig


%build
cabal v2-update
CN_GIT_COMMIT_REV=%{commit} cabal v2-build %{name}
mkdir -p ./bin
cp $(find ./dist-newstyle/build -name %{name} -type f -executable) ./bin


%install
install -Dpm 0755 ./bin/%{name} %{buildroot}%{_bindir}/%{name}


%check
echo "$(%{buildroot}%{_bindir}/%{name} version)" | grep "cardano-cli %{version}"
echo "$(%{buildroot}%{_bindir}/%{name} version)" | grep "git rev %{commit}"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%license LICENSE
%doc README.rst
%{_bindir}/%{name}


%changelog
* Tue May 24 2022 Kevin Haller <kevin.haller@blockblu.io>
- Initial package
