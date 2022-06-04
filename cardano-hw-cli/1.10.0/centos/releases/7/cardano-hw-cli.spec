# Blockblu IO spec file for cardano-hw-cli
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global debug_package %{nil}

Name:           cardano-hw-cli
Version:        %{_app_version}
Release:        2%{?dist}
Summary:        Cardano CLI tool for hardware wallets
Group:          Development/Tools
BuildArch:      %{_app_arch}

License:        ISC
Source0:        https://github.com/vacuumlabs/cardano-hw-cli/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  python3
BuildRequires:  rh-nodejs14

Packager:       Kevin Haller <kevin.haller@blockblu.io>


%description
Cardano CLI tool for signing transactions with hardware wallets. Its command-line
interface is based on the official cardano-cli tool.


%prep
%setup -q -n "%{name}-%{version}"


%build
npm install
npm run build-js
nexe --verbose --build ./dist/index.js -o cardano-hw-cli --python /usr/bin/python3


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc package.json
%doc build/dependencies/linux/Release/HID.node
%doc build/dependencies/linux/Release/HID_hidraw.node
%{_bindir}/%{name}


%changelog
* Fri May 20 2022 Kevin Haller <kevin.haller@blockblu.io>
- Vacuumlabs removed the usb_bindings.node documentation file
- Vacuumlabs renamed the HID-hidraw.node documentation file
* Thu Dec 23 2021 Kevin Haller <kevin.haller@blockblu.io>
- Initial package