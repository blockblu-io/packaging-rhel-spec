# Blockblu IO spec file for libsecp256k1
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global libname libsecp256k1
%global soname  0

Name:           libsecp256k1-cardano
Version:        0.0.1
Release:        1%{?dist}
Summary:        Optimized C library for EC operations on curve secp256k1
Group:          Development/Libraries
ExclusiveArch:  %{_app_arch}

License:        MIT
Source0:        https://github.com/blockblu-io/secp256k1/archive/refs/tags/%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  pkg-config

Obsoletes:      %{libname}%{soname} <= %{version}

Packager:       Kevin Haller <kevin.haller@blockblu.io>


%description
Optimized C library for ECDSA signatures and secret/public key operations on curve secp256k1.

This library is intended to be the highest quality publicly available library for cryptography
on the secp256k1 curve. However, the primary focus of its development has been for usage in the
Bitcoin system and usage unlike Bitcoin's may be less well tested, verified, or suffer from a
less well thought out interface. Correct usage requires some care and consideration that the
library is fit for your application's purpose.


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
%setup -q -n "secp256k1-%{version}"


%build
%define _lto_cflags -flto=auto -ffat-lto-objects
./autogen.sh
%configure \
  --disable-silent-rules \
  --disable-opt \
  --enable-module-schnorrsig \
  --enable-experimental
%make_build


%install
%make_install
rm -f %{buildroot}%{_libdir}/%{libname}.la


%check
make check


%files
%license COPYING
%{_libdir}/%{libname}.so.%{soname}*

%files devel
%doc README.md
%doc SECURITY.md
%doc doc/*
%doc examples/*.{c,h}
%doc examples/EXAMPLES_COPYING
%{_includedir}/secp256k1.h
%{_includedir}/secp256k1_extrakeys.h
%{_includedir}/secp256k1_preallocated.h
%{_includedir}/secp256k1_schnorrsig.h
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%files static
%{_libdir}/%{libname}.a


%changelog
* Thu May 26 2022 Kevin Haller <kevin.haller@blockblu.io>
- Initial package