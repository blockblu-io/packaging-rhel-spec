# Blockblu IO spec file for libsodium fork of IOG
#
# Big parts of this spec file are inspired by the
# libsodium spec file of the Fedora project.
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global libname libsodium
%global soname  23

Name:           libsodium
Version:        1.0.18
Release:        92%{?dist}
Summary:        The Sodium crypto library (IOG fork)
Group:          Development/Libraries
ExclusiveArch:  %{_app_arch}

License:        ISC
Source0:        https://github.com/blockblu-io/libsodium/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  pkgconfig

Obsoletes:      %{libname}%{soname} <= %{version}

Packager:       Kevin Haller <kevin.haller@blockblu.io>


%description
Sodium is a new, easy-to-use software library for encryption, decryption,
signatures, password hashing and more. It is a portable, cross-compilable,
installable, packageable fork of NaCl, with a compatible API, and an extended
API to improve usability even further. Its goal is to provide all of the core
operations needed to build higher-level cryptographic tools. The design
choices emphasize security, and "magic constants" have clear rationales.

IOG (and Algorand team) created a fork of Sodium to implement a draft of
"Verifiable Random Functions". This package provides this fork of IOG.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{libname}%{soname}-devel <= %{version}

%description    devel
This package contains libraries and header files for
developing applications that use %{name} libraries.


%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      %{libname}%{soname}-static <= %{version}

%description    static
This package contains the static library for statically
linking applications to use %{name}.


%prep
%setup -q


%build
%define _lto_cflags -flto=auto -ffat-lto-objects
./autogen.sh
%configure \
  --disable-silent-rules \
  --disable-opt
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/%{libname}.la


%check
make check


%files
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}*

%files devel
%doc AUTHORS ChangeLog README.markdown THANKS
%doc test/default/*.{c,exp,h}
%doc test/quirks/quirks.h
%{_includedir}/sodium.h
%{_includedir}/sodium/
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%files static
%{_libdir}/libsodium.a


%changelog
* Thu May 19 2022 Kevin Haller <kevin.haller@blockblu.io>
- Renames the package to libsodium without -iog suffix
- Add a release number that is newer than original release
* Thu Dec 23 2021 Kevin Haller <kevin.haller@blockblu.io>
- Initial package, inspired by libsodium.spec file of fedora project