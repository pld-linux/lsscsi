Summary:	Utility that uses sysfs to list SCSI devices and SCSI hosts
Summary(pl):	Narzêdzie u¿ywaj±ce sysfs-a do wypisywania urz±dzeñ i hostów SCSI
Name:		lsscsi
Version:	0.16
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://sg.torque.net/scsi/%{name}-%{version}.tgz
# Source0-md5:	52c1672e36ad0d9a5ef75cccae4831c6
URL:		http://sg.torque.net/scsi/lsscsi.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The lsscsi command accesses the sysfs file system (usually mounted
under /sys ) to obtain information rather than opening the SCSI device
nodes (e.g. /dev/sda) in the system. Reading information within the
sysfs file system is usually available to all users (as is the
information in procfs). However the permissions on SCSI device nodes
are necessarily tight which precludes normal users from directly
interrogating these devices. The lsscsi command will typically be
available to all users.

%description -l pl
Polecenie lsscsi w celu uzyskania informacji odczytuje system plików
sysfs (zwykle podmontowany pod /sys) zamiast otwierania plików
urz±dzeñ SCSI (np. /dev/sda) w systemie. Odczyt informacji z systemu
plików sysfs jest zwykle dostêpny dla wszystkich u¿ytkowników
(podobnie jak informacje w procfs). Jednak uprawnienia do plików
urz±dzeñ SCSI musz± byæ ograniczone, aby nie pozwoliæ na bezpo¶redni
dostêp przez u¿ytkowników do tych urz±dzeñ. Polecenie lsscsi zwykle
jest dostêpne dla wszystkich u¿ytkowników.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
