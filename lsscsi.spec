# NOTE: beta versions are versioned with just new version number,
#       so check URL for final releases
Summary:	Utility that uses sysfs to list SCSI devices and SCSI hosts
Summary(pl.UTF-8):	Narzędzie używające sysfs-a do wypisywania urządzeń i hostów SCSI
Name:		lsscsi
Version:	0.26
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://sg.danny.cz/scsi/%{name}-%{version}.tgz
# Source0-md5:	624d705899ed08e872e164679ac56545
URL:		http://sg.danny.cz/scsi/lsscsi.html
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl.UTF-8
Polecenie lsscsi w celu uzyskania informacji odczytuje system plików
sysfs (zwykle podmontowany pod /sys) zamiast otwierania plików
urządzeń SCSI (np. /dev/sda) w systemie. Odczyt informacji z systemu
plików sysfs jest zwykle dostępny dla wszystkich użytkowników
(podobnie jak informacje w procfs). Jednak uprawnienia do plików
urządzeń SCSI muszą być ograniczone, aby nie pozwolić na bezpośredni
dostęp przez użytkowników do tych urządzeń. Polecenie lsscsi zwykle
jest dostępne dla wszystkich użytkowników.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
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
