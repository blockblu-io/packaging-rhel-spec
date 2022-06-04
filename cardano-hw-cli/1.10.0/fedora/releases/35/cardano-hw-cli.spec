# Blockblu IO spec file for cardano-hw-cli
#
# License: MIT
# http://opensource.org/licenses/MIT
#
%global debug_package %{nil}

%global commit cd28f24c19c32ad2087944a2faff76714bfbdf77

Name:           cardano-hw-cli
Version:        1.10.0
Release:        2%{?dist}
Summary:        Cardano CLI tool for hardware wallets
Group:          Development/Tools
BuildArch:      %{_app_arch}

License:        ISC
Source0:        https://github.com/vacuumlabs/cardano-hw-cli/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  npm

Packager:       Kevin Haller <kevin.haller@blockblu.io>


%description
Cardano CLI tool for signing transactions with hardware wallets. Its command-line
interface is based on the official cardano-cli tool.


%prep
%setup -q -n "%{name}-%{version}"


%build
cp package.json _package.json
sed -i '2 i \ \ "commit":"'%{commit}'",' _package.json
yarn install
yarn run build-js
yarn nexe --build --empty
yarn nexe ./dist/index.js -o cardano-hw-cli --build --verbose


%install
install -Dpm 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 0755 _package.json %{buildroot}%{_datadir}/cardano-hw-cli/package.json
install -Dpm 0755 build/dependencies/linux/Release/HID.node %{buildroot}%{_datadir}/cardano-hw-cli/Release/HID.node
install -Dpm 0755 build/dependencies/linux/Release/HID_hidraw.node %{buildroot}%{_datadir}/cardano-hw-cli/Release/HID_hidraw.node


%check
echo "$(%{buildroot}%{_bindir}/%{name} version)" | grep "Cardano HW CLI Tool version %{version}"
echo "$(%{buildroot}%{_bindir}/%{name} version)" | grep "Commit hash: %{commit}"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc README.md
%doc docs/*.md
%{_bindir}/%{name}
%{_datadir}/cardano-hw-cli/package.json
%{_datadir}/cardano-hw-cli/Release/*


%changelog
* Tue May 31 2022 Kevin Haller <kevin.haller@blockblu.io>
- adds tests for checking whether compiled binary works
- adds the commit hash to package json
* Fri May 20 2022 Kevin Haller <kevin.haller@blockblu.io>
- Vacuumlabs removed the usb_bindings.node documentation file
- Vacuumlabs renamed the HID-hidraw.node documentation file
* Thu Dec 23 2021 Kevin Haller <kevin.haller@blockblu.io>
- Initial spec file