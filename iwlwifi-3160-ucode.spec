Summary:	Intel Wireless 3160 microcode
Name:		iwlwifi-3160-ucode
Version:	25.228.9.0
Release:	1
Source0:	http://www.intellinuxwireless.org/iwlwifi/downloads/%{name}-%{version}.tgz
License:	Proprietary
Group:		System/Kernel and hardware
Url:		http://intellinuxwireless.org/
BuildArch: noarch

%description
The file iwlwifi-3160-*.ucode provided in this package is required to be
present on your system in order for the Intel Wireless 3160 Network
Connection Adapter driver for Linux (iwlagn) to be able to operate on
your system.

%prep
%setup -q

%build

%install
install -d %{buildroot}/lib/firmware
install -m644 *.ucode %{buildroot}/lib/firmware/


%files
%doc LICENSE.* README.*
/lib/firmware/*.ucode
