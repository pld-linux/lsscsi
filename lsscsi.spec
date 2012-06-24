Summary:	Utility that uses sysfs to list SCSI devices and SCSI hosts
Summary(pl):	Narz�dzie u�ywaj�ce sysfs-a do wypisywania urz�dze� i host�w SCSI
Name:		lsscsi
Version:	0.19
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://sg.torque.net/scsi/%{name}-%{version}.tgz
# Source0-md5:	bc80ef8ae775e8640f40603bf761aeb9
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
Polecenie lsscsi w celu uzyskania informacji odczytuje system plik�w
sysfs (zwykle podmontowany pod /sys) zamiast otwierania plik�w
urz�dze� SCSI (np. /dev/sda) w systemie. Odczyt informacji z systemu
plik�w sysfs jest zwykle dost�pny dla wszystkich u�ytkownik�w
(podobnie jak informacje w procfs). Jednak uprawnienia do plik�w
urz�dze� SCSI musz� by� ograniczone, aby nie pozwoli� na bezpo�redni
dost�p przez u�ytkownik�w do tych urz�dze�. Polecenie lsscsi zwykle
jest dost�pne dla wszystkich u�ytkownik�w.

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
%attr(755,root,root) %{_bindir}/lsscsi
%{_mandir}/man8/lsscsi.8*
